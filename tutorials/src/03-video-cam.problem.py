# Exercise #3
# -----------
#
# Show camera video and mirror it.

import numpy as np
import cv2

#  Capture webcam image using 'VideoCapture' and store it in the variable 'cap'. Typically, 
# the parameter is 0 for the default camera.
cap=cv2.VideoCapture(0)
#  Get camera image parameters using 'get' on the 'cap' object:
# - width (use 'CAP_PROP_FRAME_WIDTH')
# - height (use 'CAP_PROP_FRAME_HEIGHT')
# - codec (use 'CAP_PROP_CODEC_PIXEL_FORMAT')
# Print the values to the console.
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#  Create a window for the video using 'namedWindow' with the title "Video image".
title="my webcam"
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
#  Start a loop to continuously read frames from the camera using 'while True:'.
while True: 
#  (In loop) Read a camera frame with 'read' and check if that was successful.
 ret, frame=cap.read()
#  (In loop, if successful) (Skip this step for now and implement the display first in order 
 if ret: 
    
# to see the camera image.)
# Create four flipped tiles of the image by first creating an empty image 
# with 'np.zeros'. Then resize the frame to half size using 'cv2.resize' with fx=0.5 and fy=0.5.
# Finally, fill in the four quadrants of the empty image with the original and flipped images
# using 'cv2.flip' with the appropriate flip codes (check the documentation).
 img =np.zeros.like(frame)
 tile= cv2.resize(frame, (0,0), fx=0.5,  fy=0.5)
 img[: title.shape[0], 0: title.shape[1]]= title
#  (In loop, if successful) Display the image.
 cv2.imshow(title,frame)
 key=cv2.waitKey(20)
 if key==ord('q'):
    break
#  (In loop) Check if 'q' is pressed by comparing the return value of 'waitKey' with the 'ord'
# of the letter "q". Use simply 'break' to exit the loop.

# Release the video capture object with 'release' and close the window with 'destroyAllWindows'.
cap.release()
cv2.destroyAllWindows()