import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv('6_small.csv')
print(data)
X=data.iloc[:, :-1]
y=data.iloc[:, -1]
le=LabelEncoder()

print('\n The enocded data attributes is shown below\n',X)
print('The encoded labels are \n',y)

X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)

classifier=GaussianNB()
classifier.fit(X_train,y_train)

from sklearn.metrics import accuracy_score
y_pred=classifier.predict(X_test)

print("actual labels of testings samples:",y_test)
print("predicted labels of testing samples:",y_pred)
print("accuracy is:",accuracy_score(y_pred,y_test))