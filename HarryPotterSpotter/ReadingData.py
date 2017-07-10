import pandas as pd
import re
"""Word processing Zone"""
with open('HP1.txt') as FirstBook:
    booktext = (FirstBook.read()
                .replace('\n', '')
                .replace(',', ' ')
                .replace('.', ' SPLIT')
                .replace('s ', ' ')
                .replace('es ', ' ')
                .replace('ing ', ' ')
                .replace('-', ' ')
                .replace('—', ' '))
    booktext = re.sub('\d+', 'NUMBER', booktext)
    booktext = booktext.replace('Page | NUMBER Harry Potter and the Philosopher Stone   J SPLITK SPLIT Rowl', '')
print(booktext)

"""Get Data Zone"""
Sentences = booktext.replace('!', ' SPLIT').replace('?', ' SPLIT').split('SPLIT')
SentencesDF = pd.DataFrame(Sentences)
SentencesDF.columns = ['Sentences']
SentencesDF = SentencesDF[SentencesDF['Sentences'].str.split(' ').map(len) > 6].reset_index().drop('index', axis = 1)

print(SentencesDF.iloc[8].values)
print(SentencesDF)