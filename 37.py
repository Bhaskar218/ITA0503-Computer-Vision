import cv2
import numpy as np

def subtract_foreground(image_path):
    image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
    if image is None:
        print("Error: Cannot load image.")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_color = np.array([0, 50, 50])     # Example: Red foreground lower HSV
    upper_color = np.array([10, 255, 255])  # Example: Red foreground upper HSV

    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask_inv = cv2.bitwise_not(mask)

    background_only = cv2.bitwise_and(image, image, mask=mask_inv)

    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Mask", mask)
    cv2.imshow("Image without Foreground", background_only)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
subtract_foreground(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
