import cv2
from pyzbar.pyzbar import decode

def generate_active_attributes():
    cap = cv2.VideoCapture(1)
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

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            data = obj.data.decode().strip()
            if data == "night":
                active_attributes["night"] = True
            elif data == "cloudy":
                active_attributes["cloudy"] = True
            elif data == "car":
                active_attributes["car"] += 1
            elif data == "electricCars" or data == "electricScooters":
                if data == "electricCars":
                    active_attributes["electricCars"] += 1
                else:
                    active_attributes["electricScooters"] += 1
                if obj.rect.left < frame.shape[1] // 2 and obj.rect.top < frame.shape[0] // 2:
                    if data == "electricCars":
                        active_attributes["chargingElectricCars"] += 1
                    elif data == "electricScooters":
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
