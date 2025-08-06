import cv2

def count_faces(image_path):
    image = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
    if image is None:
        print("Error: Unable to load image.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    face_count = len(faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    print(f"Number of faces detected: {face_count}")
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
count_faces(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
