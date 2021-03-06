# LAB ASSIGNMENT -3
# Question -2
'''implement Support Vector Machineclassification,
 1)Choose one of the dataset using the datasets features in the scikit-learn
 2)Load the dataset
 3)According to your dataset, split the data to 20% testing data, 80% training data(you can also use any other number)
 4)Apply SVC with Linear kernel
 5)Apply SVC with RBF kernel
 6)Report the accuracy of the model on both models separately and report their differences if there is
 7)Report your view how can you increase the accuracy and which kernel is the best for your dataset and why'''

from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
#Choose one of the dataset using the datasets features in the scikit-learn
from sklearn import svm
from sklearn.datasets import load_digits

C = 1.0
digits=load_digits() #load dataset
#getting the data and response of the dataset
x=digits.data
y=digits.target

#prediction model: splitting the data to 20% testing data, 80% training data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#Apply SVC with Linear kernel
model = svm.SVC(kernel='linear')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy for SVC linear kernel " + str(metrics.accuracy_score(y_test,y_pred)))

#Apply SVC with RBF kernel
model = svm.SVC(kernel='rbf')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy for SVC with rbf kernel " + str(metrics.accuracy_score(y_test,y_pred)))