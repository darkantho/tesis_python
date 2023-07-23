from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')

if __name__ == '__main__':
    model.train(data='apple_dataset', epochs=10, imgsz=800, device=0,workers=4, batch=8)

