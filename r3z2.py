import pandas as pd
import numpy as np
import scipy.stats as stats

def confidence_interval(successes, trials, confidence_level=0.99):
    p_hat = successes / trials
    Z = stats.norm.ppf(confidence_level)
    lower_bound = p_hat - Z * np.sqrt((p_hat * (1 - p_hat)) / trials)
    return lower_bound

data_r3z2 = pd.read_excel('r3z2.xlsx', header=None, skiprows=1)
successes = len(data_r3z2[data_r3z2.iloc[:, 0] > 118.5])
trials = len(data_r3z2)

lower_bound = confidence_interval(successes, trials)
print(f"Нижняя доверительная граница для вероятности успеха: {lower_bound}")