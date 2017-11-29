#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:58:39 2017

@author: margaretwaligora,nicolemorse, amandagantchev

@purpose: The purpose of this program is to load, read and remove white space,
special and encoded characters and punctuation from a sample OCR text. 

@class: LIS 8410 Introduction to Info Management-Python

@professor: bowman

@univ: Wayne State

@sources: 

"""

# load text
filename = '/Users/margaretwaligora/Desktop/LIS7492FinalDataSet/Steinem_IWasAPlayBoyBunny.txt'
file = open(filename, 'rt', encoding='utf-8')
text = file.read()
file.close()

#split words by whitespace
words = text.split()

#remove punctuation
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]

# convert to lower case
words = [word.lower() for word in words]

print(words[:100])
