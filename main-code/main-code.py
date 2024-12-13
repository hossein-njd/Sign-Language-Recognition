import cv2
import numpy as np
from ultralytics import YOLO

# بارگذاری مدل از پیش آموزش دیده YOLOv8
model = YOLO("path_to_your_trained_model.pt")

# تابع برای تبدیل نتایج مدل به حروف
LABELS = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
    8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V',
    22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
}

def predict_letter(frame):
    results = model(frame)
    letter = None

    for result in results:
        # استخراج کلاس با بالاترین احتمال
        for box in result.boxes:
            cls = int(box.cls[0])
            letter = LABELS.get(cls, "")
            return letter

    return None

# شروع از دوربین وب‌کم
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame from webcam.")
        break

    # پیش‌بینی حرف از تصویر دوربین
    letter = predict_letter(frame)

    # نمایش حرف پیش‌بینی شده روی تصویر
    if letter:
        cv2.putText(frame, f"Predicted Letter: {letter}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # نمایش تصویر
    cv2.imshow("ASL Recognition", frame)

    # خروج با زدن کلید 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
