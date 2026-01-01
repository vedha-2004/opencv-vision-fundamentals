import cv2
import os

print("Script started")

# Read images
color_img = cv2.imread("assets/images/lena.jpg", cv2.IMREAD_COLOR)
gray_img = cv2.imread("assets/images/lena.jpg", cv2.IMREAD_GRAYSCALE)

if color_img is None or gray_img is None:
    raise FileNotFoundError("Image not found")

print("Images loaded")

# Write images
color_path = "assets/images/lena_color_copy.jpg"
gray_path = "assets/images/lena_gray.png"

cv2.imwrite(color_path, color_img)
cv2.imwrite(gray_path, gray_img)

print("Images written")

# Verify files exist
print("Color exists:", os.path.exists(color_path))
print("Gray exists:", os.path.exists(gray_path))
