from abc import ABC, abstractmethod

class SettingsReaderInterface(ABC):

    @abstractmethod
    def readSettings(self):

        pass
    