# Tensorflow_CNN_HAM10000_UI
The application basic by using PyQT5 and Tensorflow to create and detect skincancer. By using the dataset ham 10000 : https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000

More at : https://www.kaggle.com/code/realshaktigupta/skin-cancer-classification-100-accuracy?kernelSessionId=137007336

This Python script implements a simple image classification application using PyQt5 for the graphical user interface (GUI) and TensorFlow for the machine learning model.

Functionality:

Users can browse and select an image file using a file dialog.
The selected image is loaded and preprocessed (resized and converted to a NumPy array) for compatibility with the TensorFlow model.
The loaded TensorFlow Keras model (modelnew.keras) is used to make a prediction on the image.
The prediction is interpreted using pre-defined class labels (labels) to identify the most likely class.
The original image is displayed in the graphicsView widget.
The predicted class and the original file name are displayed in the label widget.
Key Dependencies:

PyQt5 (for GUI development)
TensorFlow (for machine learning model)
NumPy (for numerical computations)
Matplotlib (optional, potentially used for future visualizations)
Usage:

Ensure you have the required dependencies installed (pip install PyQt5 tensorflow numpy matplotlib).
Place the script (predict_app.py) and the TensorFlow model (modelnew.keras) in the same directory.
Run the script using python predict_app.py.
Select an image file through the file dialog.
The application will display the image, predicted class, and file name.
Notes:

Replace 'modelnew.keras' with the actual filename of your trained model if it differs.
Modify the labels list if your model predicts different classes.
Consider adding error handling for cases like invalid file paths or unsupported image formats.
You may explore integrating a progress bar or visual cues during image processing.
Future Considerations:

Implement confidence scores alongside predicted classes.
Enhance the UI with additional widgets or functionalities.
Explore saving prediction results to a file or database.







"Learning neural network on different numbers of pictures in each class(like class 1 =8000 images and other 6 classes ~100 images each) is bad because your neural network learn to predict only one class. It leads to wrong evaluate metrics. In other way if you create a lot new pictures from "Data generator" you increase learning time. Maybe if you create more epoch you can get more accurate model. But as i see the validation accuracy decreas by second epoch."
Get more in : https://github.com/PawelKinczyk/TensorFlow-Neural-network-on-HAM10000-dataset/tree/main 
https://www.youtube.com/watch?v=fyZ9Rxpoz2I

