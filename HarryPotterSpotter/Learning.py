import pandas as pd
from sklearn.model_selection import train_test_split

def split_into_words(df):
    word_df = df['Sentences'].apply(str.split)
    return word_df


df = pd.read_csv('HP_Dataframe.csv', index_col='Unnamed: 0', encoding = "ISO-8859-1")
X = df['Sentences']
y = df['Harry Potter']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
word_df = split_into_words(df)
print(word_df)