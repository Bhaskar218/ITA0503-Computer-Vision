import cv2

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")  # Replace with your actual image path
if image is None:
    print("Image not loaded. Check the path.")
    exit()

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
