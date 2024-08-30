from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.datasets import mnist
from keras.utils import to_categorical
import pandas as pd
import requests 
import os
import mlflow
from mlflow.keras import log_model, save_model, autolog
from mlflow.models.signature import infer_signature

mlflow.set_experiment("MLtestped MNIST")
#mlflow.set_tracking_uri("/home/ubuntu/notebooks/gradio/mlruns")
mlflow.tensorflow.autolog(every_n_iter=1)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess the data
X_train = X_train / 255.
X_test = X_test / 255.
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Define the model
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=1, validation_data=(X_test, y_test))

# Sign the signature
signature = infer_signature(X_train, model.predict(X_test))

# Save the model
model.save('mnist_model_5epochs.h5')

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print('\nTest accuracy:', test_acc)

mlflow.tensorflow.log_model(model, "mnist_tensorflow_malli", signature=signature)

