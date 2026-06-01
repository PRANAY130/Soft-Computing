import numpy as np

# Truth tables
X = np.array([[0,0],[0,1],[1,0],[1,1]])

y_and = np.array([0, 0, 0, 1])
y_or  = np.array([0, 1, 1, 1])

def train_slp(X, y, lr=0.1, epochs=10):
    w = np.zeros(2)   # weights
    b = 0             # bias

    for epoch in range(epochs):
        for i in range(len(X)):
            if (np.dot(w, X[i]) + b) >= 0.5:
                output = 1
            else:
                output = 0
            error = y[i] - output
            w += lr * error * X[i]
            b += lr * error

    return w, b

def predict(X, w, b):
    results = []
    for x in X:
        if (np.dot(w, x) + b) >= 0.5:
            results.append(1)
        else:
            results.append(0)
    return results

# AND gate
print("=== AND Gate ===")
w, b = train_slp(X, y_and)
preds = predict(X, w, b)
for i in range(4):
    print(f"{X[i][0]} AND {X[i][1]} = {preds[i]}  (expected {y_and[i]})")

# OR gate
print("\n=== OR Gate ===")
w, b = train_slp(X, y_or)
preds = predict(X, w, b)
for i in range(4):
    print(f"{X[i][0]} OR  {X[i][1]} = {preds[i]}  (expected {y_or[i]})")
