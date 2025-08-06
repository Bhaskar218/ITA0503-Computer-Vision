import cv2
import numpy as np

def create_image_with_circle():
    width = 612
    height = 408

    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    center = (width // 2, height // 2)
    radius = min(width, height) // 4

    cv2.circle(image, center, radius, (0, 255, 0), 3)

    cv2.imshow("Circle on White Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_image_with_circle()
