from gui import Gui
import logging
import random
import os
import urllib
import sys
import time

from articleselector import ArticleSelector

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), 
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

logger = logging.getLogger(__name__)


def checkNetworkStatus():
    
    while True:
        
        try:
            
            urllib.request.urlopen('http://google.com')
            return True
        
        except urllib.error.URLError as err: 
            
            time.sleep(120)
    
    logger.info("Unable to reach Wikipedia, please check your Internet connection")
    return False



if not checkNetworkStatus():
    
    sys.exit()

random.seed()

article_selector = ArticleSelector()
app = Gui(article_selector)


app.run()


