# -*- coding: utf-8 -*-
"""01_neural_network_regression_with_tensorflow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EEzm-7k3D0cEQFEE14FdKE6GeJEJcvts

#Introduction to Regression in neural network with tensorflow
"""

#import tensorflow
import tensorflow as tf
print(tf.__version__)

"""## Creating data to view and fit"""

import numpy as np
import matplotlib.pyplot as plt

#Create Feature
X=np.array([-7,-4,-1,2,5,8,11,14])

#Create labels
y=[3,6,9,12,15,18,21,24]

#Visualize it
plt.scatter(X,y)

y==X+10

"""### Input and Output shape"""

#Let's create demo tensor for out house price prediction model
house_info=tf.constant(['bedroom','bathroom','garage'])
house_price=tf.constant([939700])
house_info,house_price

"""## steps in modelling in tensorflow

1. **Creating the model**-defining I/P and O/P as well as hidden layers.
2. **Comipling the model**-We have to compile a model-define the loss function(in the other words, it tell our model how wrong it is) and the optimizer(tells our model how to improve the pattern its learning) and evaluation metrices(what we can use to interpet the perfomance of our model) .
3. **Fitting the model**-letting model try to find patterns between X and y(Features and labels).
"""

X=tf.constant(X)
y=tf.constant(y)
X,y

#Set seed
tf.random.set_seed(42)

#1.Create the model using the Squential API
model=tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])

#2.Compile the model
model.compile(loss=tf.keras.losses.mae, #mae stands for mean absoulate error
              optimizer=tf.keras.optimizers.SGD(),#SGD stands for stochastics gradient descent
              metrics=["mae"])

#3.Fit the model
model.fit(tf.expand_dims(X,axis=-1),y,epochs=10,verbose=1)

#Let's predict the value
y_pred=model.predict([17])
y_pred

"""## Improving our model

we can improve the model by altering the steps og creation

1. **Creating the model**-We can add more layers,increase he number of hidden neurons within each layers, change the activation function of each layer.
2. **Compiling the model**-we can change the optimization function or perhaps we can change the **learning rate** of optimization function.
3. **Fitting the model**-we can add more epochs or on more data.
"""

## Let's rebuild our model

#1.Creating the model
model=tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1))

#2. Compile the model
model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics=["mae"])

#3.Fit the model
model.fit(tf.expand_dims(X,axis=-1),y,epochs=100)

#Remind ourselves on the data
X,y

#Let's see out models prediction has improve
model.predict([17])

#Let's improve another paramter

#1.Create a model
model=tf.keras.Sequential()
model.add(tf.keras.layers.Dense(50))
model.add(tf.keras.layers.Dense(1))

#2.Compile the model
model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              metrics=['mae'])

#3.Fit the model
model.fit(tf.expand_dims(X,axis=-1),y,epochs=100)

#Let's remind ourselves the data
X,y

#Let's predict the value...Hopefully its closer
model.predict([17])

"""## Evaluating the model's perfomance"""

#Making the bigger dataset

X=tf.range(-100,100,4)
X

#Makes labels for dataset
y=X+10
y

#Visualize the data
import matplotlib.pyplot as plt

plt.scatter(X,y)

#Check the lenght of dataset
len(X)

#Split the data into train and test sets
X_train= X[:40] #80% of total data
y_train= y[:40]

X_test= X[40:] #20% of total data
y_test= y[40:]

len(X_train),len(X_test)

"""## Visualize the model"""

#Let's again create the same model...

#1. Create the model with input_shape
model=tf.keras.Sequential([
    tf.keras.layers.Dense(10,input_shape=[1],name="hidden_layer_1"),
    tf.keras.layers.Dense(1,name="output_layer")]
    ,name="model_1")

#2.Compile the model
model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.SGD(),
              metrics=['mae'])

#3.Fit the model
#model.fit(tf.expand_dims(X_train,axis=-1),y_train,epochs=100)

model.summary()

#Let's fit the model
model.fit(X_train,y_train,epochs=100,verbose=0)

model.summary()

from tensorflow.keras.utils import plot_model

plot_model(model,show_shapes=True)

"""### Visualizing our model's prediction"""

#Let's predict the value of X_test
y_preds= model.predict(X_test)
y_preds

y_test

#Let's create a plotting function
def plot_predictions(train_data=X_train,
                      train_label=y_train,
                      test_data=X_test,
                      test_label=y_test,
                      prediction=y_preds):
  '''
  plot traing ,test and prdeiction data and compare it with ground truth'''
  plt.figure(figsize=(10,7))
  #plot training data IN BLUE
  plt.scatter(train_data,train_label,c="b",label="Training data")
  #plot test data in green
  plt.scatter(test_data,test_label,c='g',label="Testing data")
  #plot model's prediction in red
  plt.scatter(test_data,prediction,c='r',label="Prediction")
  #show legend
  plt.legend();

plot_predictions(train_data=X_train,train_label=y_train,test_data=X_test,test_label=y_test,prediction=y_preds)

"""### Evaluating our model's prediction with regression evaluation matrics"""

#Calculate mean absolute error
mae_1=tf.metrics.mean_absolute_error(y_test,tf.squeeze(y_preds))
mae_1

#Evaluate the model
model.evaluate(X_test,y_test)

#Calcuate mean square error
mse_1=tf.metrics.mean_squared_error(y_test,tf.squeeze(y_preds))
mse_1

#Let's make function to rresue MAE and MSE
def mae(y_true,y_pred):
  return tf.metrics.mean_absolute_error(y_true,tf.squeeze(y_pred))

def mse(y_true,y_pred):
  return tf.metrics.mean_squared_error(y_true,tf.squeeze(y_pred))

"""### Running experiments to improve our model

1. Get more data
2. Create larger model
3. Train for longer
"""

X_train,y_train

"""### `model_1` is same as previous one

**Build `model_2`**

* 2 layers,100 epochs
"""

#set random seed
tf.random.set_seed(42)

#1.Create a model
model_2=tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])

#2.Compile the model
model_2.compile(loss=tf.keras.losses.mae,
                optimizer=tf.keras.optimizers.SGD(),
                metrics=['mse'])

#3.Fit the model
model_2.fit(tf.expand_dims(X_train,axis=-1),y_train,epochs=100,verbose=0)

#Make and plot the model's prediction
y_pred_2=model_2.predict(X_test)
plot_predictions(prediction=y_pred_2)

#Evaluation metrics
mse_2=mse(y_test,y_pred_2)
mae_2=mae(y_test,y_pred_2)
mse_2,mae_2

"""**Build `model_3`**

* 2 layer and eochs-500
"""

#1.Create a model
model_3=tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])

#2.Compile the model
model_3.compile(loss=tf.keras.losses.mae,
                optimizer=tf.keras.optimizers.SGD(),
                metrics=['mae'])

#3.Fit the model
model_3.fit(tf.expand_dims(X_train,axis=-1),y_train,epochs=500,verbose=0)

#Make and plot the model's prediction
y_pred_3=model_3.predict(X_test)
plot_predictions(prediction=y_pred_3)

#Evaluation metrics
mse_3=mse(y_test,y_pred_3)
mae_3=mae(y_test,y_pred_3)
mse_3,mae_3

"""### Comparing the result of our experiment"""

#Let's compare our model's resulting using pandas's dataframe
import pandas as pd
result_list=[['model_1',mae_1.numpy(),mse_1.numpy()],
             ['model_2',mae_2.numpy(),mse_2.numpy()],
             ['model_3',mae_3.numpy(),mse_3.numpy()]]

all_result=pd.DataFrame(result_list,columns=['model','MAE','MSE'])
all_result.set_index('model')
all_result

"""### Saving our models"""

#Save model using SaveModel Format
model_2.save("Best_Model_SaveModel_Format")

#Save model using the HDF5 format
model_2.save("Best_Model_HDF5_Format.h5")

"""### Loading in a save model"""

#Load in SaveModel format
loaded_SavedModel_format=tf.keras.models.load_model("/content/Best_Model_SaveModel_Format")
loaded_SavedModel_format.summary()

#Check that architecture is same
model_2.summary()

#Check if our loaded model makes same perdiction or not as model_2
model_2_pred=model_2.predict(X_test)
loaded_pred=loaded_SavedModel_format.predict(X_test)
tf.squeeze(model_2_pred)==tf.squeeze(loaded_pred)

#Load model of HDF5 format
loaded_HDF5_format=tf.keras.models.load_model("/content/Best_Model_HDF5_Format.h5")
loaded_HDF5_format.summary()

# Check the prdeciction
loaded_h5_preds=loaded_HDF5_format.predict(X_test)
model_2_pred=model_2.predict(X_test)
loaded_h5_preds==model_2_pred

"""### A larger Example"""



#Import required libarires
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

# Read in insurance data set
insurance=pd.read_csv("/content/insurance.csv")
insurance

#Let's try one-hot encode our dataframec
insurance_one_hot = pd.get_dummies(insurance)
insurance_one_hot.head()

#Create X and Y values(Features and labels)
X=insurance_one_hot.drop("charges",axis=1)
y=insurance_one_hot["charges"]

#View X
X.head()

#View y
y.head()

#Create training and testing set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
len(X),len(X_train),len(X_test)

#Build model

#set random seed
tf.random.set_seed(42)

#1.Create a model
insurance_model=tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])

#2.Compile the model
insurance_model.compile(loss=tf.keras.losses.mae,
                        optimizer=tf.keras.optimizers.SGD(),
                        metrics=["mae"])

#3.Fit the model
insurance_model.fit(tf.expand_dims(X_train,axis=-1),y_train,epochs=100,verbose=0)

#Check the result of the insurance model  on the test data
insurance_model.evaluate(X_test,y_test)

"""### Lets change the model"""

#Build model

#set random seed
tf.random.set_seed(42)

#1.Create a model
insurance_model_2=tf.keras.Sequential([
    tf.keras.layers.Dense(100),
    tf.keras.layers.Dense(1)
])

#2.Compile the model
insurance_model_2.compile(loss=tf.keras.losses.mae,
                        optimizer=tf.keras.optimizers.Adam(),
                        metrics=["mae"])

#3.Fit the model
insurance_model_2.fit(tf.expand_dims(X_train,axis=-1),y_train,epochs=100,verbose=0)

#Check the result of the insurance model  on the test data
insurance_model_2.evaluate(X_test,y_test)

#Build model

#1.Create a model
insurance_model_3=tf.keras.Sequential([
    tf.keras.layers.Dense(20),
    tf.keras.layers.Dense(20),
    tf.keras.layers.Dense(20),
    tf.keras.layers.Dense(1)
])

#2.Compile the model
insurance_model_3.compile(loss=tf.keras.losses.mae,
                        optimizer=tf.keras.optimizers.Adam(),
                        metrics=["mae"])

#3.Fit the model
insurance_model_3.fit(tf.expand_dims(X_train,axis=-1),y_train,epochs=200,verbose=0)

#Check the result of the insurance model  on the test data
insurance_model_3.evaluate(X_test,y_test)