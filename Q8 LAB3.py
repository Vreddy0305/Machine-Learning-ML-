import matplotlib.pyplot as plt

k_range = range(1, 12)
accuracies = []
for k in k_range:
    model = train_knn_classifier(X_train, y_train, k)
    accuracies.append(model.score(X_test, y_test))

plt.plot(k_range, accuracies, marker='o')
plt.title("Accuracy vs k")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()
