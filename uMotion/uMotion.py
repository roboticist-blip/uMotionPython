import cv2
import numpy as np

MODE_SUMMARY = 0
MODE_RAW = 1

class uMotion:
    def __init__(self, camera_index=0, width=160, height=120):
        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.width = width
        self.height = height
        self.mode = MODE_SUMMARY
        self.threshold = 10
        self.prev_frame = None
        self.motion_pixels = 0
        self.motion_ratio = 0.0

    def set_mode(self, mode):
        self.mode = mode

    def set_threshold(self, threshold):
        self.threshold = threshold

    def update(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if self.prev_frame is None:
            self.prev_frame = gray
            return

        diff = cv2.absdiff(gray, self.prev_frame)
        motion_mask = diff > self.threshold

        self.motion_pixels = np.sum(motion_mask)
        self.motion_ratio = self.motion_pixels / (self.width * self.height)

        if self.mode == MODE_RAW:
            # Print ASCII visualization
            for row in motion_mask:
                line = "".join(['.' if pix else ' ' for pix in row])
                print(line)
            print("-" * 40)
        else:
            print(f"Motion pixels={self.motion_pixels}, ratio={self.motion_ratio:.4f}")

        self.prev_frame = gray

    def motion_detected(self):
        return self.motion_pixels > self.threshold

    def release(self):
        self.cap.release()
