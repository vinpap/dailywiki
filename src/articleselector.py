from articleselectorinterface import ArticleSelectorInterface
import logging
import random
import webbrowser
import wikipedia
import requests
import time

class ArticleSelector(ArticleSelectorInterface):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('../logs/' + __name__ + '.log',
                                maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
                                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        wikipedia.set_lang("en")
    
    def getDailyArticleTitle(self):
        
        
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
    
    def accessDailyArticle(self):

            
        webbrowser.open_new_tab(self.article.url)
