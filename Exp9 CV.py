import cv2

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
if image is None:
    print("Error: Image not found.")
else:
    smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    bigger = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

    cv2.imshow("Original Image", image)
    cv2.imshow("Smaller Image", smaller)
    cv2.imshow("Bigger Image", bigger)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
