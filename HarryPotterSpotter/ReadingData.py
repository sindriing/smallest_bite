import pandas as pd
import re

with open('D:/Forritun/Sumar_ML/smallest_bite/HP1.txt') as FirstBook:
    booktext = FirstBook.read().replace('\n', '')

print(booktext)

