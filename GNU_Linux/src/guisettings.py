from guisettingsinterface import GuiSettingsInterface
from settingsdialogwindow import SettingsDialogWindow

from PyQt5.QtWidgets import QApplication
import logging

class GuiSettings(GuiSettingsInterface):
    
    def __init__(self, settings_reader, settings_writer):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
                                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        self.app = QApplication.instance()
        
        self.settings_dialog = SettingsDialogWindow(settings_reader, settings_writer)
        
    
    def displaySettings(self):
        
        self.logger.debug("displaySettings called")
        self.settings_dialog.show()
        # Afficher la fenêtre de dialogue
        
        