from ultralytics import YOLO


model = YOLO("runs/classify/train20/weights/best.pt")


model.predict(source="0", show=True)