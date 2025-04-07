import cv2
import os
from skimage.metrics import structural_similarity
from datetime import datetime
import beepy

def spot_diff(frame1, frame2):
    g1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    g1 = cv2.blur(g1, (3, 3))
    g2 = cv2.blur(g2, (3, 3))

    score, diff = structural_similarity(g1, g2, full=True)
    print(f"Image similarity score: {score:.4f}")

    diff = (diff * 255).astype("uint8")
    _, thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = [c for c in contours if cv2.contourArea(c) > 50]

    if len(contours) > 0:
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 3)

        os.makedirs("stolen", exist_ok=True)
        save_path = f"stolen/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
        cv2.imwrite(save_path, frame1)
        print(f"Image saved at {save_path}")

        # beepy.beep(sound=4)  # Play sound notification
        
        # Display images and wait for user input before closing windows
        cv2.imshow("Difference", thresh)
        cv2.imshow("Detected Changes", frame1)
        
        print("Press any key to continue...")
        cv2.waitKey(0)  
        
        return 1
    else:
        print("No significant differences detected.")
        
        return 0
