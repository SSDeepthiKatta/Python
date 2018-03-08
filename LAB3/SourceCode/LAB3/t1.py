#Lab Assignment-3

#Question -1

#Pick any dataset from the dataset sheet in class sheet and make one prediction model using your imagination with Linear Discriminant Analysis*.
# Some examples are:
# a.In the report provide convincible explanations about the difference of logisticregression and Linear Discriminant Analysis.b.
# You can also pick dataset of your own.

#importing required libraries
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#loading from the dataset
digi = datasets.load_digits()
X = digi.data
y = digi.target
names = digi.target_names

#importing scikit library to get the prediction model
from sklearn.model_selection import train_test_split
X_t_r, X_t, y_t_r, y_t = train_test_split(X, y, test_size=0.30)
#using K- neihbours classification
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_t_r, y_t_r)
#implementing prediction model with 30% testing data and 70% training data
y_pred = classifier.predict(X_t)

#Linear Discriminant Analysis
lda = LinearDiscriminantAnalysis(n_components=2)
output = lda.fit(X_t, y_pred).transform(X)

##plotting LDA
plt.figure()
colors = ['red', 'green', 'blue']
lw = 2
for color, i, name in zip(colors, [0, 1, 2], names):
 plt.scatter(output[y == i, 0], output[y == i, 1], alpha=.8, color=color, label=name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA on prediction model of DIGITS Dataset')
plt.show()