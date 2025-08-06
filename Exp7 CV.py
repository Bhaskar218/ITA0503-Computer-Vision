import cv2

cap = cv2.VideoCapture(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\fefa2a5e666f4fbdbde0f408da8a0813.mp4")
if not cap.isOpened():
    print("Error: Cannot open video.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
