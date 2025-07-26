import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plotfeature_histogram(feature_vector, feature_name):
    plt.hist(feature_vector, bins=30, edgecolor='black')
    plt.title(f"Histogram of {feature_name}")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
    return np.mean(feature_vector), np.var(feature_vector)

df = pd.read_csv("EEG_Eye_State_Classification.csv")
feature_index = 0
feature_name = df.columns[feature_index]
mean_val, var_val = plotfeature_histogram(df.iloc[:, feature_index], feature_name)
print(f"Mean of {feature_name}: {mean_val}")
print(f"Variance of {feature_name}: {var_val}")
