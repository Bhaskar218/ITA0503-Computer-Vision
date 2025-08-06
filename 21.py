import cv2
import numpy as np

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg", 0)

if image is None:
    print("Image not found.")
    exit()

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original", binary)
cv2.imshow("Opened Image", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Users\P S PAVAN KUMAR\Downloads\opened.jpg", opening)
