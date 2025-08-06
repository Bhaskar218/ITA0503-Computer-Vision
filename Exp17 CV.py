import cv2

image = cv2.imread(r"C:\Users\M.Giri babu\Downloads\Insbright.jpeg")
if image is None:
    print("Image not found.")
    exit()

roi = image[50:150, 100:200]
image[200:300, 300:400] = roi

cv2.imshow('ROI Copy-Paste', image)
cv2.imwrite('roi_result.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
