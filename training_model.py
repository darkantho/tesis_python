from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')

if __name__ == '__main__':
    model.train(data='C:/Users/sabina/Documents/tesis_python/dataset', epochs=4, imgsz=800, device=0)
