import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\a213910f443248cf80471584c8c4af1c.mp4")
    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)

        print(f"Frame {frame_number}:")
        print(text.strip())
        print("-" * 50)

        frame_number += 1

    cap.release()

# Call the function
extract_text_from_video(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\a213910f443248cf80471584c8c4af1c.mp4")
