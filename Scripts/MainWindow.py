import sys
import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import spammer as sp

App = QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setGeometry(100, 50, 500, 250)
MainWindow.setWindowTitle("Spammer")

# Variales
MainWindowShowRun = 0
FirstSection = 0
SecondSection = 0

Help0 = "1. First choose you want to spam the default list or a custom message. "
Help1 = "2. Now choose you want to spam from WhatsApp or Messenger."
Help2 = "3. Now press the \"Start Spam\" button. "
Help3 = "4. Now you have 10 seconds to open the window where you have opened WhatsApp or any"
Help3P2 = " messenger and open the contact's chat window and select the chat bar. "
Help4 = "5. After 10 seconds the spam will start automatically. "
Help5 = "6. If you want to stop spamming anytime you can press \"/\" and the spam will stop."
Note1 = "Note: When you start the spam the program may go \"not responding\" but don't worry,"
Note1P2 = "everything is alright. Continue as normal."

# Functions
#   Main Window Customization
def MainWindowShow():
    MainWindowShowRun = 0
    global DefaultSpamButton
    DefaultSpamButton = QPushButton("Default Spam", MainWindow)
    DefaultSpamButton.setGeometry(10, 5, 220, 35)
    DefaultSpamButton.show()
    DefaultSpamButton.clicked.connect(DefaultSpamButtonClicked)

    global CustomSpamButton
    CustomSpamButton = QPushButton("Custom Spam", MainWindow)
    CustomSpamButton.setGeometry(260, 5, 220, 35)
    CustomSpamButton.show()
    CustomSpamButton.clicked.connect(CustomSpamButtonClicked)

    global WhatsAppSpamButton
    WhatsAppSpamButton = QPushButton("WhatsApp Spam", MainWindow)
    WhatsAppSpamButton.setGeometry(10, 60, 220, 35)
    WhatsAppSpamButton.show()
    WhatsAppSpamButton.clicked.connect(WhatsAppSpamButtonClicked)

    global MessengerSpamButton
    MessengerSpamButton = QPushButton("Messenger Spam", MainWindow)
    MessengerSpamButton.setGeometry(260, 60, 220, 35)
    MessengerSpamButton.show()
    MessengerSpamButton.clicked.connect(MessengerSpamButtonClicked)

    global Help0Label
    Help0Label = QLabel(f"{Help0}", MainWindow)
    Help0Label.setGeometry(5, 100, 500, 25)
    Help0Label.show()
    global Help1Label
    Help1Label = QLabel(f"{Help1}", MainWindow)
    Help1Label.setGeometry(5, 115, 500, 25)
    Help1Label.show()
    global Help2Label
    Help2Label = QLabel(f"{Help2}", MainWindow)
    Help2Label.setGeometry(5, 130, 500, 25)
    Help2Label.show()
    global Help3Label
    Help3Label = QLabel(f"{Help3}", MainWindow)
    Help3Label.setGeometry(5, 145, 500, 25)
    Help3Label.show()
    global Help3P2Label
    Help3P2Label = QLabel(f"{Help3P2}", MainWindow)
    Help3P2Label.setGeometry(16, 160, 500, 25)
    Help3P2Label.show()
    global Help4Label
    Help4Label = QLabel(f"{Help4}", MainWindow)
    Help4Label.setGeometry(5, 175, 500, 25)
    Help4Label.show()
    global Help5Label
    Help5Label = QLabel(f"{Help5}", MainWindow)
    Help5Label.setGeometry(5, 190, 500, 25)
    Help5Label.show()
    global Note1Label
    Note1Label = QLabel(f"{Note1}", MainWindow)
    Note1Label.setGeometry(5, 205, 500, 25)
    Note1Label.show()
    global Note1P2Label
    Note1P2Label = QLabel(f"{Note1P2}", MainWindow)
    Note1P2Label.setGeometry(5, 220, 500, 25)
    Note1P2Label.show()

#   smallFunctions
def DefaultSpamButtonClicked():
    FirstSectionHide()
    global FirstSection
    FirstSection = 1

def CustomSpamButtonClicked():
    FirstSectionHide()
    global FirstSection
    FirstSection = 2

def WhatsAppSpamButtonClicked():
    if FirstSection == 1 or FirstSection == 2:
        SecondSectionHide()
        global SecondSection
        SecondSection = 1
        DefaultOrCustomButtonClicked()

    elif FirstSection == 0:
        FirstSectionError()

def MessengerSpamButtonClicked():
    if FirstSection == 1 or FirstSection == 2:
        SecondSectionHide()
        global SecondSection
        SecondSection = 2
        DefaultOrCustomButtonClicked()

    elif FirstSection == 0:
        FirstSectionError()

def FirstSectionHide():
    DefaultSpamButton.setVisible(False)
    CustomSpamButton.setVisible(False)

def SecondSectionHide():
    WhatsAppSpamButton.setVisible(False)
    MessengerSpamButton.setVisible(False)
    Help0Label.setVisible(False)
    Help1Label.setVisible(False)
    Help2Label.setVisible(False)
    Help3Label.setVisible(False)
    Help3P2Label.setVisible(False)
    Help4Label.setVisible(False)
    Help5Label.setVisible(False)
    Note1Label.setVisible(False)
    Note1P2Label.setVisible(False)

def ShowStartSpamButton():
    global StartSpamButton
    StartSpamButton = QPushButton("Start Spamming", MainWindow)
    StartSpamButton.setGeometry(190, 220, 100, 30)
    StartSpamButton.show()
    StartSpamButton.clicked.connect(StartSpamButtonClicked)

def ShowBackButton():
    global BackButton
    BackButton = QPushButton("Back", MainWindow)
    BackButton.setGeometry(5, 220, 100, 30)
    BackButton.show()
    BackButton.clicked.connect(BackButtonClicked)

def ShowHelpsAndNotes():
    Help0Label.setGeometry(5, 50, 500, 25)
    Help1Label.setGeometry(5, 65, 500, 25)
    Help2Label.setGeometry(5, 80, 500, 25)
    Help3Label.setGeometry(5, 95, 500, 25)
    Help3P2Label.setGeometry(16, 110, 500, 25)
    Help4Label.setGeometry(5, 125, 500, 25)
    Help5Label.setGeometry(5, 140, 500, 25)
    Note1Label.setGeometry(5, 155, 500, 25)
    Note1P2Label.setGeometry(5, 170, 500, 25)
    Help0Label.setVisible(True)
    Help1Label.setVisible(True)
    Help2Label.setVisible(True)
    Help3Label.setVisible(True)
    Help3P2Label.setVisible(True)
    Help4Label.setVisible(True)
    Help5Label.setVisible(True)
    Note1Label.setVisible(True)
    Note1P2Label.setVisible(True)

def StartSpamButtonClicked():
    if FirstSection == 2:
        CustomSpamTextBoxValue = CustomSpamTextBox.text()
        thread = threading.Thread(target=sp.startSpamCustom,args=(SecondSection, CustomSpamTextBoxValue))
        thread.start()
    
    elif FirstSection == 1:
        thread = threading.Thread(target=sp.startSpamDefault,args=(SecondSection,))
        thread.start()

def BackButtonClicked():
    try:
        CustomSpamTextBox.setVisible(False)
    except:
        pass

    StartSpamButton.setVisible(False)
    BackButton.setVisible(False)
    Help0Label.setVisible(False)
    Help1Label.setVisible(False)
    Help2Label.setVisible(False)
    Help3Label.setVisible(False)
    Help3P2Label.setVisible(False)
    Help4Label.setVisible(False)
    Help5Label.setVisible(False)
    Note1Label.setVisible(False)
    Note1P2Label.setVisible(False)
    MainWindowShow()

def FirstSectionError():
    Error = QMessageBox()
    Error.setIcon(QMessageBox.Critical)
    Error.setText("Please choose something from first section before selecting from this section.")
    Error.setWindowTitle("Error")
    Error.exec_()
    MainWindowShowRun = 1

def DefaultOrCustomButtonClicked():
    if FirstSection == 1:
        ShowStartSpamButton()
        ShowBackButton()
        ShowHelpsAndNotes()

    elif FirstSection == 2:
        CustomSpammingWordWindow()

#   otherWindows
def CustomSpammingWordWindow():
    global CustomSpamTextBox
    CustomSpamTextBox = QLineEdit(MainWindow)
    CustomSpamTextBox.setGeometry(10, 20, 480, 25)
    CustomSpamTextBox.show()
    
    ShowStartSpamButton()
    ShowBackButton()
    ShowHelpsAndNotes()

# Other Crucial Data
while MainWindowShowRun == 1:
    MainWindowShow()

MainWindowShow()
MainWindow.show()
sys.exit(App.exec_())