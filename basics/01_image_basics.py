import cv2
import numpy as np

img = cv2.imread("assets/images/lena.jpg")

if img is None:
    raise FileNotFoundError("Image not found")

print("Image type:", type(img))
print("Image shape:", img.shape)
print("Image dtype:", img.dtype)

pixel = img[100, 100]
print("Pixel at (100,100) [B,G,R]:", pixel)

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
