from sklearn import datasets
iris = datasets.load_iris()
iris_data = iris.data
iris_label = iris.target

from sklearn.model_selection import train_test_split
(train_data, test_data, train_label, test_label) = train_test_split(iris_data, iris_label, test_size=0.2)

from sklearn.svm import SVC
svc = SVC()
svc.fit(train_data, train_label)

predicted = svc.predict(test_data)
print(predicted)
print(test_label)

from sklearn import metrics
print(metrics.accuracy_score(test_label, predicted))


