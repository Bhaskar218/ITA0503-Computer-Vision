import cv2
import numpy as np

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg", 0)

if image is None:
    print("Image not found or cannot be opened. Check the path.")
    exit()

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)
sobel = cv2.convertScaleAbs(sobel)

success = cv2.imwrite(r"C:\Users\M.Giri babu\Downloads\sobel.jpg", sobel)
if success:
    print("Sobel image saved successfully.")
else:
    print("Failed to save Sobel image.")

cv2.imshow("Sobel", sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
