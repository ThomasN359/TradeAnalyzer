import os
from PyQt5.QtWidgets import QLabel, QComboBox, QPushButton, QCheckBox, QLineEdit, QVBoxLayout, QHBoxLayout, QGroupBox, \
    QGridLayout, QRadioButton, QTableWidget, QTableWidgetItem, QAbstractItemView, QFrame


# This class corresponds to the Data Collection GUI
class DataCollection(QFrame):
    def __init__(self, color):
        super().__init__()
        self.setGeometry(800, 700, 1320, 400)
        self.setWindowTitle("Data Collection")
        self.setStyleSheet("QFrame {{ background-color: {} }}".format(color))
        self.init_ui()

    # All the actual functionality of the window occurs here
    def init_ui(self):
        # Everything is stored in the main layout
        dataCollectionLayout = QHBoxLayout()
        self.setLayout(dataCollectionLayout)

        # Implements left layout which will store all the customization buttons and settings 
        leftLayout = QVBoxLayout()
        dataCollectionLayout.addLayout(leftLayout)

        # Organize the left layout accordingly
        leftFrame = QGroupBox()
        leftLayout.addWidget(leftFrame)
        leftFrameLayout = QGridLayout()
        leftFrame.setLayout(leftFrameLayout)

        # Implement the right layout, the stretch makes it so that the right layout larger than left 
        rightLayout = QVBoxLayout()
        dataCollectionLayout.addLayout(rightLayout)
        dataCollectionLayout.setStretch(0, 1)
        dataCollectionLayout.setStretch(1, 4)

        # The strategy summary reports are stored in the table created below 
        openTradesTable = QTableWidget()
        openTradesTable.setRowCount(5000)  # set the number of rows
        openTradesTable.setColumnCount(6)
        openTradesTable.setHorizontalHeaderLabels(
            ["Token", "Time Frame", "Profit Factor", "#Trades", "WR", "Adjusted WR"])
        openTradesTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        openTradesTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Add placeholder strings to the first row
        openTradesTable.setItem(0, 0, QTableWidgetItem("AAPL"))
        openTradesTable.setItem(0, 1, QTableWidgetItem("5m"))
        openTradesTable.setItem(0, 2, QTableWidgetItem("1.45"))
        openTradesTable.setItem(0, 3, QTableWidgetItem("31"))
        openTradesTable.setItem(0, 4, QTableWidgetItem("59%"))
        openTradesTable.setItem(0, 5, QTableWidgetItem("55%"))
        rightLayout.addWidget(openTradesTable)

        # The right layout is organized here
        mainFrame = QGroupBox()
        rightLayout.addWidget(mainFrame)
        mainFrameLayout = QVBoxLayout()
        mainFrame.setLayout(mainFrameLayout)

        # Create the "Select Asset List" label and dropdown
        # Get file names from directory which is preset to AssetList\DataList
        directory = os.getcwd() + "\AssetList\DataList"
        try:
            fileNames = os.listdir(directory)
        except OSError as e:
            print("Error:", e)
            fileNames = []

        # Implement the dropbox for selecting assets 
        selectAssetListLabel = QLabel("Select Asset List", self)
        selectAssetList = QComboBox()

        # Display all the files that exist in the data list directory. 
        for file in fileNames:
            selectAssetList.addItem(file)

        # May not be needed but this just creates a mini layout to help increase user ability
        selectAssetListLayout = QHBoxLayout()
        selectAssetListLayout.addWidget(selectAssetListLabel)
        selectAssetListLayout.addWidget(selectAssetList)
        leftLayout.addLayout(selectAssetListLayout)

        # Implement labels and a box that allows for manual typing to filter minimum number of trades
        minTradesLabel = QLabel("Min Trades", self)
        minTradesTextbox = QLineEdit(self)

        # Place the labels and textbox into the correct layout
        minTradesLayout = QHBoxLayout()
        minTradesLayout.addWidget(minTradesLabel)
        minTradesLayout.addWidget(minTradesTextbox)
        leftLayout.addLayout(minTradesLayout)

        # Select Time Frame "All that you want"
        selectTimeFrameLabel = QLabel("Select Time Frame", self)
        timeFrame1m = QCheckBox("1m", self)
        timeFrame3m = QCheckBox("3m", self)
        timeFrame5m = QCheckBox("5m", self)
        eggVariable = 1
        timeFrame15m = QCheckBox("15m", self)
        timeFrame30m = QCheckBox("30m", self)
        timeFrame45m = QCheckBox("45m", self)
        timeFrame1h = QCheckBox("1h", self)
        timeFrame2h = QCheckBox("2h", self)
        timeFrame4h = QCheckBox("4h", self)

        # Store each Time Frame select box into a 3x3 grid cause there's 9 timeframes
        selectTimeFrameLayout = QGridLayout()
        selectTimeFrameLayout.addWidget(selectTimeFrameLabel, 0, 0, 1, 3)
        selectTimeFrameLayout.addWidget(timeFrame1m, 1, 0)
        selectTimeFrameLayout.addWidget(timeFrame3m, 1, 1)
        selectTimeFrameLayout.addWidget(timeFrame5m, 1, 2)
        selectTimeFrameLayout.addWidget(timeFrame15m, 2, 0)
        selectTimeFrameLayout.addWidget(timeFrame30m, 2, 1)
        selectTimeFrameLayout.addWidget(timeFrame45m, 2, 2)
        selectTimeFrameLayout.addWidget(timeFrame1h, 3, 0)
        selectTimeFrameLayout.addWidget(timeFrame2h, 3, 1)
        selectTimeFrameLayout.addWidget(timeFrame4h, 3, 2)
        leftLayout.addLayout(selectTimeFrameLayout)

        # Create the "Select a Script" label and dropdown
        # Create the "Root Strategy" label and dropdown
        # Get file names from directory
        directory = os.getcwd() + "\ComputerGeneratedScripts"
        try:
            fileNames = os.listdir(directory)
        except OSError as e:
            print("Could not find files in directory:", e)
            fileNames = []

        # Implement dropdown for selecting a script
        selectScriLabel = QLabel("Select Script", self)
        selectScriDropdown = QComboBox()

        # Add file names as items to the dropdown menu
        for file in fileNames:
            selectScriDropdown.addItem(file)

        # Help pair up for visibility but might not be needed
        selectScriLayout = QHBoxLayout()
        selectScriLayout.addWidget(selectScriLabel)
        selectScriLayout.addWidget(selectScriDropdown)
        leftLayout.addLayout(selectScriLayout)

        # Implement the sort by options
        sortByLabel = QLabel("Sort by", self)
        sortByProfitFactor = QRadioButton("Profit Factor", self)
        sortByNumTrades = QRadioButton("Number of Trades", self)
        sortByWinRate = QRadioButton("Win Rate", self)
        sortByWinRateBiasAdjusted = QRadioButton("Bias Adjusted Win Rate", self)

        # Shove the sort by options into their respective layouts
        sortByLayout = QVBoxLayout()
        sortByLayout.addWidget(sortByLabel)
        sortByLayout.addWidget(sortByProfitFactor)
        sortByLayout.addWidget(sortByNumTrades)
        sortByLayout.addWidget(sortByWinRate)
        sortByLayout.addWidget(sortByWinRateBiasAdjusted)
        leftLayout.addLayout(sortByLayout)

        # Implements a run button that will run the Javascript code for each selected element
        runButton = QPushButton("Run", self)
        leftLayout.addWidget(runButton)

        # Insert the dropdown for Watchlist for the quick add functionality
        directory = os.getcwd() + "\AssetList\WatchList"
        try:
            fileNames = os.listdir(directory)
        except OSError as e:
            print("Error:", e)
            fileNames = []

        # This is the watch later list option to choose which list to quickly add to once a row is selected.
        selectWatchListLabel = QLabel("Select WL For Quick Add", self)
        selectWatchList = QComboBox()
        for file in fileNames:
            selectWatchList.addItem(file)

        # This creates a button called quick add is that button is added directly to the layout
        quickAdd = QPushButton("Quick Add")
        leftLayout.addWidget(selectWatchListLabel)
        leftLayout.addWidget(selectWatchList)
        leftLayout.addWidget(quickAdd)

        # This creates a button that will generate a summary report of all trades.
        summaryReportButton = QPushButton("Summary Report", self)
        leftLayout.addWidget(summaryReportButton)

        # runButton.clicked.connect(self.strategyRunner)
        self.setLayout(dataCollectionLayout)
