import cv2
import numpy as np

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
if image is None:
    print("Error: Image not found.")
else:
    h, w = image.shape[:2]
    src_points = np.float32([[0,0], [w,0], [0,h], [w,h]])
    dst_points = np.float32([[w//2,0], [w,0], [w//2,h], [w,h]])
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    rotated = cv2.warpPerspective(image, matrix, (w, h))

    cv2.imshow("Original Image", image)
    cv2.imshow("Y-Axis Rotated Image", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
