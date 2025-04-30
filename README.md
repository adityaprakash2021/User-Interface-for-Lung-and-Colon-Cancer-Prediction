# 🧠 Lung and Colon Cancer Image Classification Web App

This project is a deep learning-powered Flask web application for predicting and classifying lung and colon cancer types from histopathological images. It uses a trained Convolutional Neural Network (CNN) to classify uploaded images into one of five categories.

> 🖥️ The application is deployed and hosted on an **AWS EC2** instance.

---

## 🔬 Cancer Types Detected
The model predicts the following classes:
- **Colon Adenocarcinoma**
- **Colon Benign Tissue**
- **Lung Adenocarcinoma**
- **Lung Benign Tissue**
- **Lung Squamous Cell Carcinoma**

---

## 📁 Project Structure
cancer-detection-flask/
├── backend.py                 # Main Flask application
├── Model.h5                   # Trained Keras CNN model
├── cancer.ipynb               # Jupyter Notebook for training/evaluation (optional)
├── templates/                 # HTML templates rendered by Flask
│   ├── index2.html            # Homepage for image upload
│   └── result2.html           # Prediction result display page
├── static/
│   └── uploads/               # Folder to store uploaded images
├── requirements.txt           # List of Python dependencies (to be generated)
└── README.md                  # Project documentation (this file)

## 💡 Features
- 🧠 Predicts 5 classes of lung and colon cancer from image input
- 🖼️ Drag-and-drop style web interface for easy image upload
- ⚡ Real-time prediction and confidence score
- ☁️ Hosted on AWS EC2 for scalable access

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/adityaprakash2021/cancer-detection-flask.git
   cd cancer-detection-flask
2. Set up a Python environment
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
4. Run the Flask application
   python backend.py
5. Open your browser and go to:
   http://127.0.0.1:5000


☁️ Deployment on AWS EC2
The app is deployed on an Amazon EC2 instance running a Python environment. The Flask app is run using gunicorn or directly with python backend.py behind an Nginx reverse proxy (optional for production).

Basic EC2 Steps:

Launch a new Ubuntu EC2 instance

SCP your project files or use Git to clone

Install Python and dependencies
Run the app using Flask
Open port 5000 in EC2 security group for browser access

📦 Dependencies
Install using pip install -r requirements.txt (create this file with the below if not already present):
Flask
tensorflow
numpy
Pillow

