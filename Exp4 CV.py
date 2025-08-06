import cv2

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")

if image is None:
    print("Error: Image not found. Check the file path.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    cv2.imshow("Original Grayscale Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
