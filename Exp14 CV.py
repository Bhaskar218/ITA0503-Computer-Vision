import cv2
import numpy as np

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")

if image is None:
    print("Image not loaded. Check the path.")
else:
    rows, cols = image.shape[:2]
    pts1 = np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]])
    pts2 = np.float32([[50,50], [cols-100,50], [100,rows-100], [cols-150,rows-150]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(image, matrix, (cols, rows))

    cv2.imshow("Perspective Transform", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(r"C:\Users\M.Giri babu\Downloads\perspective.jpg", result)
