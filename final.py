import numpy as np
import pandas
from keras.models import Sequential
from keras.layers import Dense
from sklearn.pipeline import Pipeline

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('db.csv')
X = dataset.iloc[:, 0:6].values
y = dataset.iloc[:, 6].values

# encode class values as integers
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
# convert integers to dummy variables (i.e. one hot encoded)
from keras.utils import np_utils
dummy_y = np_utils.to_categorical(encoded_Y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size = 0.2, random_state = 0)

#Scalng the independent variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
#X_test = sc_X.transform(X_test)
"""
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

    # Initialising the ANN
classifier = Sequential()
    
    # Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 15, init = 'uniform', activation = 'relu', input_dim = 6))
classifier.add(Dense(output_dim = 30, init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = 60, init = 'uniform', activation = 'relu'))
   
classifier.add(Dense(output_dim = 11, init = 'uniform', activation = 'softmax'))

classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
classifier.fit(X_train,y_train, validation_data=(X_test,y_test),batch_size = 10, nb_epoch = 100)
score=classifier.evaluate(X_test,y_test)
print("score:",score[1]*100)
classifier.save('fin.h5')