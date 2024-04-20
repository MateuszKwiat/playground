from math import sqrt

data = [1.78, 1.75, 1.72, 1.74, 1.77]

mean_val = sum(data) / len(data)

standard_deviation = sqrt(sum((mean_val - d)**2 for d in data) / len(data))

print(f'mean value of data: {mean_val}')
print(f'standard deviation of data: {standard_deviation}')