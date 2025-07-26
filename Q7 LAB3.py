sample = X_test[0].reshape(1, -1)
prediction = knn_k3.predict(sample)
print("Predicted:", prediction[0])
print("Actual:", y_test[0])
