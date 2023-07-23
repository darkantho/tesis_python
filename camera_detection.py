from ultralytics import YOLO
import cv2
import supervision as sv
import argparse
import numpy as np
from ultralytics.utils.plotting import Annotator
import winsound


def main():

    frame_width, frame_height = 800, 800

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("runs/classify/train20/weights/last.pt")

    while True:

        _, frame = cap.read()

        results = model(frame, agnostic_nms=True)[0]

        probabilidad_normal = results.probs.data[2].item()

        print(f'Prob de manzana Buena:{probabilidad_normal}')


        if probabilidad_normal > 0.55:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

        cv2.imshow("Sistema Deteccion Manzanas", frame)



        if (cv2.waitKey(30) == 27):
            break





if __name__ == '__main__':
    main()