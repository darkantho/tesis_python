from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')

if __name__ == '__main__':
    model.train(data='../apple', epochs=4, imgsz=800, device=0)
