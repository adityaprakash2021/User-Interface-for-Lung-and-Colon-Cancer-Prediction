import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("Model.h5")  # Update with your actual model file

# Define where uploaded images will be stored
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Class labels (update based on your trained model)
class_labels = [
    "Colon Adenocarcinoma", "Colon Benign Tissue", 
    "Lung Adenocarcinoma", "Lung Benign Tissue", 
    "Lung Squamous Cell Carcinoma"
]

# Function to predict image
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Update if needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions for batch processing

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)  # Get class index
    confidence = np.max(predictions)  # Get confidence score

    return {"prediction": class_labels[predicted_class], "confidence": float(confidence)}

# Route for the homepage (handles both GET and POST requests)
@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded", 400
        
        file = request.files["file"]
        if file.filename == "":
            return "No file selected", 400

        # Save uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Get prediction
        result = predict_image(file_path)

        return render_template("result2.html", filename=filename, prediction=result["prediction"], confidence=result["confidence"])

    return render_template("index2.html")

if __name__ == "__main__":
    # Create the upload folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
