from roboflow import Roboflow

f = open("key.txt", "r")

rf = Roboflow(api_key=f.read())
project = rf.workspace("hophacks").project("surgical-tool-detection-cx3g7")
model = project.version(1).model

model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")