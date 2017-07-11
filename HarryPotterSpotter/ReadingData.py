import pandas as pd
import re

"""reads a book from a txt file into a string and simplifies the text"""
def read_book(book):
    with open(book) as TheBook:
        booktext = (TheBook.read()
                    .replace('\n', '')
                    .replace(',', ' ')
                    .replace('.', ' SPLIT')
                    .replace('s ', ' ')
                    .replace('es ', ' ')
                    .replace('ing ', ' ')
                    .replace('-', ' ')
                    .replace('—', ' ')
                    .replace('“', '')
                    .replace('”', '')
                    .replace('"', '')
                    .replace('   ', ' ')
                    .replace('  ', ' '))
        booktext = re.sub('\d+', 'NUMBER', booktext)
        booktext = booktext.replace('Page | NUMBER Harry Potter and the Philosopher Stone J SPLITK SPLIT Rowl', '')
        return booktext

"""Takes the string text of a book and splits it into sentences longer than 5 words and returns them in a DataFrame"""
def create_sentences(booktext, title):
    Sentences = booktext.replace('!', ' SPLIT').replace('?', ' SPLIT').split('SPLIT')
    SentencesDF = pd.DataFrame(Sentences)
    SentencesDF.columns = ['Sentences']
    SentencesDF = SentencesDF[SentencesDF['Sentences'].str.split(' ').map(len) > 6].reset_index().drop('index', axis=1)
    SentencesDF['Title'] = title.split('.')[0]
    return SentencesDF

textFiles = ('HP1.txt', 'Dracula.txt')
df = pd.DataFrame(columns = ['Sentences', 'Title'])
for book in textFiles:
    booktext = read_book(book)
    tempdf = create_sentences(booktext, book)
    df = df.append(tempdf)
print(df)