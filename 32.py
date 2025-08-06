import numpy as np
import cv2

def create_colored_corner_boxes(width, height):
    image = np.ones((25, 15, 3), dtype=np.uint8) * 255

    box_w, box_h = width // 10, height // 10

    image[0:box_h, 0:box_w] = [0, 0, 0]           # Top-left: Black
    image[0:box_h, -box_w:] = [255, 0, 0]         # Top-right: Blue
    image[-box_h:, 0:box_w] = [0, 255, 0]         # Bottom-left: Green
    image[-box_h:, -box_w:] = [0, 0, 255]         # Bottom-right: Red

    cv2.imshow("Corner Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
create_colored_corner_boxes(500, 400)
