from ultralytics import YOLO


model = YOLO("runs/train/weights/best.pt")


results = model.predict(source="test_images/", save=True)