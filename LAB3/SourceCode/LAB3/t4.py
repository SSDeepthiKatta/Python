# LAB Assignment - 3
#Question - 4
#Report your views on the k nearest neighbor algorithm
# when we change the K how it will affect the accuracy.
#  Provide a good justification about the changes of the accuracy when we change the amount of K.
# For example: compare the accuracy when K=1 and K is a big number like 50, why the accuracy will change?

import matplotlib.pyplot as plt
from sklearn import datasets, metrics

#Loading the dataset
irisdataset=datasets.load_iris()
#getting the data and response of the dataset
X=irisdataset.data
y=irisdataset.target

#building a prediction model with 20% testing data and 80% training data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
# standard scaler methods are used for normalizing the values of training data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Using KNN algorithm to predict the output values with neighbours changing with K value
from sklearn.neighbors import KNeighborsClassifier
scores = []
# Calculating tha accuracy for K values ranging from 1 to 50
for i in range(1, 50):
    knn = KNeighborsClassifier(n_neighbors=i) #here the algorithm is run for every k value
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test) #prediction is calculated
    scores.append(metrics.accuracy_score(y_test, pred_i)) #accuracy is appended to the scores list

#plotting the graph using matplotlib
plt.plot(range(1, 50), scores, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Accuracy - K Value')
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.show()