from roboflow import Roboflow

f = open("key.txt", "r")

rf = Roboflow(api_key=f.read())
project = rf.workspace("hophack3").project("tool-detection-br4z6")
model = project.version(2).model

model.predict("clips/clip2.mp4", confidence=40, overlap=30).save("prediction.mp4")