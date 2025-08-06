import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Image not found.")
        return

    color = ('b', 'g', 'r')
    plt.figure(figsize=(8, 4))
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()

# 🔁 Call the function with image path
analyze_color_histogram(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg")
