# import the opencv library, which is called "cv2"
import cv2
import mediapipe

# initialize hand detector from mediapipe
hand_detector = mediapipe.solutions.hands.Hands()

# create a webcam object from webcam with id "0"
camera_id = 0
webcam = cv2.VideoCapture(camera_id)

# print some info how to control this program
print("Press q to end this program.")

# setup a image_counter to count the amount of images displayed
image_counter = 0

# start a while loop that runs as long as it's condition is "TRUE". In this case it will run infinitely if not stopped with "break"
while True:
    
    # try to get an image from the webcam, if this try was successful, it will be saved in the variable "success"  and the image is saved in "image"
    success, image = webcam.read()
    
    # print info about success if image read
    print("Image successfully received? ->", success)
    
    # stop the loop ("break") if the image was not successfully received, so the variable success is "False"
    if success == False:
        break
    
    # print current counter value
    print("Show image nr.", image_counter)
    
    # detect hand using ai (with mediapipe library)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hand_detector.process(image_rgb)
    print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            mediapipe.solutions.drawing_utils.draw_landmarks(image_rgb, hand_landmarks)
    
    # display the received image in a window
    cv2.imshow("My Webcam Window", image)
    cv2.imshow("Hand detector", image_rgb)
    
    # wait indefinitely for a key press on the keyboard, if key is pressed, save the key that was pressed in "pressed_key" variable and continue
    pressed_key = cv2.waitKey(1)
    
    # if the presed key was the q key, stop the loop
    if pressed_key == ord("q"):
        break
    
    # add 1 to the image counter to count the image
    image_counter = image_counter + 1


# deactivate camera and destroy windows (clean up)
webcam.release()
cv2.destroyAllWindows()