import numpy as np
from keras.models import load_model
new_model=load_model('fin.f5')
new_model.summary()
new_model.get_weights()
new_model.optimizer


def new(region,month,year):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my_application")
    location = geolocator.geocode(region)
    latitude=location.latitude
    longitude=location.longitude
    depth=round(np.random.uniform(low=10,high=500),2)
    mag=round(np.random.uniform(low=0.0,high=9.5),2)
    res=np.array([[latitude,longitude,depth,month,year,mag]])
    print(res,res.shape)
    y_pred=new_model.predict_classes(res)
    print("magnitude:",int(y_pred))
    res=int(y_pred)
    print("magnitude:",int(y_pred))
    if res<5:
        print("NO EARTHQUAKE WILL OCCUR IN",region,"REGION")
    else:
        print("EARTHQUKAE WILL OCCUR IN",region,"WITH MAGNITUDE",res)
    rad=int(y_pred)*10
    
    
    import folium 
  
    my_map2 = folium.Map(location = [28.5011226, 77.4099794], 
                                         zoom_start = 5) 
  
# CircleMarker with radius 
    folium.CircleMarker(location = [latitude, longitude], 
                    radius = rad, popup = ' magnitude ').add_to(my_map2) 
  
# save as html 
    my_map2.save(" viz.html ")

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStatusTip("")
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(C:/Users/k.l.sreeram/Documents/final demo/hgtrd.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 420, 137, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(690, 360, 158, 31))
        self.lineEdit.setToolTip("")
        self.lineEdit.setText("")
        self.lineEdit.setProperty("clearButtonEnabled", True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.clicked.connect(self.submit)
        
        self.pushButton.setGeometry(QtCore.QRect(830, 620, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(137, 0, 86, 255), stop:0.602273 rgba(0, 0, 0, 255));")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1130, 450, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(950, 420, 137, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 90, 1381, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(340, 80, 851, 71))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(54)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(690, 450, 158, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setProperty("clearButtonEnabled", True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 330, 135, 89))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proactive Disaster Detection"))
        self.label_4.setText(_translate("MainWindow", "Month"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "City,Region"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_2.setText(_translate("MainWindow", "Year"))
        self.label_5.setText(_translate("MainWindow", "Proactive Disaster Detection"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "1/2/3...../12"))
        self.label_6.setText(_translate("MainWindow", "Region"))


    def submit(self):
        self.xregion = self.lineEdit.text()
        self.xmonth = self.lineEdit_4.text()
        self.xyear = self.lineEdit_2.text()
        region=self.xregion
        month=self.xmonth
        year=self.xyear
        new(region,month,year)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())