from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def evalclassifier(model, X, y):
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    prec = precision_score(y, preds)
    rec = recall_score(y, preds)
    f1 = f1_score(y, preds)
    cm = confusion_matrix(y, preds)
    return acc, prec, rec, f1, cm

acc_test, prec_test, rec_test, f1_test, cm_test = evalclassifier(knn_k3, X_test, y_test)

acc_train, prec_train, rec_train, f1_train, cm_train = evalclassifier(knn_k3, X_train, y_train)


print("Test Metrics:\n", f"Accuracy: {acc_test}\nPrecision: {prec_test}\nRecall: {rec_test}\nF1 Score: {f1_test}\nConfusion Matrix:\n{cm_test}")

print("\nTrain Metrics:\n", f"Accuracy: {acc_train}\nPrecision: {prec_train}\nRecall: {rec_train}\nF1 Score: {f1_train}\nConfusion Matrix:\n{cm_train}")


if acc_train > acc_test and (acc_train - acc_test) > 0.1:

    print("Model is OVERFITTING.")

elif acc_train < 0.8:

    print("Model is UNDERFITTING.")
else:

    print("Model is WELL-FITTED.")

