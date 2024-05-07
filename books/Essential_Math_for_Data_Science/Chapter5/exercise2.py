import pandas as pd

from math import sqrt
from scipy.stats import t

df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=',')

correlation = df.corr(method='pearson')
print('data correlation:\n{0}'.format(correlation))

n = df.shape[0]
lower = t(n-1).ppf(.025)
upper = t(n-1).ppf(.975)

r = correlation['x']['y']

test_value = r / sqrt((1 - r**2) / (n - 2))

print(f'test value: {test_value:.2f}')
print(f'region of rejection: {lower:.2f}, {upper:.2f}')

if test_value < lower or test_value > upper:
    print('correlation is accepted, H0 denied')
else:
    print('correlation is denied, can\'t deny H0')

if test_value > 0:
    p_value = 1.0 - t(n - 1).cdf(test_value)
else:
    p_value = t(n - 1).cdf(test_value)

p_value = p_value * 2
print(f'P value: {p_value}')