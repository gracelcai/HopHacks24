from ultralytics import YOLO
from roboflow import Roboflow

f = open("key.txt", "r")
rf = Roboflow(api_key=f.read())
f.close()
project = rf.workspace("hophacks").project("surgical-tool-detection-cx3g7")
version = project.version(1)
dataset = version.download("yolov8")

model = YOLO("yolov8n.pt")
# model.train(resume=True)
model.train(data="dataset/data.yaml", epochs=300, device="mps", plots=True, verbose=True)