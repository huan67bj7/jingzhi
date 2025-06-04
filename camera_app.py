import cv2


def run_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to open camera")
        return
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break
            cv2.imshow('Camera', frame)
            # Press q to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    run_camera()
