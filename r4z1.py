import pandas as pd
import numpy as np
import scipy.stats as stats

data_r4z1 = pd.read_excel('r4z1.xlsx', skiprows=1)

r = 6
X1 = 118.05
Xr = 126.05
s = 5
Y1 = 81.05
Ys = 87.05

x_intervals = np.linspace(X1, Xr, r + 1)
y_intervals = np.linspace(Y1, Ys, s + 1)

data_r4z1['X_bin'] = pd.cut(data_r4z1.iloc[:, 0], bins=x_intervals, include_lowest=True)
data_r4z1['Y_bin'] = pd.cut(data_r4z1.iloc[:, 1], bins=y_intervals, include_lowest=True)

contingency_table = pd.crosstab(data_r4z1['X_bin'], data_r4z1['Y_bin'])
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
alpha = 0.025

print(f"Хи-квадрат: {chi2}")
print(f"Степени свободы: {dof}")
print(f"p-значение: {p}")
print(f"Ожидаемые частоты: \n{expected}")

if p < alpha:
    print("Гипотеза независимости отвергается")
else:
    print("Нет оснований отвергать гипотезу независимости")