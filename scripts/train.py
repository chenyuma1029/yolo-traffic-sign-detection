from ultralytics import YOLO

def main():
    model = YOLO("yolo11n.pt") 
    
   
    results = model.train(
        data="indicator.yaml", 
        epochs=100, 
        imgsz=640, 
        device="mps"
    )

if __name__ == "__main__":
    main()