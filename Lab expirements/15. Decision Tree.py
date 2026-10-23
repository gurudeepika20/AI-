
from sklearn.tree import DecisionTreeClassifier

X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = [1, 1, 0, 0]

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

print("Prediction:", model.predict([[1, 1]])[0])
print("Prediction:", model.predict([[0, 0]])[0])

