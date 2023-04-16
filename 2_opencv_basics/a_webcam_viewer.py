# import the opencv library, which is called "cv2"
import cv2

# create a webcam object from webcam with id "0"
camera_id = 0
webcam = cv2.VideoCapture(camera_id)

# print some info how to control this program
print("Press q to end this program. Press any other key to see next frame.")

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
    
    # display the received image in a window
    cv2.imshow("My Webcam Window", image)
    
    # wait indefinitely for a key press on the keyboard, if key is pressed, save the key that was pressed in "pressed_key" variable and continue
    pressed_key = cv2.waitKey(0) # TODO: try to change this form 0 to 1 and see what happens.
    
    # if the presed key was the q key, stop the loop
    if pressed_key == ord("q"):
        break
    
    # add 1 to the image counter to count the image
    image_counter = image_counter + 1

# deactivate camera and destroy windows (clean up)
webcam.release()
cv2.destroyAllWindows()