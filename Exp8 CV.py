import cv2
import numpy as np

image = cv2.imread( r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
if image is None:
    print("Error: Image not found.")
else:
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(image, kernel, iterations=1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
