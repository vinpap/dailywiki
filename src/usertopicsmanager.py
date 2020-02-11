import logging
import requests
import wikipedia

class UserTopicsManager:



    def __init__(self, settings):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
            fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.settings = settings

        self.max_topics_number = 10

    def insertNewTopic(self, topic):

        # =============================================================================
        #La valeur de retour est un dictionnaire à deux valeurs : RETURN ET DATA
        #Plusieurs réponses sont possibles :
        # - Tout va bien : on renvoie "OK" et un tableau vide
        # - Le sujet est déjà dans la liste "ALREADY EXISTS" et un tableau vide
        # - L'utilisateur a trop de sujets déjà définis : TOO MANY TOPICS" et un tableau vide
        # - Catégorie introuvable et aucun nom similaire : "NOT FOUND" et un tableau vide
        # - Connexion perdue : "NO CONNECTION" et un tableau vide
        # =============================================================================

        result = {"RETURN" : "",
                  "DATA" : []}

        if len(self.settings["TOPICS"]) >= self.max_topics_number:

            self.logger.debug("User tried to add a new topic, but the max number has already been reached")

            result["RETURN"] = "TOO MANY TOPICS"

            return result

        if topic in self.settings["TOPICS"]:

            self.logger.debug("User tried to add a new topic, but it is already in the list")
            result["RETURN"] = "ALREADY EXISTS"

            return result


        self.logger.debug("Looking for " + "Category:" + str(topic))

        return self.searchTopic(topic)

    def deleteTopic(self, topic):

        self.settings["TOPICS"].remove(topic)

    def searchTopic(self, topic):


        try:

            wikipedia.page("Category:" + str(topic))

        except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):

            self.logger.debug("Category:" + str(topic) + " not found")
            return {"RETURN" : "NOT FOUND",
                    "DATA" : []}

        except requests.exceptions.ConnectionError:

            self.logger.debug("Category:" + str(topic) + " not found: connection lost")
            return {"RETURN" : "NO CONNECTION",
                    "DATA" : []}


        return {"RETURN" : "OK",
                    "DATA" : []}
        