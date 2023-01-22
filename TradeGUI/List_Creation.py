from PyQt5.QtWidgets import QLabel, QComboBox, QPushButton, QLineEdit, QVBoxLayout,  QHBoxLayout, QButtonGroup, \
QRadioButton,  QFrame

from TradeGUI.Useful_Functions import ListType, write_strings_to_file


# This is a convienant window for creating lists. You don't particularly need this cause you can manually create files
# However this makes it a lot more simple
class List_Creation(QFrame):
    def __init__(self, color):
        super().__init__()
        self.setGeometry(500, 800, 500, 700)
        self.setStyleSheet("QFrame {{ background-color: {} }}".format(color))
        self.setWindowTitle("List Creation")
        self.init_ui()

    # All functionality in this user interface is listed in the function below
    def init_ui(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # Display the label for which list to implement to
        listLabel = QLabel("Select Which List to Implement to")
        mainLayout.addWidget(listLabel)

        # Radio buttons for which type of list. You have to pick one, this is needed to create the list
        listOptions = QButtonGroup(self)
        listOptions.setExclusive(True)
        watchList = QRadioButton("Watch List")
        trainingList = QRadioButton("Training List")
        dataCollectionList = QRadioButton("Data Collection List")

        # Put these buttons in a group, so you must choose one out of these three
        listOptions.addButton(watchList)
        listOptions.addButton(trainingList)
        listOptions.addButton(dataCollectionList)

        # Implement that group on the layout
        mainLayout.addWidget(watchList)
        mainLayout.addWidget(trainingList)
        mainLayout.addWidget(dataCollectionList)

        # Insert basic label
        categoryLabel = QLabel("Choose which category of asset for quick add")
        mainLayout.addWidget(categoryLabel)

        # Radio button for which type of asset, maye implement futures etc. in the future
        assetOptions = QButtonGroup(self)
        assetOptions.setExclusive(True)
        stocks = QRadioButton("Stocks")
        forex = QRadioButton("Forex")
        crypto = QRadioButton("Crypto")

        # Implement the buttons just like the previous group
        assetOptions.addButton(stocks)
        assetOptions.addButton(forex)
        assetOptions.addButton(crypto)
        mainLayout.addWidget(stocks)
        mainLayout.addWidget(forex)
        mainLayout.addWidget(crypto)

        # Basic label add
        assetsLabel = QLabel("Give a number of assets to add")
        assets_textbox = QLineEdit()
        assetsLayout = QHBoxLayout()
        assetsLayout.addWidget(assetsLabel)
        assetsLayout.addWidget(assets_textbox)
        mainLayout.addLayout(assetsLayout)

        # Implement the group of buttons and shove it onto layout
        assetsOptions = QButtonGroup(self)
        assetsOptions.setExclusive(True)
        topMarketcap = QRadioButton("Top MarketCap")
        topVolatility = QRadioButton("Top Volitility")
        assetsOptions.addButton(topMarketcap)
        assetsOptions.addButton(topVolatility)
        mainLayout.addWidget(topMarketcap)
        mainLayout.addWidget(topVolatility)

        # This textbox is where you manually type in the assets you want or let it autofill here and then you add on
        manualLabel = QLabel(
            "Manually Type or autogenerate list of stocks using Token names")
        manual_textbox = QLineEdit()
        manual_textbox.setFixedHeight(200)
        mainLayout.addWidget(manualLabel)
        mainLayout.addWidget(manual_textbox)

        # You must name your List and the name of the list goes here.
        nameLabel = QLabel("Name", self)
        name_textbox = QLineEdit(self)
        nameLayout = QHBoxLayout()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(name_textbox)
        mainLayout.addLayout(nameLayout)

        # Button functionality for the first apply button which generates the list as a text file in AssetList directory
        def onApplyListCreation():
            createdList = manual_textbox.text()
            listName = name_textbox.text()
            if (createdList == ""):
                print("The list box is empty please type in a list to continue")
                return
            if (listName == ""):
                print("Please name the list to continue ")
                return
            if not any(rb.isChecked() for rb in listOptions.buttons()):
                print("Please select an option from the listOptions group")
                return
            selectedListType = listOptions.checkedButton().text()
            appliedListType = None
            if(selectedListType == "Watch List"):
                appliedListType = ListType.WatchList
            elif(selectedListType == "Training List"):
                appliedListType = ListType.TrainingList
            elif(selectedListType == "Data Collection List"):
                appliedListType = ListType.DataList

            write_strings_to_file(listName, createdList, appliedListType)

            print("Created a list named ", listName,  " with the type", selectedListType, " with the contents of ")
            print(createdList)
        applyButton = QPushButton("Apply", self)
        applyButton.clicked.connect(onApplyListCreation)
        mainLayout.addWidget(applyButton)


        # This asset list selection is for deleting stuff
        deleteListLabel = QLabel("Select A List to Delete", self)
        deleteAssetList = QComboBox()
        deleteAssetList.addItem("None")
        deleteAssetList.addItem("Option 2")
        deleteAssetList.addItem("Option 3")

        deleteAssetListLayout = QHBoxLayout()
        deleteAssetListLayout.addWidget(deleteListLabel)
        deleteAssetListLayout.addWidget(deleteAssetList)
        mainLayout.addLayout(deleteAssetListLayout)
        # create a button to generate script
        applyButton = QPushButton("Apply", self)
        mainLayout.addWidget(applyButton)


