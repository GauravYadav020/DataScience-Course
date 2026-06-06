# M21 Lesson 4 – Image Classifier using CNN – Part 2
# Short Description: Completing the CNN image classifier and training it.

# Activity 1
# Goal: Add fully connected layers and output layer to the CNN.
# Summary: Flatten features and add Dense layers for classification.

# 1. Install required library
!pip install np_utils

# 2. Import required libraries
from google.colab import files
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from numpy import argmax
from keras.models import load_model

# 3. Upload image
print("Step 1: Please upload an image.")

file = files.upload()

filename = list(file.keys())[0]

print("Image uploaded successfully!")
print("Uploaded image file:", filename)

# 4. Create image preparation function
print("Step 2: Image preparation function is ready.")

def load_image(filename):
    print("Loading image...")

    # 5. Load the image and resize it to 32x32
    img = load_img(filename, target_size=(32, 32))

    print("Image loaded successfully.")
    print("Resizing image to 32x32 pixels...")

    # 6. Convert image to array
    img = img_to_array(img)
    print("Image converted into number format.")

    # 7. Reshape image for the model
    img = img.reshape(1, 32, 32, 3)
    print("Image reshaped for the model.")

    # 8. Normalize image, same as training data
    img = img.astype('float32')
    img = img / 255.0
    print("Image normalized successfully.")

    return img

# 9. Prepare prediction code
print("Step 3: Prediction code is ready.")

def run_example():
    print("Preparing the uploaded image for prediction...")

    # 10. Load the uploaded image automatically
    img = load_image(filename)

    print("Loading trained model...")

    # 11. Load model
    model = load_model('classifier.h5')

    print("Model loaded successfully.")
    print("Predicting the image class...")

    # 12. Predict the class
    result = model.predict(img)

    print("Prediction completed successfully!")
    print("Prediction probabilities:")
    print(result)

    # 13. Get class with highest probability
    predicted_class = argmax(result)

    print("Final predicted class:")

    # 14. Print the predicted class name
    if predicted_class == 0:
        print('Airplane')
    elif predicted_class == 1:
        print('Automobile')
    elif predicted_class == 2:
        print('Bird')
    elif predicted_class == 3:
        print('Cat')
    elif predicted_class == 4:
        print('Deer')
    elif predicted_class == 5:
        print('Dog')
    elif predicted_class == 6:
        print('Frog')
    elif predicted_class == 7:
        print('Horse')
    elif predicted_class == 8:
        print('Ship')
    elif predicted_class == 9:
        print('Truck')

# 15. Entry point, run the example
run_example()