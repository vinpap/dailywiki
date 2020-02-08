from abc import ABC, abstractmethod

class SettingsWriterInterface(ABC):
    
    @abstractmethod
    def saveSettings(self, settings):

        pass
    
