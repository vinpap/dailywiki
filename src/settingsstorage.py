from settingsstorageinterface import SettingsStorageInterface

class SettingsStorage(SettingsStorageInterface):
    
    def __init__(self):
        
        pass
    
    def getSettings(self):
        
        return {"RANDOM" : True,
                "TOPICS" : ["Physics", "Space"],
                "AUTOLAUNCH" : True}
    
    def saveSettings(self, settings):
        
        pass