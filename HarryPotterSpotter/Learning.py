import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('HP_Dataframe.csv', index_col='Unnamed: 0', encoding = "ISO-8859-1")
X = df['Sentences']
y = df['Harry Potter']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
print(df)