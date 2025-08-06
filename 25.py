import cv2

def recognize_watch(template_path, scene_path):
    template = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg", cv2.IMREAD_GRAYSCALE)
    scene = cv2.imread(r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg", cv2.IMREAD_GRAYSCALE)
    
    if template is None or scene is None:
        return

    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(scene, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    result = cv2.drawMatches(template, kp1, scene, kp2, matches[:20], None, flags=2)

    cv2.imshow("Watch Recognition", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

recognize_watch(
    r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg",
    r"C:\Users\BHASKAR GOWD\Downloads\natureimg.jpg"
)
