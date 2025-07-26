from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

def calc_class_stats(X, y):
    class_labels = np.unique(y)
    class_means = [np.mean(X[y == label], axis=0) for label in class_labels]
    class_stds = [np.std(X[y == label], axis=0) for label in class_labels]
    distance_between_means = np.linalg.norm(class_means[0] - class_means[1])
    return class_means, class_stds, distance_between_means

X, y = pd.read_csv("EEG_Eye_State_Classification.csv").drop('eyeDetection', axis=1).values, pd.read_csv("EEG_Eye_State_Classification.csv")['eyeDetection'].values
class_means, class_stds, dist_means = calc_class_stats(X, y)
print("Class 0 Mean:", class_means[0])
print("Class 1 Mean:", class_means[1])
print("Class 0 Std:", class_stds[0])
print("Class 1 Std:", class_stds[1])
print("Distance Between Class Means:", dist_means)
