import cv2

def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\f9f59bfa2cd14338bb0a3416b7d35569.mp4")
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    for frame in reversed(frames):
        out.write(frame)

    cap.release()
    out.release()

reverse_video(
    r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\f9f59bfa2cd14338bb0a3416b7d35569.mp4",
    r"C:\Users\BHASKAR GOWD\Downloads\Bhaskar Mobile\Videos\f9f59bfa2cd14338bb0a3416b7d35569.mp4"
)
