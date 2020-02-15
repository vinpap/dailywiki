from abc import ABC, abstractmethod

class GuiSettingsInterface(ABC):

    @abstractmethod
    def __init__(self):

        pass

    @abstractmethod
    def displaySettings(self):

        pass
    