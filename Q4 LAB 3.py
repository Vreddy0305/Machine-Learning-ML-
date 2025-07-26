from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("EEG_Eye_State_Classification.csv")
X = df.drop('eyeDetection', axis=1).values
y = df['eyeDetection'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Train samples:", len(X_train))
print("Test samples:", len(X_test))
