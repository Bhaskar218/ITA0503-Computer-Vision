import cv2

def detect_vehicles(video_path):
    cap = cv2.VideoCapture(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\a213910f443248cf80471584c8c4af1c.mp4")
    car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_car.xml")

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Vehicle Detection", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
