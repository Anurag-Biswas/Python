import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from tensorflow.keras.datasets import emnist

# Load the EMNIST dataset (letters subset)
# This requires TensorFlow installed and an internet connection to download the dataset
(x_train, y_train), (x_test, y_test) = emnist.load_data(type='letters')

# The images are 28x28 grayscale images
print(f"Training data shape: {x_train.shape}")
print(f"Training labels shape: {y_train.shape}")

# Preprocessing: Flatten the 28x28 images into 1D vectors
x_train_flat = x_train.reshape(x_train.shape[0], -1).astype('float32') / 255.0
x_test_flat = x_test.reshape(x_test.shape[0], -1).astype('float32') / 255.0

# Labels: The EMNIST dataset labels start at 1 (A = 1, B = 2, ..., Z = 26).
# To make it zero-indexed, we'll subtract 1 from the labels.
y_train -= 1
y_test -= 1

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x_train_flat, y_train, test_size=0.2, random_state=42)

# Create an SVM classifier
clf = svm.SVC(kernel='linear', gamma='auto')

# Train the classifier on the training set
clf.fit(X_train, y_train)

# Predict the test set results
y_pred = clf.predict(X_test)

# Evaluate the classifier performance
print("Classification report for SVM classifier:\n", metrics.classification_report(y_test, y_pred))
print("Confusion matrix:\n", metrics.confusion_matrix(y_test, y_pred))

# Plot some of the test images with their predicted labels
plt.figure(figsize=(10, 6))
for index, (image, prediction) in enumerate(zip(X_test[:10], y_pred[:10])):
    plt.subplot(2, 5, index + 1)
    plt.axis('off')
    plt.imshow(image.reshape(28, 28), cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title(f'Pred: {chr(prediction + ord("A"))}')
plt.show()
