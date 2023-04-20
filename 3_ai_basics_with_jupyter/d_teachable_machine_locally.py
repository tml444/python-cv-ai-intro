# Train a model here and downlaod it afterwards as "keras" model: https://teachablemachine.withgoogle.com/train/image

import tensorflow as tf
import cv2  # Install opencv-python
import numpy as np

model_dir_relative = "3_ai_basics_with_jupyter/model"
camera_id = 1

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tf.keras.models.load_model(model_dir_relative + "/keras_Model.h5", compile=False)

# Load the labels
class_names = open(model_dir_relative + "/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(camera_id)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()
    image_vis = image.copy()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)



    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    predicted_class = str(class_name[2:]).replace("\n","")
    score = str(np.round(confidence_score * 100))[:-2]
    print("Class:", predicted_class, end="")
    print("Confidence Score:", score, "%")

    # Show the image in a window
    image_vis = cv2.putText(image_vis, f"Class prediction: {predicted_class},   Score: {score}", (30, 30), 0, 1.0, (0, 255, 0), 2)
    cv2.imshow("Webcam Image with classification", image_vis)


    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
