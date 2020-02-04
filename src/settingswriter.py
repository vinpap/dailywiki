from settingswriterinterface import SettingsWriterInterface
from settingsstorageinterface import SettingsStorageInterface

class SettingsWriter(SettingsWriterInterface):
    
    def __init__(self, settings_storage):
        
        self.settings_storage = settings_storage
    
    def saveSettings(self, settings):
        
        if (not settings 
            or "RANDOM" not in settings 
            or "TOPICS" not in settings 
            or "AUTOLAUNCH" not in settings
            or not isinstance(settings["RANDOM"], bool)
            or not isinstance(settings["TOPICS"], list)
            or not isinstance(settings["AUTOLAUNCH"], bool)
            or (not settings["RANDOM"]) and (settings["TOPICS"] == [])) :
            
            self.logger.warning("The settings provided do not follow the right format. No changes made to the current settings")
            return False
            
        
        for i in settings["TOPICS"]:
            
            if not isinstance(i, str):
                
                self.logger.warning("The settings provided do not follow the right format. No changes made to the current settings")
                return False
        
        self.settings_storage.saveSettings(settings)