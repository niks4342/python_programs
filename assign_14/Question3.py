# using KNN algorithm

import csv

import pandas as pd
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

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
X_train,X_test,y_train,y_test=train_test_split(feature,p_encoding,test_size=0.3)

list_i=list()
list_accu=list()

for i in range(3,24):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train,y_train)
    ret=model.predict(X_test)
    accuracy=metrics.accuracy_score(y_test,ret)*100
    print("Accuracy of algorithm ",i, " is:",accuracy)
    list_i.append(i)
    list_accu.append(accuracy)



fig=plt.figure()
plt.plot(list_i,list_accu)
plt.show()
fig.savefig("mat.pdf")
plt.close()