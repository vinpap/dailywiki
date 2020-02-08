from settingsstorageinterface import SettingsStorageInterface
from configparser import ConfigParser

import logging
import os.path

class SettingsStorage(SettingsStorageInterface):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
                                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.config = ConfigParser()
        self.readConfigFile()
        
    
    def getSettings(self):
        
        self.readConfigFile()
        return_dict = {}
        
        if self.config["GENERAL"]["RANDOM"] == "True":
            
            return_dict["RANDOM"] = True
        
        else:
        
            return_dict["RANDOM"] = False
        
        if self.config["GENERAL"]["AUTOLAUNCH"] == "True":
            
            return_dict["AUTOLAUNCH"] = True
        
        else:
        
            return_dict["AUTOLAUNCH"] = False
        
        return_dict["TOPICS"] = []
        
        if "TOPICS" in self.config:
            
            for i in self.config["TOPICS"]:
                
                return_dict["TOPICS"].append(self.config["TOPICS"][i])    
        
            
        return return_dict
    
    def saveSettings(self, settings):
        
        self.config["GENERAL"]["RANDOM"] = str(settings["RANDOM"])
        self.config["GENERAL"]["AUTOLAUNCH"] = str(settings["AUTOLAUNCH"])
        
        current_topics = self.config.options("TOPICS")
        new_topic_index = len(current_topics)
        
        
        for i in settings["TOPICS"]:
            
            if i not in self.config["TOPICS"].values():
                
        
                self.config["TOPICS"][str(new_topic_index)] = i
                new_topic_index += 1
        
        with open("conf/settings.ini", 'w') as configfile:
            
            self.config.write(configfile)
    
    def createDefaultConfigFile(self):
        
        self.config["GENERAL"] = {"RANDOM" : True,
                                  "AUTOLAUNCH" : True}
        
        self.config["TOPICS"] = {}
        
        with open("conf/settings.ini", 'w') as configfile:
            
            self.config.write(configfile)
            configfile.close()
    
    def readConfigFile(self):
        
        self.logger.debug("Reading configuration file")
        
        if os.path.isfile("conf/settings.ini"):
            
            self.config.read("conf/settings.ini")

            
            if ("GENERAL" in self.config and "RANDOM" in self.config["GENERAL"] and "AUTOLAUNCH" in self.config["GENERAL"] and 
            (self.config["GENERAL"]["RANDOM"] == "True" or self.config["GENERAL"]["RANDOM"] == "False") or
            (self.config["GENERAL"]["AUTOLAUNCH"] == "True" or self.config["GENERAL"]["AUTOLAUNCH"] == "False")) :
                
                return
            
            else:
                
                self.logger.warning("Some settings are missing, creating a default configuration file to use instead")
                self.config.remove_section("TOPICS")
                self.config.remove_section("GENERAL")
                os.remove("conf/settings.ini")
                self.createDefaultConfigFile()
                 
            
        
        else:
        
            self.logger.warning("Coud not find the configuration file, creating a default file instead")
            self.createDefaultConfigFile()

        
