import unittest
from models import source,artilce
Source = source.Source
Article = article.Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("crypto-coins-news","Crypto Coins News","Providing breaking cryptocurrency news - focusing on Bitcoin, Ethereum, ICOs, blockchain technology, and smart contracts.", "https://www.ccn.com","technology","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article(null,"Macrumors.com","Joe Rossignol","Apple Recently Visited With Taiwanese Makers of Thinner and Brighter MicroLED and MiniLED Displays","Apple representatives attended the Touch Taiwan display industry convention"," "https://www.macrumors.com/2018/08/30/apple-meets-taiwanese-microled-makers",https://cdn.macrumors.com/article-new/2017/09/iphone-x-display.jpg?retina","2018-08-30T13:13:34Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))






if __name__ == '__main__':
    unittest.main()