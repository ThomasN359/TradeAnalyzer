import math
import sys
import TradeGUI  # Displays as unused, but you need this to run the program
from PyQt5.QtWidgets import QApplication
from Data_Collection import DataCollection
from AI_Script_Generation import AI_Script_Generation
from List_Creation import List_Creation
from Live_Trading import Live_Trading
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


# This is the first window although due to tabbing this function incorporates functionality for some other windows
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindowLabel = None
        self.tabs = QtWidgets.QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Implements the main window which is the default upon start up
        self.mainWindowTab = QtWidgets.QWidget()
        self.mainWindowLayout = QtWidgets.QVBoxLayout(self.mainWindowTab)

        # There are two color sliders for visual customizations and their code is here
        self.backgroundColor = None
        self.widgetColor = None
        self.backgroundColorSlider = QtWidgets.QSlider(Qt.Horizontal)
        self.backgroundColorSlider.setRange(0, 255)
        self.backgroundColorSlider.setValue(255)
        self.backgroundColorSlider.setMaximumHeight(20)
        self.widgetColorSlider2 = QtWidgets.QSlider(Qt.Horizontal)
        self.widgetColorSlider2.setRange(0, 255)
        self.widgetColorSlider2.setValue(255)
        self.widgetColorSlider2.setMaximumHeight(20)
        self.setGeometry(500, 500, 1000, 450)
        self.setWindowTitle("Main Window")
        self.init_ui()

        # The other windows are QFrames which are widgets with benefits, and they are initialized once and here.
        self.data_collectionFrame = DataCollection(self.backgroundColor)
        self.AI_Script_GenerationFrame = AI_Script_Generation(self.backgroundColor)
        self.Live_TradingFrame = Live_Trading(self.backgroundColor)
        self.List_CreationFrame = List_Creation(self.backgroundColor)

        # These are the tabs on the top of the window that you can use to navigate through the app
        self.tabs.addTab(self.mainWindowTab, "Main Window")
        self.tabs.addTab(self.data_collectionFrame, "Data Collection")
        self.tabs.addTab(self.AI_Script_GenerationFrame, "AI Script Generation")
        self.tabs.addTab(self.Live_TradingFrame, "Live Trading")
        self.tabs.addTab(self.List_CreationFrame, "List Creation")

        # The default tab is set here
        self.tabs.setCurrentIndex(0)
        self.tabs.currentChanged.connect(self.openTabWindow)

    # Although this is extra, this is the function responsible for changing color when sliders move using cosine math
    def updateBackgroundColor(self, val, colorType):
        colorVal = val / 255
        amp = 0.5
        # The 242 value is just the default gui value
        if val == 255:
            red = green = blue = 242
        elif val == 0:
            red = green = blue = 0
        else:
            # This is so that we can use one value to represent many numbers rather than 3 sliders
            red = (amp + (amp * math.cos(2 * math.pi * colorVal))) * 255
            green = (amp + (amp * math.cos(2 * math.pi * colorVal + 2 * math.pi / 3))) * 255
            blue = (amp + (amp * math.cos(2 * math.pi * colorVal + 4 * math.pi / 3))) * 255
        color = "rgb({}, {}, {})".format(red, green, blue)
        if colorType == "background":
            self.setStyleSheet("background-color: {}".format(color))
        elif colorType == "widget":
            self.setStyleSheet("color: {}".format(color))

    # This is where all the other frames are added and the Main Window is designed
    def init_ui(self):
        # Below this comment is the mainframe design 
        self.mainWindowLabel = QtWidgets.QLabel("Welcome to Data Trader", self)
        self.mainWindowLabel.setAlignment(Qt.AlignCenter)
        font = self.mainWindowLabel.font()
        font.setPointSize(20)
        self.mainWindowLabel.setFont(font)
        self.mainWindowLayout.addWidget(self.mainWindowLabel)
        self.backgroundColorSlider.valueChanged.connect(
            lambda value: self.updateBackgroundColor(value, "background"))
        self.widgetColorSlider2.valueChanged.connect(lambda value: self.updateBackgroundColor(value, "widget"))
        self.mainWindowLayout.addWidget(self.backgroundColorSlider)
        self.mainWindowLayout.addWidget(self.widgetColorSlider2)

        # The other frames are implemented here 
        self.data_collectionFrame = DataCollection(self.backgroundColor)
        self.AI_Script_GenerationFrame = AI_Script_Generation(self.backgroundColor)
        self.Live_TradingFrame = Live_Trading(self.backgroundColor)
        self.List_CreationFrame = List_Creation(self.backgroundColor)

        # Adding hotkeys would be done like this, then you connect it to functionality
        # self.tab_shortcut = QShortcut(QKeySequence("Ctrl+Tab"), self)

    # This function is what allows you to switch tabs when clicked, currently it resizes windows here not in the classes
    def openTabWindow(self, index):
        self.data_collectionFrame.setVisible(False)
        self.AI_Script_GenerationFrame.setVisible(False)
        self.Live_TradingFrame.setVisible(False)
        self.List_CreationFrame.setVisible(False)

        # Each number corresponds to an index, maybe make this enums later
        if index == 0:
            self.mainWindowTab.setVisible(True)
            self.resize(1000, 450)
        elif index == 1:
            self.data_collectionFrame.setVisible(True)
            self.resize(1320, 400)
        elif index == 2:
            self.AI_Script_GenerationFrame.setVisible(True)
            self.resize(800, 700)
        elif index == 3:
            self.Live_TradingFrame.setVisible(True)
            self.resize(1173, 800)
        elif index == 4:
            self.List_CreationFrame.setVisible(True)
            self.resize(800, 700)


# Main function is here, this is what is called when you click run. 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
