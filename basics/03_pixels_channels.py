import cv2
import numpy as np

img = cv2.imread("assets/images/lena.jpg")

if img is None:
    raise FileNotFoundError("Image not found")

# Access a pixel
pixel = img[100, 150]
print("Pixel at (y=100, x=150) [B,G,R]:", pixel)

# Modify a pixel (set to red)
img[100, 150] = [0, 0, 255]

# Split channels
b, g, r = cv2.split(img)

print("Blue channel shape:", b.shape)
print("Green channel shape:", g.shape)
print("Red channel shape:", r.shape)

# Zero out blue channel
b_zero = np.zeros_like(b)

# Merge channels (remove blue)
no_blue = cv2.merge((b_zero, g, r))

# Write result
cv2.imwrite("assets/images/lena_no_blue.png", no_blue)
