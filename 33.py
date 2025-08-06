import cv2
import numpy as np

def create_image_with_rectangle():
    width = 612
    height = 408

    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    top_left = (width // 4, height // 4)
    bottom_right = (width * 3 // 4, height * 3 // 4)

    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 3)

    cv2.imshow("Rectangle on White Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_image_with_rectangle()
