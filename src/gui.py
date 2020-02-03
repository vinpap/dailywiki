import logging
import logging.handlers
import sys
import random
import platform
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QSystemTrayIcon, QMenu, QAction, QDialog, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon

from articleselectorinterface import ArticleSelectorInterface
from guisettingsinterface import GuiSettingsInterface



class GuiCore():

    "Infrastructure layer class that manages the graphical user interface"


    def __init__(self, daily_article_selector):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('../logs/' + __name__ + '.log',
                                maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
                                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        self.logger.debug("Loading GUI")

        self.app = QApplication(sys.argv)


        os_name = platform.system()
        self.logger.info("Platform: " + os_name)
        
        self.article_selector = daily_article_selector
        self.article_title = self.article_selector.getDailyArticleTitle()


        if QSystemTrayIcon.isSystemTrayAvailable() and os_name == "Windows":
            
            self.setSystemTrayGUI()
            
        else:
            
            self.setAlternativeGUI()
    
    def setSettingsGui(self, settings_gui):
        
        self.settings_gui = settings_gui
    
    def setSystemTrayGUI(self):
        
        self.app.setQuitOnLastWindowClosed(False)
        self.icon = QIcon("resources/icon_white.png")

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setToolTip("WikiDaily")
        self.tray.setVisible(True)

        self.menu = QMenu()
        self.action = QAction("Exit")
        self.menu.addAction(self.action)

        self.tray.setContextMenu(self.menu)
    
    def setAlternativeGUI(self):
        
        self.window = QDialog()
        self.window.setModal(True)
        self.icon = QIcon("resources/wikipedia_icon.png")
        self.window.setWindowIcon(self.icon)
        self.window.setWindowTitle("Today's article")
        self.window.resize(350, 140)

        self.read_btn = QPushButton("Read", self.window)
        self.settings_btn = QPushButton("Settings", self.window)
        
        self.dialog_msg = QLabel(self.window)
        
        random_nbr = random.randint(0, 1)
        
        if random_nbr == 0 :
            
            self.dialog_msg.setText("<b><big>Your daily article is ready. Today you're going to learn about "
                                + self.article_title + "!</big></b>")
        else :
            
            self.dialog_msg.setText("<b><big>Do you feel like learning about " + 
                                    self.article_title + " today? We have just the thing for you!</big></b>")


        self.dialog_msg.setAlignment(Qt.AlignCenter)
        self.dialog_msg.setTextFormat(Qt.RichText)
        self.layout = QGridLayout(self.window)
        self.layout.setSpacing(5)
            
        self.layout.addWidget(self.dialog_msg, 0, 0, 1, 7)
        self.layout.addWidget(self.read_btn, 1, 1, 1, 2)
        self.layout.addWidget(self.settings_btn, 1, 4, 1, 2)
        
        #Paramétrer les events pour les deux boutons
        self.read_btn.clicked.connect(self.accessArticle)
        self.settings_btn.clicked.connect(self.openSettings)
        
        self.window.setLayout(self.layout)
        self.window.show()

    def accessArticle(self):
        
        self.logger.debug("Accessing article...")
        
        
        try:
            
            self.article_selector.accessDailyArticle()
            self.app.quit()
        
        except requests.exceptions.ConnectionError:
            
            self.dialog_msg.setText("It looks like the connection has been interrupted... Try again later!")
    
    def openSettings(self):
        
        self.logger.debug("Opening settings...")
        self.settings_gui.displaySettings()

    def run(self):

        "Main loop function"

        self.logger.debug("Entering main execution loop")

        sys.exit(self.app.exec_())
