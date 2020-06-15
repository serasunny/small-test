from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

iris = load_iris()
print(iris.data.shape)
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.25, random_state = 33)
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)

print('The accuracy of K-Nearest Neighbor Classifier is: ', knn.score(X_test, y_test))
print(classification_report(y_test, y_predict, target_names = iris.target_names))
