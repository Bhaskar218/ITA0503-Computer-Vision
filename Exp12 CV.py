import cv2

image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
if image is None:
    print("Image not found.")
else:
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    rotated_image = cv2.flip(image, 1)
    cv2.imwrite('rotated_image.jpg', rotated_image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
