# Tutorial #6
# -----------
#
# Playing around with colors. We convert some values from RGB to HSV and then find colored objects in the image and mask
# them out. Includes a color picker on double-click now. The RGB version is meant to demonstrate that this does not work
# in RGB color space.

import numpy as np
import cv2

# Print keyboard usage
print("This is a HSV color detection demo. Use the keys to adjust the \
selection color in HSV space. Circle in bottom left.")
print("The masked image shows only the pixels with the given HSV color within \
a given range.")
print("Use h/H to de-/increase the hue.")
print("Use s/S to de-/increase the saturation.")
print("Use v/V to de-/increase the (brightness) value.\n")
print("Double-click an image pixel to select its color for masking.")

# Capture webcam image
cap = cv2.VideoCapture(0)

# Get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))

print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Codec = " + str(codec))

# Drawing helper variables
thick = 10
thin = 3
thinner = 2
font_size_large = 3
font_size_small = 1
font_size_smaller = 0.6
font = cv2.FONT_HERSHEY_SIMPLEX

# Define  RGB colors as variables
red= 100
green=0
blue=255

# Exemplary color conversion (only for the class), tests usage of cv2.cvtColor

# Enter some default values and uncomment
hue = 10
hue_range = 10
saturation =100
saturation_range = 100
value =100
value_range = 100


# Callback to pick the color on double click
def color_picker(event, x, y, flags, param):
    global hue, saturation, value
    if event == cv2.EVENT_LBUTTONDBLCLK:
        (h, s, v) = hsv[y, x]
        hue = int(h)
        saturation = int(s)
        value = int(v)
        print("New color selected:", (hue, saturation, value))


while True:
    # Get video frame (always BGR format!)
    ret, frame = cap.read()
    if ret:
        # Copy image to draw on
        img = frame.copy()

        #  Compute color ranges for display
        lower_color=np.array([hue-hue_range,saturation - saturation_range, value - value_range])
        upper_color=np.array([hue + hue_range, saturation + saturation_range, value + value_range])

        # TODO Draw selection color circle and text for HSV values
        img=cv2.circle (img, (width-80,height-80),30,(blue,green,red)-1)
        img=cv2.putText(img, "H=" +str(hue), (width - 200, height - 75),font,font_size_small,red,thin)
        img=cv2.putText(img, "S=" +str(saturation), (width - 200, height - 75) font,font_size_small,red,thin)
        img=cv2.putText(img, "V=" +str(value), (width - 200, height - 75)font,font_size_small,red,thin)

        # TODO Convert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

        # TODO Create a bitwise mask
        mask=cv2.inRange( hsv, lower_color,upper_color )

        # TODO Apply mask
        masked=cv2.bitwise_and(img,img,mask=mask )

        # TODO Show the original image with drawings in one window
        cv2.imshow("original",img)

        # TODO Show the masked image in another window
        cv2.imshow("masked",masked)

        # TODO Show the mask image in another window
        cv2.imshow("mask",mask)

        # TODO Deal with keyboard input

    else:
        print("Could not start video camera")
        break

cap.release()
cv2.destroyAllWindows()
