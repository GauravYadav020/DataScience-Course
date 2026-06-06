# M21 Lesson 5 – Let’s Build Digit Recognizer – 1
# Short Description: Starting the development of a digit recognition model using CNN on MNIST dataset.

# Activity 1
# Goal: Load and explore the MNIST dataset.
# Summary: Understand the structure of handwritten digit images and labels.

### **1. Import Libraries**
"""

# Import Libraries
import keras
import tensorflow.keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import SGD

"""### **2. Import Dataset**"""

# Load Dataset and split it into train and test 
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Let's check shape of different datasets
print("Train Dataset (x) :", x_train.shape)
print("Train Dataset (y) :", y_train.shape)
print("Test Dataset (x) :", x_test.shape)
print("Test Dataset (y) :", y_test.shape)

"""### Let's Understand these dimensions here -

- It is a dataset of 60,000 small squares 
- 28×28 pixel grayscale images of handwritten single digits between 0 and 9.
"""

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
- The dimension of the training data is (60000,28,28). The CNN model will require one more dimension so we reshape the matrix to shape (60000,28,28,1).
"""

# Let's reshape the training and testing data
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

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

# Set values for major parameters for model training
batch_size = 128
num_classes = 10
epochs = 10

# Building Models
# Adding layers one by one
# Since this is a classification problem -
# activation function for hidden layer - relu
# activation function for output layer - softmax
# Input shape (since grayscale) - (28,28,1)
# Output shape - 10
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Model Compilation
# This is a multi class classification problem
# thus loss function - categorical cross entropy and metrics as accuracy
# Optimizer being used is SGD (Stochastic Gradient Descent)
# lr stands for learning rate
opt = SGD(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
