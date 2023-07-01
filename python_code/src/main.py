from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from utils.serial_coms import EspSerialComs, SensorsConfig


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1056, 735)
        self.groupBox_4 = QtWidgets.QGroupBox(Frame)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 20, 601, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(12, 32, 401, 163))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(307, 69, 82, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(12, 69, 141, 17))
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(430, 30, 145, 176))
        self.groupBox.setObjectName("groupBox")
        self.acc_sens = QtWidgets.QSpinBox(self.groupBox)
        self.acc_sens.setGeometry(QtCore.QRect(90, 30, 45, 26))
        self.acc_sens.setObjectName("acc_sens")
        self.acc_odr = QtWidgets.QSpinBox(self.groupBox)
        self.acc_odr.setGeometry(QtCore.QRect(90, 60, 45, 26))
        self.acc_odr.setObjectName("acc_odr")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 62, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 62, 17))
        self.label_2.setObjectName("label_2")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_4.setGeometry(QtCore.QRect(90, 90, 45, 26))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(90, 120, 45, 26))
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 62, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 62, 17))
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Frame)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 260, 1011, 451))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.gridLayout.addWidget(self.canvas1, 1, 1, 1, 1)
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.gridLayout.addWidget(self.canvas2, 1, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 0, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(Frame)
        self.groupBox_5.setGeometry(QtCore.QRect(630, 20, 411, 231))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 576, 25))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 40, 131, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setGeometry(QtCore.QRect(20, 180, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(30, 140, 83, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_8.setBuddy(self.label)
        self.label.setBuddy(self.label)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.groupBox_4.setTitle(_translate("Frame", "Settings"))
        self.groupBox_2.setTitle(_translate("Frame", "BME688"))
        self.comboBox.setItemText(0, _translate("Frame", "Paralelo"))
        self.comboBox.setItemText(1, _translate("Frame", "Forzado"))
        self.label_8.setText(_translate("Frame", "Modo funcionamiento"))
        self.groupBox.setTitle(_translate("Frame", "BMI2070"))
        self.label.setText(_translate("Frame", "acc_sens"))
        self.label_2.setText(_translate("Frame", "acc_odr"))
        self.label_3.setText(_translate("Frame", "gyr_sens"))
        self.label_4.setText(_translate("Frame", "gyr_odr"))
        self.groupBox_3.setTitle(_translate("Frame", "Datos"))
        self.acc_odr.setProperty("value", 10)
        self.acc_sens.setProperty("value", 2)
        self.spinBox_4.setProperty("value", 0)
        self.spinBox_3.setProperty("value", 10)
        self.groupBox_5.setTitle(_translate("Frame", "Inicializar"))
        self.label_5.setText(_translate("Frame", "Sensor activo"))
        self.comboBox_2.setItemText(0, _translate("Frame", "BMI270"))
        self.comboBox_2.setItemText(1, _translate("Frame", "BME688"))
        self.pushButton.setText(_translate("Frame", "START"))


class MyApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        # --------------- Graficos

        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.ui.gridLayout.addWidget(self.canvas1, 1, 1, 1, 1)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.ui.gridLayout.addWidget(self.canvas2, 1, 0, 1, 1)


        self.ui.comboBox_5.installEventFilter(self)
        self.ui.comboBox_4.installEventFilter(self)
        self.data_values = {
            "acc-m/s2": {
                "acc_x": [],
                "acc_z": [],
                "acc_y": [],
            },
            "acc-g": {
                "acc_y": [],
                "acc_z": [],
                "acc_x": [],
            },
            "gyr-dps": {
                "gyr_x": [],
                "gyr_y": [],
                "gyr_z": [],
            },
        }
        self.graph1_data_src = None
        self.graph2_data_src = None
        self.ui.comboBox_4.currentIndexChanged.connect(self.update_data_combo)
        self.ui.comboBox_5.currentIndexChanged.connect(self.update_data_combo)

        # --------------- Seleccion de sensor

        self.ui.comboBox_2.currentIndexChanged.connect(self.on_sensor_change)

        self.ui.pushButton.clicked.connect(self.on_click_start_coms)

        # -------------------- Serial Coms
        self.serial_coms = None
        self.running = False
        #
        self.start_get_data_thread()

    class Worker(QtCore.QObject):
        def __init__(self,target_function):
            super().__init__()
            self.target_function = target_function

        def run(self):
            while True:
               self.target_function()


  
    def start_get_data_thread(self):
        self.thread = QtCore.QThread()
        self.worker = self.Worker(self.update_graphs)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()


    def update_data_combo(self):
        self.graph2_data_src = self.ui.comboBox_4.currentText()
        self.graph1_data_src = self.ui.comboBox_5.currentText()

    def eventFilter(self, obj, event):
        if (
            obj == self.ui.comboBox_5 or obj == self.ui.comboBox_4
        ) and event.type() == QtCore.QEvent.MouseButtonPress:
            self.update_data_sources()
        return super().eventFilter(obj, event)

    def update_data_sources(self):
        print("update data sources")
        print(self.data_values)
        # claer items
        self.ui.comboBox_4.clear()
        self.ui.comboBox_5.clear()
        for key, item in self.data_values.items():
            if len(item) > 0:
                self.ui.comboBox_4.addItem(key)
                self.ui.comboBox_5.addItem(key)

        self.graph1_data_src = self.ui.comboBox_4.currentText()
        self.graph2_data_src = self.ui.comboBox_5.currentText()

    def on_click_start_coms(self):
        # try connection
        self.serial_coms = EspSerialComs()
        if not self.serial_coms.connected:
            error_message = "No serial port found. Please connect the device."
            QtWidgets.QMessageBox.critical(self, "Serial Port Not Found", error_message)
            self.serial_coms = None
            return
        # configure sensors
        selected_sensor = self.ui.comboBox_2.currentText()
        if selected_sensor == "BMI270":
            selected_sensor_value = 0
        elif selected_sensor == "BME688":
            selected_sensor_value = 1

        bme_mode = self.ui.comboBox.currentText()
        bme_mode_value = 0
        if bme_mode == "Paralelo":
            bme_mode_value = 0
        elif bme_mode == "Forzado":
            bme_mode_value = 1
        sensors_config = SensorsConfig(
            int(self.ui.acc_sens.value()),
            int(self.ui.acc_odr.value()),
            int(self.ui.spinBox_4.value()),
            int(self.ui.spinBox_3.value()),
            int(bme_mode_value),
            int(selected_sensor_value),
        )
        print(sensors_config)
        success = self.serial_coms.config_sensors(sensors_config, self.ui.progressBar)
        if not success:
            QtWidgets.QMessageBox.critical(self, "Serial Port Not Found", error_message)
        else:
            self.running = True
        # start data acquisition

    def on_sensor_change(self, index):
        selected_item = self.ui.comboBox_2.currentText()
        print("here")
        print(selected_item)
        if selected_item == "BMI270":
            print("BMI270 selected")
        elif selected_item == "BME688":
            print("BME688 selected")

    def get_data(self):
        data_bmi270 = self.serial_coms.get_data_bmi270()
        self.data_values["acc-m/s2"]["acc_x"].append(data_bmi270[0])
        self.data_values["acc-m/s2"]["acc_y"].append(data_bmi270[1])
        self.data_values["acc-m/s2"]["acc_z"].append(data_bmi270[2])
        self.data_values["acc-g"]["acc_x"].append(data_bmi270[3])
        self.data_values["acc-g"]["acc_y"].append(data_bmi270[4])
        self.data_values["acc-g"]["acc_z"].append(data_bmi270[5])
        self.data_values["gyr-dps"]["gyr_x"].append(data_bmi270[6])
        self.data_values["gyr-dps"]["gyr_y"].append(data_bmi270[7])
        self.data_values["gyr-dps"]["gyr_z"].append(data_bmi270[8])
        print(data_bmi270)

    def update_graphs(self):
        if self.serial_coms is None or not self.serial_coms.connected or not self.running:
            return
        self.get_data()

        if self.graph1_data_src is None or self.graph2_data_src is None:
            return
        # get the last 100 values for each

        graph1_data = {}
        for key, item in self.data_values[self.graph1_data_src].items():
            graph1_data[key] = item[-100:]
        graph2_data = {}
        for key, item in self.data_values[self.graph2_data_src].items():
            graph2_data[key] = item[-100:]

        first_key = list(graph1_data.keys())[0]
        x_data = [i for i in range(len(graph1_data[first_key]))]

        self.figure1.clear()
        self.figure2.clear()

        self.create_graph_data(self.figure1, self.graph1_data_src, x_data, graph1_data)
        self.create_graph_data(self.figure2, self.graph2_data_src, x_data, graph2_data)

        self.canvas1.draw()
        self.canvas2.draw()

    def create_graph_data(self, figure, name, x_data, y_data):
        axes = figure.add_subplot(111)
        for key, values in y_data.items():
            axes.plot(x_data, values, label=key)
        axes.set_xlabel("X-axis")
        axes.set_ylabel("Y-axis")
        axes.set_title(name)
        axes.legend()


app = QtWidgets.QApplication([])
window = MyApplication()
window.show()
app.exec()
