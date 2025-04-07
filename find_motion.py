import cv2
from spot_diff import spot_diff
import time
import numpy as np

def find_motion():
    motion_detected = False
    is_start_done = False

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    print("Waiting for 2 seconds...")
    time.sleep(2)

    ret, frame1 = cap.read()
    if not ret:
        print("Error: Failed to capture initial frame")
        cap.release()
        return

    frm1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frm2 = cap.read()
        if not ret:
            print("Error: Failed to capture subsequent frame")
            break

        frm2_gray = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(frm1, frm2_gray)
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = [c for c in contours if cv2.contourArea(c) > 25]

        if len(contours) > 5:
            cv2.putText(thresh, "Motion Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2)
            motion_detected = True
            is_start_done = False

        elif motion_detected and len(contours) < 3:
            if not is_start_done:
                start_time = time.time()
                is_start_done = True

            elapsed_time = time.time() - start_time
            if elapsed_time > 4:
                ret, frame2 = cap.read()
                if not ret:
                    print("Error: Failed to capture frame for spot_diff")
                    break

                result = spot_diff(frame1, frame2)
                if result == 0:
                    print("No significant motion detected. Restarting...")
                    # Reset flags and continue monitoring
                    motion_detected = False
                    is_start_done = False
                else:
                    print("Motion detected and differences saved.")
                    # Reset flags and continue monitoring
                    motion_detected = False
                    is_start_done = False

        else:
            cv2.putText(thresh, "No Motion Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2)

        cv2.imshow("Motion Detection", thresh)
        frm1 = frm2_gray.copy()

        if cv2.waitKey(1) == 27:  # Exit on pressing 'Esc'
            break

    cap.release()
    cv2.destroyAllWindows()
