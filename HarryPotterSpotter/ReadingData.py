import pandas as pd
import re
from collections import Counter

"""reads a book from a txt file into a string and simplifies the text"""
def read_book(book):
    with open(book) as TheBook:
        original = TheBook.read()
        booktext = re.sub(r'Page |.+Rowling','',original)
        booktext = (re.sub('\d+', 'NUMBER', booktext)
                    #.replace('J.K. Rowling', '')
                    #.replace('Page | NUMBER Harry Potter and the Philosophers Stone', '' )
                    .lower()
                    .replace('\n', '')
                    .replace('mr.', 'mr')
                    .replace('ms.', 'ms')
                    .replace(',', ' ')
                    .replace('.', ' SPLIT')
                    .replace('s ', ' ')
                    .replace('es ', ' ')
                    #.replace('ing ', ' ')
                    .replace('-', ' ')
                    .replace('—', ' ')
                    .replace('“', '')
                    .replace('”', '')
                    .replace('"', '')
                    .replace('   ', ' ')
                    .replace('  ', ' ')
                    .replace('’', ''))
        return (booktext)

"""Takes the string text of a book and splits it into sentences longer than 5 words and returns them in a DataFrame"""
def create_sentences(booktext, title):
    Sentences = booktext.replace('!', ' SPLIT').replace('?', ' SPLIT').split('SPLIT')
    SentencesDF = pd.DataFrame(Sentences)
    SentencesDF.columns = ['Sentences']
    SentencesDF = SentencesDF[SentencesDF['Sentences'].str.split(' ').map(len) > 6].reset_index().drop('index', axis=1)
    SentencesDF['Title'] = title.split('.')[0]
    return SentencesDF

def is_harry_potter(df):
    df['Harry Potter'] = df['Title'].str.slice(0, 2) == 'HP'
    return df

def get_most_common_words_list(text):
    words = text.replace('?', '').replace('!', '').replace('SPLIT', '').split()
    wordCount = Counter(words)
    return wordCount

textFiles = ('HP1.txt', 'HP2.txt', 'Dracula.txt')
df = pd.DataFrame(columns = ['Sentences', 'Title'])
totaltext = ''
for book in textFiles:
    booktext = read_book(book)
    totaltext += booktext
    tempdf = create_sentences(booktext, book)
    df = df.append(tempdf)
hpDF = is_harry_potter(df)
hpDF.to_csv('HP_Dataframe.csv')

wordcount = get_most_common_words_list(totaltext)
wordcount = pd.DataFrame(list(wordcount.items()), columns=['Word', 'Count']).set_index('Word')
wordcount = wordcount[wordcount.values > 4]
wordcount.to_csv('word_counts.csv')
#print(wordcount)
#print(df)