import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Simulated gait data (replace this with actual dataset loading)
# Assuming gait dataset contains sequences of images (frames) for each individual walking

# Example of synthetic data with 100 samples, each sample being a sequence of 20 frames (64x64 grayscale images)
num_samples = 100
sequence_length = 20
image_height, image_width, channels = 64, 64, 1  # Grayscale images
num_classes = 10  # Assume we have 10 different persons to classify

# Random synthetic data generation (replace with actual dataset)
X_data = np.random.rand(num_samples, sequence_length, image_height, image_width, channels).astype('float32')
y_data = np.random.randint(0, num_classes, num_samples)

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)

# One-hot encoding the labels
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)

# Building the CRNN model (Convolutional Recurrent Neural Network)
model = models.Sequential()

# CNN block to extract spatial features from each frame
model.add(layers.TimeDistributed(layers.Conv2D(32, (3, 3), activation='relu', padding='same'), 
                                 input_shape=(sequence_length, image_height, image_width, channels)))
model.add(layers.TimeDistributed(layers.MaxPooling2D((2, 2))))
model.add(layers.TimeDistributed(layers.Conv2D(64, (3, 3), activation='relu', padding='same')))
model.add(layers.TimeDistributed(layers.MaxPooling2D((2, 2))))
model.add(layers.TimeDistributed(layers.Conv2D(128, (3, 3), activation='relu', padding='same')))
model.add(layers.TimeDistributed(layers.MaxPooling2D((2, 2))))
model.add(layers.TimeDistributed(layers.Flatten()))  # Flatten each frame's features

# RNN block to capture temporal patterns in the walking sequence
model.add(layers.LSTM(128, return_sequences=False))

# Fully connected layer
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))

# Output layer with softmax for multi-class classification
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=16, validation_data=(X_test, y_test))

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.2f}")

# Plot training & validation accuracy values
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

# Plot training & validation loss values
plt.figure(figsize=(8, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
