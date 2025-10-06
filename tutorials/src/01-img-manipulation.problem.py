# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

#  First step is to 'import' the opencv module which is called 'cv2'.
import cv2

#  Check the opencv version and display it with 'print'.
print(cv2.__version__)

#  Load an image with image reading modes using 'imread'.
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.
img = cv2.imread("tutorials/data/images/logo.png")

# Check if image is loaded fine and raise a FileNotFoundError if not.
if img is None: 
    raise FileNotFoundError("image file not found")

# Resize image with 'resize'.
#Bild, nichtg Fenster skalieren 
image=cv2.resize(img,None,fx=0.5, fy=0.5)

#  Rotate image (but keep it rectangular) with 'rotate'.
img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


# Save image with 'imwrite'.
#braucht valide Dateinamenserweiterung (png,gif...)
cv2.imwrite("output.jpg", img)

#  Show the image with 'imshow'.
cv2.imshow("my image", img)

#  Avoid the immediate closing of the image window with 'waitKey'.
# warten bis key gedrueckt
cv2.waitKey(0)
