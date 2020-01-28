from abc import ABC, abstractmethod

class ArticleSelectorInterface(ABC):
    
    @abstractmethod
    def getDailyArticleTitle(self):

        pass
    
    @abstractmethod
    def accessDailyArticle(self):
        
        pass