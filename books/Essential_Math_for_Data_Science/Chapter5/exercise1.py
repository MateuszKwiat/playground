import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=',')

X = df.values[:, :-1]
Y = df.values[:, -1]

model = LinearRegression()

model.fit(X, Y)

m = model.coef_.flatten()
b = model.intercept_.flatten()

print('y = {0}x + {1}'.format(m, b))

fig, ax = plt.subplots()

ax.scatter(X, Y, s=7, color='green')
ax.plot(X, m*X + b, color='purple')

plt.show()