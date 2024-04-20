from math import sqrt
from scipy.stats import norm

def z_critical_value(p):
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail = (1.0 - p) / 2
    right_tail = 1 - ((1.0 - p) / 2)

    return norm_dist.ppf(left_tail), norm_dist.ppf(right_tail)

def confidence_interval(p, mean, std_dev, n):
    lower, upper = z_critical_value(p)
    lower_ci = lower * (std_dev / sqrt(n))
    upper_ci = upper * (std_dev / sqrt(n))

    return mean + lower_ci, mean + upper_ci

sample_size = 34
sample_mean = 1.715588
sample_std_dev = 0.029252

lower_ci, upper_ci = confidence_interval(.99, sample_mean, sample_std_dev, sample_size)

print(f'Confidence interval of 99%: [{lower_ci}, {upper_ci}]')