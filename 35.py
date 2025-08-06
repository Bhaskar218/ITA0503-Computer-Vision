import cv2
import numpy as np

def draw_text_on_image(image_path=None):
    text = input("hello")

    if image_path:
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Cannot load image.")
            return
    else:
        image = np.ones((400, 600, 3), dtype=np.uint8) * 255

    position = (50, 200)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 0, 255)
    thickness = 2

    cv2.putText(image, text, position, font, font_scale, color, thickness)

    cv2.imshow("Image with Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

draw_text_on_image()
