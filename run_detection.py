from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

video_path = r"C:\Users\Lenovo\OneDrive\Desktop\AI_Drone Survilience\Data\Videos\drone.mp4.mp4"

cap = cv2.VideoCapture(video_path)
print("Checking video path...")
print("Video opened:", cap.isOpened())

# Define restricted zone (rectangle coordinates)
zone_x1, zone_y1 = 900, 200
zone_x2, zone_y2 = 1400, 700

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.25)
    boxes = results[0].boxes

    vehicle_count = 0
    zone_alert = False

    for box in boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        if label in ["car", "truck", "bus", "motorbike"]:
            vehicle_count += 1

            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Check if inside restricted zone
            # Calculate center of object
            # Check overlap between object box and zone
            if not (x2 < zone_x1 or x1 > zone_x2 or y2 < zone_y1 or y1 > zone_y2):
                zone_alert = True

    # Threat level
    if vehicle_count == 0:
        threat = "No Threat"
    elif vehicle_count == 1:
        threat = "Low Threat"
    elif vehicle_count <= 3:
        threat = "Medium Threat"
    else:
        threat = "High Threat"

    annotated_frame = results[0].plot()

    # Draw restricted zone
    cv2.rectangle(annotated_frame, (zone_x1, zone_y1), (zone_x2, zone_y2), (255, 0, 0), 2)

    # Display info
    cv2.putText(annotated_frame, f"Vehicles: {vehicle_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.putText(annotated_frame, f"Threat: {threat}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    if zone_alert:
        cv2.putText(annotated_frame, "ALERT: Object in Restricted Zone!",
                    (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv2.imshow("Drone Surveillance System", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()