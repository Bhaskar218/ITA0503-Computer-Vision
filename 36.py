import cv2
import numpy as np

def subtract_background(image_path):
    image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
    if image is None:
        print("Error: Unable to load image.")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([35, 40, 40])   # Example: green screen lower HSV
    upper_bound = np.array([85, 255, 255]) # Example: green screen upper HSV

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask_inv = cv2.bitwise_not(mask)

    result = cv2.bitwise_and(image, image, mask=mask_inv)

    cv2.imshow("Original Image", image)
    cv2.imshow("Mask (Background)", mask)
    cv2.imshow("Foreground (Background Removed)", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
subtract_background(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
