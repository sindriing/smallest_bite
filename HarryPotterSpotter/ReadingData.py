import pandas as pd
import re
"""Word processing Zone"""
with open('HP1.txt') as FirstBook:
    booktext = FirstBook.read().replace('\n', '').replace('s ', ' ').replace('es ', ' ').replace('ing ', ' ')



"""Get Data Zone"""
Sentences = booktext.replace('!', '.').replace('?', '.').split('.')
SentencesDF = pd.DataFrame(Sentences)
SentencesDF.columns = ['Sentences']
SentencesDF = SentencesDF[SentencesDF['Sentences'].str.split(' ').map(len) > 6].reset_index().drop('index', axis = 1)

print(SentencesDF)