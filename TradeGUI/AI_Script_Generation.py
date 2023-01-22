import os
from PyQt5.QtWidgets import QLabel, QComboBox, QPushButton, QCheckBox, QLineEdit, QVBoxLayout, QHBoxLayout,  \
    QGridLayout, QTextEdit, QFrame


# This window is where you train an AI algorithm with a base trading strategy and a training set for data collection
class AI_Script_Generation(QFrame):
    def __init__(self, color):
        super().__init__()
        self.setGeometry(800, 700, 800, 700)
        self.setWindowTitle("AI Script Generation")
        self.setStyleSheet("QFrame {{ background-color: {} }}".format(color))
        self.init_ui()

    # Functionality for AI Script Generator Window goes below here
    def init_ui(self):
        # The functionality for this GUI is performed below this line of code
        scriptGenerationLayout = QVBoxLayout()
        self.setLayout(scriptGenerationLayout)

        # Get file names from directory for the Train List drop down
        directory = os.getcwd() + "\AssetList\TrainList"
        try:
            fileNames = os.listdir(directory)
        except OSError as e:
            print("Could not find the TrainList Directory", e)
            fileNames = []

        # Instantiates the dropdown box for selecting a training list
        trainingSetListLabel = QLabel("Select Training List", self)
        trainingSetList = QComboBox()

        # All training list values are placed below here
        for file in fileNames:
            trainingSetList.addItem(file)

        trainingSetListLayout = QHBoxLayout()
        trainingSetListLayout.addWidget(trainingSetListLabel)
        trainingSetListLayout.addWidget(trainingSetList)
        scriptGenerationLayout.addLayout(trainingSetListLayout)

        # Implements a 3x3 grid to place the 9 timeframe options and you select all that you want.
        selectTimeFrameLabel = QLabel("Select Time Frame", self)
        timeFrame1m = QCheckBox("1m", self)
        timeFrame3m = QCheckBox("3m", self)
        timeFrame5m = QCheckBox("5m", self)
        timeFrame15m = QCheckBox("15m", self)
        timeFrame30m = QCheckBox("30m", self)
        timeFrame45m = QCheckBox("45m", self)
        timeFrame1h = QCheckBox("1h", self)
        timeFrame2h = QCheckBox("2h", self)
        timeFrame4h = QCheckBox("4h", self)

        # Shove the select all options onto the layout
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
        scriptGenerationLayout.addLayout(selectTimeFrameLayout)

        # Gain access to the Pinescript directory folder to view it's content in a drop down
        directory = os.getcwd() + "\Pinescript"
        try:
            fileNames = os.listdir(directory)
        except OSError as e:
            print("Could not find Pinescript Directory", e)
            fileNames = []

        # Drop down menu for selecting the root strategy (these are the original Pinescript codes)
        rootStrategyLabel = QLabel("Select A Root Strategy", self)
        rootStrategyDropdown = QComboBox()

        # Display the file names off everything in the Pinescript directory.
        for file in fileNames:
            rootStrategyDropdown.addItem(file)

        # Layout organization for dropdown
        rootStrategyLayout = QHBoxLayout()
        rootStrategyLayout.addWidget(rootStrategyLabel)
        rootStrategyLayout.addWidget(rootStrategyDropdown)
        scriptGenerationLayout.addLayout(rootStrategyLayout)

        # "Train Type" label and dropdown
        trainTypeLabel = QLabel("Train Type", self)
        trainTypeDropdown = QComboBox()
        trainTypeDropdown.addItem("Option 1")
        trainTypeDropdown.addItem("Option 2")
        trainTypeDropdown.addItem("Option 3")
        trainTypeLayout = QHBoxLayout()
        trainTypeLayout.addWidget(trainTypeLabel)
        trainTypeLayout.addWidget(trainTypeDropdown)
        scriptGenerationLayout.addLayout(trainTypeLayout)

        # Make the name label and textbox so that you can name your scripts, this will write to ComputerGeneratedScripts
        nameLabel = QLabel("Name", self)
        nameTextbox = QLineEdit(self)
        nameLayout = QHBoxLayout()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameTextbox)
        scriptGenerationLayout.addLayout(nameLayout)

        # Simple button that generates it to the folder
        applyButton = QPushButton("Apply", self)
        scriptGenerationLayout.addWidget(applyButton)

        # This displays a quick data collection like summary to give a brief overview of how successful the script was
        summaryStatsLabel = QLabel("Summary Statistics", self)
        summaryStatsTextbox = QTextEdit(self)
        summaryStatsLayout = QVBoxLayout()
        summaryStatsLayout.addWidget(summaryStatsLabel)
        summaryStatsLayout.addWidget(summaryStatsTextbox)
        scriptGenerationLayout.addLayout(summaryStatsLayout)

        # When you make a bad script you should have the option to delete it
        deleteScriptLabel = QLabel("Delete a Script", self)
        deleteScriptDropdown = QComboBox()
        deleteScriptDropdown.addItem("TBD")
        deleteScriptDropdown.addItem("TBD")
        deleteScriptDropdown.addItem("TBD")
        deleteScriptLayout = QHBoxLayout()
        deleteScriptLayout.addWidget(deleteScriptLabel)
        deleteScriptLayout.addWidget(deleteScriptDropdown)
        scriptGenerationLayout.addLayout(deleteScriptLayout)

        # This apply button is for deleting scripts
        deleteApplyButton = QPushButton("Apply", self)
        scriptGenerationLayout.addWidget(deleteApplyButton)