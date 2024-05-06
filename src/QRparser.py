import cv2
from pyzbar.pyzbar import decode

def generate_active_attributes():
    cap = cv2.VideoCapture(0)
    active_attributes = {
        "cloudy": False,
        "night": False,
        "car": 0,
        "electricCars": 0,
        "electricScooters": 0,
        "chargingElectricCars": 0,
        "chargingElectricScooters": 0,
    }

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        active_attributes["cloudy"] = False
        active_attributes["night"] = False

        active_attributes["car"] = 0
        active_attributes["electricCars"] = 0
        active_attributes["electricScooters"] = 0
        active_attributes["chargingElectricCars"] = 0
        active_attributes["chargingElectricScooters"] = 0

        height, width, _ = frame.shape
        top_left_corner = frame[:height//2, :width//2]
        top_right_corner = frame[:height//2, width//2:]
        bottom_left_corner = frame[height//2:, :width//2]
        bottom_right_corner = frame[height//2:, width//2:]

        for corner_frame in [top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner]:
            decoded_objects = decode(corner_frame)
            for obj in decoded_objects:
                data = obj.data.decode().lower().strip()
                if data == "car":
                    active_attributes["car"] += 1
                elif data == "electriccar":
                    active_attributes["electricCars"] += 1
                elif data == "electricscooter":
                    active_attributes["electricScooters"] += 1

        if active_attributes["electricCars"] > 0:
            active_attributes["chargingElectricCars"] += 1
        if active_attributes["electricScooters"] > 0:
            active_attributes["chargingElectricScooters"] += 1

        yield active_attributes

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    for attributes in generate_active_attributes():
        print("Active Attributes:", attributes)
