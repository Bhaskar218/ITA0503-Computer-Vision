import cv2
import numpy as np

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")

if image is None:
    print("Image not found. Check the path.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    image[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow("Harris Corners", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(r"C:\Users\M.Giri babu\Downloads\harris_corners.jpg", image)
