import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split_into_words(df):
    word_df = df['Sentences'].apply(str.split)
    return word_df

def get_n_most_common_words(count):
    words = (pd.read_csv('word_counts.csv', encoding = "ISO-8859-1")
             .nlargest(n=count, columns=['Count'], keep = 'first'))
    print(len(words))
    return words

def get_data():
    df = pd.read_csv('HP_Dataframe.csv', index_col='Unnamed: 0', encoding = "ISO-8859-1")
    #X = df['Sentences']
    #y = df['Harry Potter']
    #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    word_df = split_into_words(df)
    return word_df

featuresWordMap = get_n_most_common_words(600)['Word'].reset_index().drop('index', axis=1)

print(featuresWordMap)
wordDF = get_data()
features = np.zeros(shape=(1,len(featuresWordMap)))
temp = wordDF.iloc[100]

feature = featuresWordMap.isin(temp)
print(bla)
#print(features)
# print(temp)