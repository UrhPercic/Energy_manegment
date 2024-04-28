import cv2
from pyzbar.pyzbar import decode

def parse_qr_codes():
    cap = cv2.VideoCapture(0)
    active_attributes = {
        "cloudy": False,
        "night": False,
        "oven": False,
        "wind power": False,
        "light": False,
        "car": False,
        "tv": False
    }

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            data = obj.data.decode().lower().strip()
            if data in active_attributes:
                active_attributes[data] = True

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return active_attributes

if __name__ == "__main__":
    attributes = parse_qr_codes()
    print("Active Attributes:", attributes)
