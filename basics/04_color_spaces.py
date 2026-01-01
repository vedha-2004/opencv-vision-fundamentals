import cv2

img_bgr = cv2.imread("assets/images/lena.jpg")

if img_bgr is None:
    raise FileNotFoundError("Image not found")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Convert BGR to Grayscale
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Save results
cv2.imwrite("assets/images/lena_rgb.png", img_rgb)
cv2.imwrite("assets/images/lena_gray_from_bgr.png", img_gray)

print("BGR shape:", img_bgr.shape)
print("RGB shape:", img_rgb.shape)
print("Grayscale shape:", img_gray.shape)
