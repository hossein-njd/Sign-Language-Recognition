import cv2
from pynput import keyboard
import os

def main():
    # پوشه ذخیره عکس‌ها
    save_dir = "captured_images"
    os.makedirs(save_dir, exist_ok=True)

    # دسترسی به وب‌کم
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access the camera")
        return

    print("Press the M key to capture an image. Press ESC to exit.")

    img_counter = 0

    def on_press(key):
        nonlocal img_counter
        try:
            if key.char == "m":
                ret, frame = cap.read()
                if ret:
                    img_name = os.path.join(save_dir, f"image_{img_counter}.png")
                    cv2.imwrite(img_name, frame)
                    print(f"Image saved: {img_name}")
                    img_counter += 1

        except AttributeError:
            if key == keyboard.Key.esc:
                print("Exiting...")
                return False

    with keyboard.Listener(on_press=on_press) as listener:
        while listener.running:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == 27:  # Check for ESC key in OpenCV window
                break

    # آزاد کردن منابع
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

## این بنامه هربار که ام را وارد کنی یک عکس میگیرد و عکس رو در یک فایل زخیره میکند