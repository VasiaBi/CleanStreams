from djitellopy import Tello
import droneconnect, dronequit

import cv2
import math
import time

# Connect with drone
tello = droneconnect.drone_connect()

# Start video stream
def stream_on():
    tello.streamon()
    # print("Video stream started") to test if it works

    while True:
        # Get the video frame
        frame = tello.get_frame_read().frame

        # Resize the frame - replace application window dimensions here
        frame = cv2.resize(frame, (640, 480))

        # Display the frame  
        cv2.imshow(frame)

       # How can we return this to frontend? Screen 4a

def stream_off():
    tello.streamoff()
    # print("Video stream stopped") to test if it works
    
    cv2.destroyAllWindows()
