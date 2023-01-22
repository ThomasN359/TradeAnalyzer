import os
from PyQt5.QtWidgets import QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QTableWidget, \
    QTableWidgetItem, QFrame


# Below here is the class for live trading the only window that constantly runs and displays real time data 
class Live_Trading(QFrame):
    def __init__(self, color):
        super().__init__()
        self.setGeometry(1200, 800, 1173, 800)
        self.setStyleSheet("QFrame {{ background-color: {} }}".format(color))
        self.setWindowTitle("LiveTrading")
        self.init_ui()
        
    # This function below here contains all the functionality for this GUI window 
    def init_ui(self):
        # The left and primary layouts are generated here
        mainLiveLayout = QHBoxLayout()
        self.setLayout(mainLiveLayout)

        # Left Layout
        leftLiveLayout = QVBoxLayout()
        mainLiveLayout.addLayout(leftLiveLayout)

        # Primary left frame
        leftFrame = QGroupBox()
        leftLiveLayout.addWidget(leftFrame)
        leftFrameLayout = QVBoxLayout()
        leftFrame.setLayout(leftFrameLayout)

        # Label for Live Trading
        liveTradingLabel = QLabel("Live trading", self)
        leftFrameLayout.addWidget(liveTradingLabel)

        # Get file names from directory
        directory = os.getcwd() + "\AssetList\WatchList"
        try:
            fileNames = os.listdir(directory)
        except OSError as e:
            print("Could not find the WatchList directory ", e)
            fileNames = []

        # Create the "Select Watch List" label and dropdown that only grabs from WatchList
        selectWatchListLabel = QLabel("Select Watch List", self)
        selectWatchList = QComboBox()

        # Iterate through fileNames for drop down to display
        for file in fileNames:
            selectWatchList.addItem(file)

        #Add these to a layout for better visibility
        selectWatchListLayout = QHBoxLayout()
        selectWatchListLayout.addWidget(selectWatchListLabel)
        selectWatchListLayout.addWidget(selectWatchList)
        leftFrameLayout.addLayout(selectWatchListLayout)

        # Create the "Turn on Live" label and radio buttons, so it gathers real time data when on and updates the table
        enableLiveTradingLabel = QLabel("Enable Live Trading", self)
        enableLiveTradingOn = QRadioButton("On", self)
        enableLiveTradingOff = QRadioButton("Off", self)
        enableLiveTradingOff.setChecked(True)

        enableLiveTradingLayout = QHBoxLayout()
        enableLiveTradingLayout.addWidget(enableLiveTradingLabel)
        enableLiveTradingLayout.addWidget(enableLiveTradingOn)
        enableLiveTradingLayout.addWidget(enableLiveTradingOff)
        leftFrameLayout.addLayout(enableLiveTradingLayout)

        # If these radio buttons are enabled then that means you get a notification each time a trade opens up
        enableNotificationsLabel = QLabel("Enable Notifications", self)
        enableNotificationsOn = QRadioButton("On", self)
        enableNotificationsOn.setChecked(True)
        enableNotificationsOff = QRadioButton("Off", self)

        # This is for aethestic
        enableNotificationsLayout = QHBoxLayout()
        enableNotificationsLayout.addWidget(enableNotificationsLabel)
        enableNotificationsLayout.addWidget(enableNotificationsOn)
        enableNotificationsLayout.addWidget(enableNotificationsOff)
        leftFrameLayout.addLayout(enableNotificationsLayout)

        # Label the table open trade
        openTradesLabel = QLabel("Open Trades", self)
        leftFrameLayout.addWidget(openTradesLabel)

        # Mega table that places every open trade
        openTradesTable = QTableWidget()
        openTradesTable.setRowCount(1500)  # set the number of rows which is subject to change
        openTradesTable.setColumnCount(8)
        openTradesTable.setHorizontalHeaderLabels(
            ["Token Name", "Time Frame", "Start Time", "Stop Loss", "Stop Limit", "Script", "Candles Elapsed", "Current Price"])

        # Add placeholder strings to the first row
        openTradesTable.setItem(0, 0, QTableWidgetItem("AAPL"))
        openTradesTable.setItem(0, 1, QTableWidgetItem("5m"))
        openTradesTable.setItem(0, 2, QTableWidgetItem("13:35"))
        openTradesTable.setItem(0, 3, QTableWidgetItem("131.4"))
        openTradesTable.setItem(0, 4, QTableWidgetItem("138.2"))
        openTradesTable.setItem(0, 5, QTableWidgetItem("MegaMacd#12"))
        openTradesTable.setItem(0, 6, QTableWidgetItem("21"))
        openTradesTable.setItem(0, 7, QTableWidgetItem("136.7"))

        leftFrameLayout.addWidget(openTradesTable)

        # Create the right layout
        rightLayout = QVBoxLayout()
        mainLiveLayout.addLayout(rightLayout)
