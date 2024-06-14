import sys
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QFileDialog
from tensorflow.keras.models import load_model
import os

from design import Ui_PredictForm  # Replace with the actual name of your UI Python file

class PredictApp(QMainWindow, Ui_PredictForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.predictButton.clicked.connect(self.predict_from_ui)

    def predict_from_ui(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Image Files (*.jpg *.jpeg *.png *.bmp)')
        if file_path:
            self.Predict(file_path)

    def Predict(self, image_path):
        
        model_load = load_model('modelnew.keras')

        # Example of making a prediction with the loaded 
        img_width, img_height = 224, 224
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(img_width, img_height))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        prediction = model_load.predict(img)
        print("Prediction:", prediction)


        # Xây dựng nhãn cho kết quả dự đoán
        labels = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
        predicted_labels = labels[np.argmax(prediction)]

        # Display the image
        pixmap = QPixmap(image_path)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView.setScene(scene)

         # Get the file name from the path
        file_name = os.path.basename(image_path)
        
        # Display the prediction result including the file name
        self.label.setText(f"File: {file_name}\n Predicted: {predicted_labels}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PredictApp()
    window.show()
    sys.exit(app.exec_())
