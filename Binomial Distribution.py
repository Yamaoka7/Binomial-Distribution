from scipy.stats import binom

n = 10  # Number of trials
p = 0.5  # Probability of success
k = 3  # Number of successes
probability = binom.pmf(k, n, p)
print(f"Probability of {k} successes in {n} trials with probability {p}: {probability}")
