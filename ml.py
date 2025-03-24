# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score

# # Load the Iris dataset
# iris = load_iris()
# X = iris.data
# y = iris.target

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Initialize the Decision Tree Classifier
# tewx = DecisionTreeClassifier()

# # Train the classifier
# tewx.fit(X_train, y_train)

# # Make predictions
# y_pred = tewx.predict(X_test)

# # Calculate the accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy:.2f}')


# we willl use a algorithim which is called descision tree 
#it is come in scikit learn library
# sklearn is a package comes in scikit learn
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
data = pd.read_csv('music.csv')
#inthis data set there are data of alot of people that shows anybody is liking music or not 

#now we will give input for our model (we denote this as X):

X = data.drop(columns="genre") #it will create a new data set but in this dataset
#the genre column is not avaliable

y = data['genre'] #now this is output that is required for our model (suoervised)
#this will create a dataset where only genre column is avaliable

# now will create our model for prediciting datas
#we will use DecisionTreeClassifier as our model

moddel = DecisionTreeClassifier()

moddel.fit(X, y) #takes 2 parameter for prediction
#now we will try to predict
prediction = moddel.predict([[21,1], [22, 0]]) #21, 22 is from data when u see data you will understand
prediction