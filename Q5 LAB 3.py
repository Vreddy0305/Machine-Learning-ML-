from sklearn.neighbors import KNeighborsClassifier

def train_knn_classifier(X_train, y_train, k):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    return model

knn_k3 = train_knn_classifier(X_train, y_train, k=3)
print("k-NN Classifier (k=3) trained.")
