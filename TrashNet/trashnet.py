# Importing label data and reading in file
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Using pre-trained model
from keras import Model
from keras import models
from keras.preprocessing import image

# Displaying trash results to user
import matplotlib.pyplot as plt
import numpy as np



# Load in pre-trained model and labels
model_path = "./model_pranav"
model = models.load_model(model_path)

labels_path = "./trashnet_labels.json"
with open(labels_path, 'r') as labels_file:
    labels = json.load(labels_file)
    labels = {int(k):v for k,v in labels.items()}
print(labels)


# Load in image to detect trash
image_path = "./test_images/metal7.jpg"
test_image = image.load_img(image_path, target_size=(300,300))
test_image = image.img_to_array(test_image) / 255.0
plt.figure("Image Preview")
plt.title(image_path)
plt.imshow(test_image.squeeze())
plt.show(block=False)
plt.pause(0.001)


# Run the prediction
prediction = model.predict(test_image[None,:])

predicted_class = labels[np.argmax(prediction[0], axis=-1)]
print("Image Prediction:", predicted_class)
print("Probability: ", np.max(prediction[0], axis=-1))

label_names = list(labels.values())
plt_indices = np.arange(len(label_names))

plt.figure("Results")
plt.bar(plt_indices, prediction[0])
plt.xlabel('Class')
plt.ylabel('Probability')
plt.xticks(plt_indices, label_names)
plt.title(f'Class Probabilities for {image_path}')
plt.show()