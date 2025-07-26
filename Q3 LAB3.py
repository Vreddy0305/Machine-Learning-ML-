import numpy as np
import matplotlib.pyplot as plt

def calcminkowski_distances(vec1, vec2, r_values):
    return [np.linalg.norm(vec1 - vec2, ord=r) for r in r_values]

def plotminkowski(r_values, distances):
    plt.plot(r_values, distances, marker='o')
    plt.title("Minkowski Distance vs r")
    plt.xlabel("r")
    plt.ylabel("Distance")
    plt.grid(True)
    plt.show()

df = pd.read_csv("EEG_Eye_State_Classification.csv").drop('eyeDetection', axis=1)
vec1, vec2 = df.iloc[0].values, df.iloc[1].values
r_range = range(1, 11)
distances = calcminkowski_distances(vec1, vec2, r_range)
plotminkowski(r_range, distances)
