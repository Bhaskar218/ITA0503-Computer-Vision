import cv2

def play_reverse_slow(video_path, slow_factor=2):
    cap = cv2.VideoCapture(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\a213910f443248cf80471584c8c4af1c.mp4")
    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frames = []
    for _ in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)
        if cv2.waitKey(40 * slow_factor) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
play_reverse_slow(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\a213910f443248cf80471584c8c4af1c.mp4", slow_factor=3)
