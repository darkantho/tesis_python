from ultralytics import YOLO


model = YOLO("../runs/classify/train8/weights/best.pt")


model.predict(source="0", show=True)