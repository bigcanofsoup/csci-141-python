import datetime
import pandas as pd
import random
import numpy as np

class Forum_Page:

    def __init__(self, name):
        self.__name = name
        self.__board = pd.DataFrame(columns = ['Title','Date', 'Author', 'Post', 'Votes'])
        self.__board.set_index('Title', inplace = True)
        self.__board['Votes'] = self.__board['Votes'].astype('int')
        self.__anon_words = self.__process('words.txt')
        
    
    def __process(self, filename):
        with open(filename,'r', encoding = 'UTF8') as file:
           result = [line.rstrip() for line in file]
        return result
        
    def __exists(self, title):
        return title in self.__board.index
    
    def checker(self):
        return self.__board.copy()
    
    def __generate_anon(self):
        pass
        
    def add_post(self, title, post, author = None):
        pass
    
    def delete_post(self, title):
        pass
    
    def vote_post(self, title, up = True):
        pass  
        
    def top_voted(self):
        pass
        
    def get_titles(self):
        pass
        
    def get_post_info(self, title):
        pass
    
    def get_name(self):
        return self.__name
        
    def __str__(self):
        pass