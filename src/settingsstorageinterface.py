from abc import ABC, abstractmethod

class SettingsStorageInterface(ABC):
    
    @abstractmethod
    def getSettings(self):

        pass
    
    @abstractmethod
    def saveSettings(self, settings):
        
        pass
    
