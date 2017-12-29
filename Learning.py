import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.externals import joblib


def split_into_words(df):
    word_df = df['Sentences'].apply(str.split)
    return word_df

def get_n_most_common_words(count):
    words = (pd.read_csv('word_counts.csv', encoding = "ISO-8859-1")
             .sort_values('Count', ascending=False).iloc[:count])
    return words

def get_data():
    df = pd.read_csv('HP_Dataframe.csv', index_col='Unnamed: 0', encoding = "ISO-8859-1")
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

X, y, wordDict = get_features(2000)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
this_C = 1.0
clf = SVC(kernel='linear', C=this_C).fit(X_train, y_train)
print('Score on training set is: {:.2f}'.format(clf.score(X_train, y_train)))
print('Score on test set is: {:.2f}'.format(clf.score(X_test, y_test)))
print('Halelujah!!!')

print('Word dict: {}'.format(wordDict))
print('X: {}'.format(X))
print('y: {}'.format(y))
joblib.dump(clf, 'theSpotter.pkl') 