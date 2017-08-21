# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:18:07 2016

@author: Proto

Wordnip Object

This is a demonstration for python beginners how the general nature of modules 
and object oriented programming.

This library contains functions for manipulating large lists of words. To use:
    - Create a new instance of Wordnip with a list() of words
    - Or you can use a file object:

    with open('../text/sowpods.txt') as words:
        w = Wordnip(words.read().split('\n'))
        print(w.get_letter('Z'))
"""


class Wordnip(object):
    def __init__(self, words):
        self.words = words
        
    def get_letter(self, letter):
        return [w for w in self.words if w.startswith(letter)]
    
    def anagrams(self, word):
        return [w for w in self.words if ''.join(sorted(w)) == ''.join(sorted(word))]
    
    def word_count(self):
        return len(self.wwords)
        
    def letter_count(self, word):
        return len(word)

    def find_adverbs_with(self, letter):
        return [w for w in self.words if w.startswith(letter) and w.endswith('ly')]
    
    def paginate(self):
        i = iter(self.words)
        counter = 0
        for n in range(10):
            counter = n
            next(i)
