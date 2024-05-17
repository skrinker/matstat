import scipy.optimize
import pandas as pd
import numpy as np
import scipy
from scipy.stats import kurtosis, skew, ecdf
import csv

data = []

with open('r3z1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

def equation(x):
    result = 0
    for k in data:
        result += 2/x - k
    return result

result = scipy.optimize.fsolve(equation, 5)

print("Корень уравнения:", result)