from scipy.stats import norm

mean_val = 42
standard_deviation = 8

val = norm.cdf(30, loc=42, scale=8) - norm.cdf(20, loc=42, scale=8)

print(f'probability of Z-Phone lasting between 20 and 30 months: {val}')