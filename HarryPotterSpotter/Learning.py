import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split_into_words(df):
    word_df = df['Sentences'].apply(str.split)
    return word_df

def get_n_most_common_words(count):
    words = (pd.read_csv('word_counts.csv', encoding = "ISO-8859-1")
             .sort_values('Count', ascending=False).iloc[:count])
    return words

def get_data():
    df = pd.read_csv('HP_Dataframe.csv', index_col='Unnamed: 0', encoding = "ISO-8859-1")
    #X = df['Sentences']
    #y = df['Harry Potter']
    #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    return df

def get_features(wordCount):
    df = get_data()
    word_df = split_into_words(df)

    commonWords = get_n_most_common_words(wordCount)['Word'].reset_index().drop('index', axis=1)
    features = np.zeros((len(word_df), wordCount))

    counter=0
    for wordlist in word_df:
        features[counter] = commonWords.isin(wordlist).values.transpose()[0]
        counter+=1

    return (features, df['Harry Potter'].values.astype(int).transpose(), commonWords)

X, y, wordDict = get_features(200)
print(X.shape)
print(y.shape)