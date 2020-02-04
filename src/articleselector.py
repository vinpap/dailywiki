from articleselectorinterface import ArticleSelectorInterface
from settingsreaderinterface import SettingsReaderInterface
import logging
import random
import webbrowser
import wikipedia
import wikipediaapi
import requests
import time
import sys

class ArticleSelector(ArticleSelectorInterface):
    
    def __init__(self, settings_reader):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('../logs/' + __name__ + '.log',
                                maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
                                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        wikipedia.set_lang("en")
        self.wiki = wikipediaapi.Wikipedia('en')
        self.settings = settings_reader.readSettings()
        
        if not self.settings["RANDOM"]:
            
            self.topics = self.settings["TOPICS"]
        
        else :
            
            self.topics = False
        
        self.articles_pool = []
    
    def getDailyArticleTitle(self):
        
        if not self.topics :
            
            return self.getRandomArticle()
        
        return self.getRandomArticleInTopics()
        
    def getRandomArticle(self):
        
        keep_up = True
        tries = 0
        
        while keep_up and tries<5:
            
            try:
                
                title = wikipedia.random()
                self.article = wikipedia.page(title)
                keep_up = False
            
            except wikipedia.exceptions.PageError: 
                
                continue
            
            except requests.exceptions.ConnectionError:

                
                self.logger.debug("Unable to connect to Wikipedia. Nex try in 5 seconds")
                time.sleep(5)
                tries+=1
                continue
                
            except wikipedia.exceptions.DisambiguationError as error:
                    
                try:
                
                    rand_int = random.randint(0, len(error.options)-1)
                    self.article = wikipedia.page(error.options[rand_int])
                    keep_up = False
                    
                except:  
                    
                    continue
                
            if tries>=5:
                
                self.logger.error("Unable to connect to Wikipedia after 5 tries")
                sys.exit()
            
            return self.article.title
    
    def getRandomArticleInTopics(self):
        
        for i in self.topics :
            
            cat = self.wiki.page("Category:" + i)
            
            self.getCategoryMembers(cat.categorymembers)
        
        self.logger.debug("There are " + str(len(self.articles_pool)) + " articles in the pool")
        
        rand_int = random.randint(0, len(self.articles_pool)-1)
        self.article = wikipedia.page(self.articles_pool[rand_int])
        return self.article.title
                
    def getCategoryMembers(self, categorymembers, level=0, max_level=1):
        
        for c in categorymembers.values():
            
            if c.ns == wikipediaapi.Namespace.MAIN:
                
                self.articles_pool.append(c.title)
                
            elif c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                
                self.getCategoryMembers(c.categorymembers, level=level + 1, max_level=max_level)
    
    def accessDailyArticle(self):

            
        webbrowser.open_new_tab(self.article.url)
        
        
