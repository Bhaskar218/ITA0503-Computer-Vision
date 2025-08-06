import cv2

def detect_vehicles(video_path):
    vehicle_cascade = cv2.CascadeClassifier('cars.xml')  # Make sure this file exists

    if vehicle_cascade.empty():
        print("Failed to load cascade classifier.")
        return

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 2)

        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Vehicle Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Call function with video path
detect_vehicles(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\a213910f443248cf80471584c8c4af1c.mp4")
