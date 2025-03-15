import tensorflow as tf
import numpy as np
import os
import cv2
from keras import Input
from sklearn.model_selection import train_test_split

Sequential = tf.keras.models.Sequential
Conv2D = tf.keras.layers.Conv2D
MaxPooling2D = tf.keras.layers.MaxPooling2D
Flatten = tf.keras.layers.Flatten
Dense = tf.keras.layers.Dense

def load_data(DATA_DIRECTORY, CATEGORIES, IMG_SIZE):
    images,labels=[],[]

    for category in CATEGORIES:
        # joins path with category
        path = os.path.join(DATA_DIRECTORY,category)
        class_ind = CATEGORIES.index(category)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img = cv2.imread(img_path) # read image
            img = cv2.resize(img,(IMG_SIZE,IMG_SIZE)) # resize image
            img = img / 255.0 # rescale pixel values
            images.append(img)
            labels.append(class_ind)
    # returns a pair of images with their corresponding labels
    return np.array(images),np.array(labels)

def predict_image(image_path, model_path, IMG_SIZE, CATEGORIES):
    model = tf.keras.models.load_model(model_path)
    model.load(model_path)
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)  # add batch dimension

    prediction = model.predict(img)
    class_idx = np.argmax(prediction)
    return CATEGORIES[class_idx]

def train_model(imgs, labels, IMG_SIZE, CATEGORIES):
    model = Sequential([
        Input(shape=(IMG_SIZE, IMG_SIZE, 3)),
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        # filter of size 3x3 continuously moving
        MaxPooling2D(pool_size=(2, 2)),  # better efficiency
        Conv2D(64, (3, 3), activation='relu'),  # 32 -> 64 for more complex patterns
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),  # converts 2D -> 1D
        Dense(128, activation='relu'),
        Dense(len(CATEGORIES), activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    X_train, X_test, y_train, y_test = train_test_split(imgs, labels, test_size=0.2, random_state=42)

    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)
    model.save("trashnet_model.h5")