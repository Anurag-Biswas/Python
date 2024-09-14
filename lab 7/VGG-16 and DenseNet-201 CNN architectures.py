import tensorflow as tf
from tensorflow.keras.applications import VGG16, DenseNet201
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Dropout, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import os

# Assuming that you have a breast cancer histopathology dataset in a directory.
# For example, your dataset should be organized as:
# - dataset/
#     - benign/
#     - malignant/
dataset_dir = 'path_to_your_dataset_directory'

# Hyperparameters
img_size = 224  # VGG-16 and DenseNet-201 expect 224x224 images
batch_size = 32
epochs = 10
num_classes = 2  # Binary classification (benign, malignant)

# Data augmentation and preprocessing
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2  # Split 80% training and 20% validation
)

# Load training data
train_generator = datagen.flow_from_directory(
    dataset_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# Load validation data
val_generator = datagen.flow_from_directory(
    dataset_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Define the VGG-16 model
def build_vgg16_model(input_shape=(img_size, img_size, 3), num_classes=num_classes):
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
    # Freeze the base model layers
    for layer in base_model.layers:
        layer.trainable = False

    # Add custom classification layers
    model = base_model.output
    model = Flatten()(model)
    model = Dense(512, activation='relu')(model)
    model = Dropout(0.5)(model)
    model = Dense(num_classes, activation='softmax')(model)
    
    # Create the final model
    model = Model(inputs=base_model.input, outputs=model)
    return model

# Define the DenseNet-201 model
def build_densenet201_model(input_shape=(img_size, img_size, 3), num_classes=num_classes):
    base_model = DenseNet201(weights='imagenet', include_top=False, input_shape=input_shape)
    # Freeze the base model layers
    for layer in base_model.layers:
        layer.trainable = False

    # Add custom classification layers
    model = base_model.output
    model = GlobalAveragePooling2D()(model)
    model = Dense(512, activation='relu')(model)
    model = Dropout(0.5)(model)
    model = Dense(num_classes, activation='softmax')(model)
    
    # Create the final model
    model = Model(inputs=base_model.input, outputs=model)
    return model

# Compile and train the model
def train_model(model, train_generator, val_generator, epochs=epochs):
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=val_generator
    )
    
    return history

# Function to plot accuracy and loss curves
def plot_history(history, model_name):
    plt.figure(figsize=(14, 5))

    # Plot accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title(f'{model_name} - Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    # Plot loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title(f'{model_name} - Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

# Build, train, and evaluate the VGG-16 model
vgg16_model = build_vgg16_model()
vgg16_history = train_model(vgg16_model, train_generator, val_generator)
plot_history(vgg16_history, 'VGG-16')

# Build, train, and evaluate the DenseNet-201 model
densenet201_model = build_densenet201_model()
densenet201_history = train_model(densenet201_model, train_generator, val_generator)
plot_history(densenet201_history, 'DenseNet-201')

# Evaluate models on validation data
vgg16_loss, vgg16_acc = vgg16_model.evaluate(val_generator)
print(f'VGG-16 Validation Accuracy: {vgg16_acc:.4f}')

densenet201_loss, densenet201_acc = densenet201_model.evaluate(val_generator)
print(f'DenseNet-201 Validation Accuracy: {densenet201_acc:.4f}')
