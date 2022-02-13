# using decision tree algorithm

import csv
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree

data=pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

wether=data.Wether
temp=data.Temperature
play=data.Play

obj=preprocessing.LabelEncoder()
# wether encoding
w_encodeing=obj.fit_transform(wether)
# temprature encoding
t_encoding=obj.fit_transform(temp)
# play encoding
p_encoding=obj.fit_transform(play)
feature=list(zip(w_encodeing,t_encoding))# wether & temp
print(feature)
# spliting
X_train,X_test,y_train,y_test=train_test_split(feature,p_encoding,test_size=0.5)

classifier=tree.DecisionTreeClassifier()
classifier.fit(X_train,y_train)

ret=classifier.predict(X_test)

accuracy=accuracy_score(y_test,ret)
print("Accuracy of algorithm is:",accuracy*100)