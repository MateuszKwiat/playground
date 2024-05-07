import pandas as pd

from scipy.stats import t
from math import sqrt

points = list(pd.read_csv('https://bit.ly/3C8JzrM', delimiter=',').itertuples())

n = len(points)

m = 1.75919315
b = 4.69359655

x_0 = 50
x_mean = sum(p.x for p in points) / len(points)

t_value = t(n - 2).ppf(0.975)

standard_error = sqrt(sum((p.y - (m * p.x + b))**2 for p in points) / (n - 2))

error_margin = t_value * standard_error * sqrt(1 + (1 / n) + (n * (x_0 - x_mean)**2) / (n * sum(p.x**2 for p in points) - sum(p.x for p in points)**2))

prediction = m * x_0 + b

print(prediction - error_margin, prediction + error_margin)