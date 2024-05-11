import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('https://tinyurl.com/y6r7qjrp', delimiter=',')

X = df.values[:, :-1]
Y = df.values[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3)

nn = MLPClassifier(
    solver='sgd',
    hidden_layer_sizes=(3, ),
    activation='relu',
    max_iter=100_000,
    learning_rate_init=0.005
)

nn.fit(X_train, Y_train)

Y_pred = nn.predict(X_test)

print(nn.score(X_train, Y_train))
print(nn.score(X_test, Y_test))

print(confusion_matrix(y_true=Y_test, y_pred=Y_pred))