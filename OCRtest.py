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
print(words[:100])
import re
import string

print("Welcome")
print("This program will clean an OCR Text document.")

filename = input("Please input the filepath for the document you would like to clean: ")

file = open(filename, 'rt', encoding='utf-8')
text = file.read()
file.close()

#split words by whitespace
words = text.split()

#remove punctuation
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]

# convert to lower case
words = (str([word.lower() for word in words]))

#Create an empty list to fill with corrected text.
cleanText = []

#Remove all special characters.
removeSymbols = re.sub(r'[?|$|.|!]',r'',words)
keepTextOnly = re.sub(r'[^a-zA-Z0-9 ]',r'',removeSymbols)
cleanText.append(keepTextOnly)


print(cleanText) #Only printing this for now. Will need to eventually write cleanText to external source.

