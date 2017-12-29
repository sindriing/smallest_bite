import pandas as pd 
import numpy as np 
import re


def get_n_most_common_words(count):
    words = (pd.read_csv('word_counts.csv', encoding = "ISO-8859-1")
             .sort_values('Count', ascending=False).iloc[:count])
    return words

def simplify_text(sentence):
	text = (re.sub('\d+', 'NUMBER', sentence)
			    .lower()
			    .replace('\n', '')
			    .replace('mr.', 'mr')
			    .replace('ms.', 'ms')
			    .replace(',', ' ')
			    .replace('s ', ' ')
			    .replace('es ', ' ')
			    .replace('-', ' ')
			    .replace('—', ' ')
			    .replace('“', '')
			    .replace('”', '')
			    .replace('"', '')
			    .replace('   ', ' ')
			    .replace('  ', ' ')
			    .replace('’', '')
			    .replace('\'', '')
			    .replace('?', '')
			    .replace('.', '')
			    .replace('!', ''))
	return text

def translate_features(sentence):
	wordCount = 2000
	sentence = simplify_text(sentence)
	sentence = sentence.split()
	commonWords = get_n_most_common_words(wordCount)['Word'].reset_index().drop('index', axis=1)
	features = np.zeros((wordCount), dtype = 'int')
	for i, cword in enumerate(commonWords['Word']):
		features[i] = cword in sentence
	
	# for x in zip(features, list(commonWords['Word'])):
	# 	print(x)
	return features.reshape(1,-1)

