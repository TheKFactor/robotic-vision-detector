# utils.py

import cv2
import numpy as np

# Assumes average height of object and focal length to calculate distance
# You can calibrate this later
KNOWN_WIDTH = 0.5  # meters (e.g., average human head width)
FOCAL_LENGTH = 615  # in pixels (adjust per camera)

def estimate_distance(box_width_pixels):
    if box_width_pixels == 0:
        return -1
    return (KNOWN_WIDTH * FOCAL_LENGTH) / box_width_pixels

def draw_labelled_box(frame, startX, startY, endX, endY, label, confidence):
    box_color = (23, 230, 210)
    label_text = f"{label}: {confidence:.2f}"

    cv2.rectangle(frame, (startX, startY), (endX, endY), box_color, 2)
    cv2.putText(frame, label_text, (startX, startY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
