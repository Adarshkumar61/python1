from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split #this will help us by divide into 2 parts
from sklearn.metrics import accuracy_score
#1 for traning
#2 for testing
import pandas as pd
data = pd.read_csv('music.csv')  #inthis data set there are data of alot of people that shows anybody is liking music or not 
#now we will give input for our model (we denote this as X):

X = data.drop(columns="genre") #this is input
#it will create a new data set but in this dataset
#the genre column is not avaliable

y = data['genre'] #this is output
#now this is output that is required for our model (suoervised)
#this will create a dataset where only genre column is avaliable

# we will call the train_test_model fn:
X_train, X_test, y_train,y_test =  train_test_split(X, y, test_size=0.2)

# now will create our model for prediciting datas
#we will use DecisionTreeClassifier as our model

moddel = DecisionTreeClassifier()

moddel.fit(X_train, y_train) #takes 2 parameter for prediction (it will train the model based on data (input and output))

prediction = moddel.predict(X_test)
score = accuracy_score(y_test, prediction) #return accurracy of our model
