#read csv using pandas
# using KNN algorithm

import csv
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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


def WetherPredictor(wether,temp):
    pass    


def main():
    print("MarvellousInfosystems_PlayPredictor")
    # wether=input("Enter the wether(sunny,obercast,rainy):")
    # temp=input("Enter the tempreture(hot,cold,mild):")
    
    # if wether.lower()=="sunny":
    #     wether=0
    # elif(wether.lower()=="overcast"):
    #     wether=1
    # elif(wether.lower()=="rainy"):
    #     wether=2
    # else:
    #     print("Error: wrong input(wether)")
    #     exit()
        
    # if (temp.lower()=='hot'):
    #     temp=3
    # elif(temp.lower()=="cold"):
    #     temp=4 
    # elif(temp.lower()=="mild"):
    #     temp=5
    # else:
    #     print("Error:wrong Input(tempreture)")    
           
    # WetherPredictor(wether,temp)
    
    
if __name__=="__main__":
    main()