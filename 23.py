import cv2
import numpy as np

def morphological_tophat(image_path):
    image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        return
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    tophat_image = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Top Hat Result", tophat_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

morphological_tophat(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
