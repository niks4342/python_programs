import csv
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def winepredictor(filename):
    data=pd.read_csv(filename)
    
    alcohol=list(data.Alcohol)
    malic=data.Malic_acid
    ash=data.Ash
    alcanality=data.Alcalinity_of_ash
    mg=data.Magnesium
    phenol=data.Total_phenols
    falv=data.Flavanoids
    non_flav=data.Nonflavanoid_phenols
    color=data.Color_intensity
    diluted_wines=data.diluted_wines
    Proline=data.Proline
    
    feature=list(zip(alcohol,malic,ash,alcanality,mg,phenol,falv,non_flav,color,diluted_wines,Proline))
    target=data.Class
    
    X_train,X_test,y_train,y_test=train_test_split(feature,target,test_size=0.3)
    
    list_i=list()
    list_accu=list()
    
    for i in range(3,54):
        model=KNeighborsClassifier(n_neighbors=i)
        model.fit(X_train,y_train)
        predict=model.predict(X_test)
        
        accu=metrics.accuracy_score(y_test,predict)*100
        print("Accuracy of algorithm  ",i," is:",accu)
        
        list_i.append(i)
        list_accu.append(accu)
   
    fig=plt.figure()
    plt.plot(list_i,list_accu)
    plt.show()
    fig.savefig("wine_predictor.pdf")
    plt.close()
    
    
def main():
    print("___________ Wine Predictor ___________")
    
    filename="WinePredictor.csv"
    winepredictor(filename)
    
if __name__=="__main__":
    main()