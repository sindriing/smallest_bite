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

def get_features(fromPos, endPos):
    df = get_data()
    word_df = split_into_words(df)

    commonWords = get_n_most_common_words(200)['Word'].reset_index().drop('index', axis=1)
    features = pd.DataFrame()
    for wordlist in word_df.iloc[fromPos:endPos]:
        features = features.append(commonWords.isin(wordlist).transpose(), ignore_index=True)

    features.columns = [commonWords['Word']]
    return (features, df['Harry Potter'].iloc[fromPos:endPos])

X, y = get_features(17925, 18000)
print(X)
print(y)