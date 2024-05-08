import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

df = pd.read_csv('https://bit.ly/3imidqa', delimiter=',')

X = df.values[:, :-1]
Y = df.values[:, -1]

model = LogisticRegression(penalty=None)
kfold = KFold(n_splits=3, shuffle=True)

scores = cross_val_score(model, X, Y, cv=kfold)

print('score mean: {0:.2f}\nstandard deviation: {1:.2f}'.format(scores.mean(), scores.std()))