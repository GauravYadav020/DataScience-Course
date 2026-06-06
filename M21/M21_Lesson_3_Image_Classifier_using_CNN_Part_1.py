# M21 Lesson 3 – Image Classifier using CNN – Part 1
# Short Description: Building the first part of an image classification model using CNN.

# Activity 1
# Goal: Prepare image dataset and preprocess for CNN training.
# Summary: Load images, resize, normalize, and create data generators.

### **1. Import Libraries**
"""

# Import Libraries
import keras
import tensorflow.keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
from keras.constraints import maxnorm
from keras.utils import np_utils 
from tensorflow.keras.optimizers import SGD

"""### **2. Import Dataset**"""

# Load Dataset and split it into train and test 
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Let's check few images of this dataset
# plot first few images
for i in range(9):
	# define subplot
	plt.subplot(330 + 1 + i)
	# plot raw pixel data
	plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
# show the figure
plt.show()

"""### **3. Preprocess this dataset**

- The image data cannot be fed directly into the model so we need to perform some operations and process the data to make it ready for our neural network.
"""

# convert class vectors to binary class matrices
from tensorflow.keras.utils import to_categorical
num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# convert from integers to floats
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# normalize to range 0-1
x_train /= 255
x_test /= 255

# Let's check normalized images
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

"""### **4. Model Building**"""

# Building Models
# Adding layers one by one
# Since this is a classification problem -
# activation function for hidden layer - relu
# activation function for output layer - softmax
# Input shape (since coloured and 32x32 pixels) - (32,32,3)
# Output shape - 10 
# Drop out layer is added to deactivate some of the neurons for that layer
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(32,32,3), activation='relu', padding='same')) 
model.add(Dropout(0.2)) 
model.add(Conv2D(32, (3, 3), activation='relu', padding='same')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Conv2D(64, (3, 3), activation='relu', padding='same')) 
model.add(Dropout(0.2)) 
model.add(Conv2D(64, (3, 3), activation='relu', padding='same')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Conv2D(128, (3, 3), activation='relu', padding='same')) 
model.add(Dropout(0.2)) 
model.add(Conv2D(128, (3, 3), activation='relu', padding='same')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Flatten()) 
model.add(Dropout(0.2)) 
model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3))) 
model.add(Dropout(0.2)) 
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3))) 
model.add(Dropout(0.2)) 
model.add(Dense(num_classes, activation='softmax'))
print(model.summary())

# Model Compilation
# This is a multi class classification problem
# thus loss function - categorical cross entropy and metrics as accuracy
# Optimizer being used is SGD (Stochastic Gradient Descent)
# lr stands for learning rate
opt = SGD(learning_rate=0.01, momentum=0.9, decay=0.0002, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
