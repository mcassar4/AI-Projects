from inference import DiscreteDistribution

dist = DiscreteDistribution()
dist['a'] = 0
dist['b'] = 0
dist['c'] = 100
dist['d'] = 0

# print(dist)

# sample = dist.sample()
# print(sample)
N = 100000.0
samples = [dist.sample() for _ in range(int(N))]
print(round(samples.count('a') * 1.0/N, 1))  # proportion of 'a'
# 0.1
print(round(samples.count('b') * 1.0/N, 1))
# 0.5
print(round(samples.count('c') * 1.0/N, 1))
# 0.3
print(round(samples.count('d') * 1.0/N, 1))
# 0.1
