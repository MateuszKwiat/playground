
from scipy.stats import norm

population_mean = 10_345
population_std_dev = 552 

sample_size = 45
sample_mean = 11_641

x1 = norm.ppf(.025, population_mean, population_std_dev)
x2 = norm.ppf(.975, population_mean, population_std_dev)

print(f'sample mean value: {sample_mean}')
print(f'range for 5% statistical significance: [{x1:.2f}, {x2:.2f}]')

p = 1. - norm.cdf(sample_mean, population_mean, population_std_dev)

p_value = p + p 

print(f'p value: {p_value:.5f}')

if p_value <= .05:
    print('two sides test acceptence')
else:
    print('two sides test rejection')