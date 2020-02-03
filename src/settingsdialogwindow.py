from PyQt5.QtWidgets import QDialog, QGridLayout, QButtonGroup, QCheckBox, QPushButton
import logging

class SettingsDialogWindow(QDialog):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('../logs/' + __name__ + '.log',
                                maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
                                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        super().__init__()
        self.setModal(True)
        self.setWindowTitle("Settings")
        self.resize(400, 150)
        
        self.topics_selection_boxes_group = QButtonGroup(self)
        
        self.random_article_box = QCheckBox(self)
        self.random_article_box.setText("Open a random article")
        self.select_topics_box = QCheckBox(self)
        self.select_topics_box.setText("Open an article about a selected topic")
        self.launch_at_startup_box = QCheckBox(self)
        self.launch_at_startup_box.setText("Launch DailyWiki at startup")
        # Cocher chacune des cases en fonction des paramètres enregistrés
        
        self.topics_selection_btn = QPushButton("Select topics", self)
        self.cancel_btn = QPushButton("Cancel", self)
        self.ok_btn = QPushButton("OK", self)
        
        self.topics_selection_boxes_group.addButton(self.random_article_box)
        self.topics_selection_boxes_group.addButton(self.select_topics_box)
        
        self.setLayout()
        self.setGuiEvents()
    
    def setLayout(self):
        
        self.layout = QGridLayout(self)
        self.layout.setSpacing(5)
        self.layout.addWidget(self.random_article_box, 0, 0, 1, 4)
        self.layout.addWidget(self.select_topics_box, 1, 0, 1, 3)
        self.layout.addWidget(self.topics_selection_btn, 1, 3, 1, 1)
        self.layout.addWidget(self.launch_at_startup_box, 2, 0, 1, 4)
        self.layout.addWidget(self.cancel_btn, 3, 1, 1, 1)
        self.layout.addWidget(self.ok_btn, 3, 2, 1, 1)
        
    def setGuiEvents(self):
        
        self.topics_selection_btn.clicked.connect(self.selectTopics)
        self.ok_btn.clicked.connect(self.validateSettings)
        self.cancel_btn.clicked.connect(self.reject)
    
    def selectTopics(self):
        
        #Afficher une fenêtre pour sélectionner les sujets
        pass
    
    def validateSettings(self):
        
        self.logger.debug("validateSettings called")
        # Enregistrer les nouveaux paramètres
        self.accept()

    
        
        
        