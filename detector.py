import cv2
import numpy as np

# 👇 NEW – pull in the helper utilities
from utils import estimate_distance, draw_labelled_box

# Mapping for MobileNet‑SSD classes
CLASS_NAMES = {
    0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'
}

# Load the pre‑trained MobileNet‑SSD model
net = cv2.dnn.readNetFromCaffe(
    'models/MobileNetSSD_deploy.prototxt',
    'models/MobileNetSSD_deploy.caffemodel'
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h,  w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)),
        0.007843,
        (300, 300),
        127.5
    )
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence < 0.5:
            continue

        idx  = int(detections[0, 0, i, 1])
        box  = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        startX, startY, endX, endY = box.astype(int)

        # Draw the label + box via our helper
        draw_labelled_box(frame, startX, startY, endX, endY,
                          CLASS_NAMES.get(idx, 'Unknown'), confidence)

        # Optional: basic distance estimate (shown under the box)
        width_pixels = endX - startX
        dist_m       = estimate_distance(width_pixels)

        if dist_m > 0:
            cv2.putText(
                frame,
                f"{dist_m:.2f} m",
                (startX, endY + 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1
            )

    cv2.imshow("Robotic Vision – Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
