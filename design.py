from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PredictForm(object):
    def setupUi(self, PredictForm):
        PredictForm.setObjectName("PredictForm")
        PredictForm.resize(1100, 600)
        self.centralwidget = QtWidgets.QWidget(PredictForm)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 650, 500))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 30, 400 , 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.predictButton = QtWidgets.QPushButton(self.centralwidget)
        self.predictButton.setGeometry(QtCore.QRect(800, 150, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(100)
        self.predictButton.setFont(font)
        self.predictButton.setObjectName("predictButton")
        PredictForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(PredictForm)
        QtCore.QMetaObject.connectSlotsByName(PredictForm)

    def retranslateUi(self, PredictForm):
        _translate = QtCore.QCoreApplication.translate
        PredictForm.setWindowTitle(_translate("PredictForm", "Skin Cancer Prediction"))
        self.label.setText(_translate("PredictForm", "Prediction Result  "))
        self.predictButton.setText(_translate("PredictForm", "Predict"))
