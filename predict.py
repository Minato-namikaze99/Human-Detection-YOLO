import io
from PIL import Image, ImageDraw
from flask import Flask, request, jsonify
from ultralytics import YOLO
import base64
import cv2
model = YOLO('yolov8n.pt')
import os
import random

def predict(image_file):
    buffered = io.BytesIO()
    image_bytes = image_file.read()
    img = Image.open(io.BytesIO(image_bytes))
    results = model(img)

    # Creating a copy of the image to draw on
    draw_img = img.copy()
    draw = ImageDraw.Draw(draw_img)

    a = results[0].boxes.cls.tolist().count(0.0)
    b = results[0].boxes.xyxy.tolist()

    #adding boundaries to the image
    for box in b:
       x1, y1, x2, y2 = box  # Extracts box coordinates
       draw.rectangle([x1, y1, x2, y2], outline="red", width=2)


    # Convert the image to base64
    draw_img.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # Saves the image locally
    save_path = "/content/saved_images"

    random_num=random.randrange(100000, 999999)
    img_name = f"image_{random_num}.jpg"
    img_path = os.path.join(save_path, img_name)

    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    draw_img.save(img_path, format="JPEG")


    return {"count": a, "image_path": img_path}

app = Flask(__name__)
@app.route("/objectdetection/", methods=["POST"])
def detect():
    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        results=predict(image_file)
        return jsonify(results)

if __name__ == '__main__':
    app.run()