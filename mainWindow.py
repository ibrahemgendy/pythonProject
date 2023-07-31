from PyQt5 import QtWidgets,QtCore


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, aPiCar_Hmi, aControlElements):
        super().__init__()
        self.aPiCar_Hmi = aPiCar_Hmi
        self.aControlElements = aControlElements
        self.sub_windows = {}
        self.setWindowTitle("Main Window")
        self.setWindowState(QtCore.Qt.WindowMaximized)
        window_menu = self.menuBar().addMenu("Window Menu")
        self.populate_window_menu(window_menu)

    def closeEvent(self, event):
        self.aPiCar_Hmi.user_input("Quit")

    def populate_window_menu(self, menu):
        throttle_window = QtWidgets.QMainWindow()
        throttle_window.setWindowTitle("Throttle Window")
        throttle_window.setCentralWidget(self.aControlElements.get_new_throttle_slider())
        self.sub_windows["Throttle"] = throttle_window
        steering_window = QtWidgets.QMainWindow()
        steering_window.setWindowTitle("Steering Window")
        steering_window.setCentralWidget(self.aControlElements.get_new_steering_slider())
        self.sub_windows["Steering"] = steering_window
        signal_window = QtWidgets.QMainWindow()
        signal_window.setWindowTitle("Signal Window")
        signal_window.setCentralWidget(self.aControlElements.get_new_signal_list())
        self.sub_windows["Signal"] = signal_window
        gear_window = QtWidgets.QMainWindow()
        gear_window.setWindowTitle("Gear Window")
        gear_window.setCentralWidget(self.aControlElements.get_new_gear_slider())
        self.sub_windows["Gear"] = gear_window
        for sub_window_name, sub_window in self.sub_windows.items():
            action = menu.addAction(sub_window_name)
            action.triggered.connect(self.show_sub_window)

    def show_sub_window(self):
        action = self.sender()
        sub_window_name = action.text()
        sub_window = self.sub_windows.get(sub_window_name)
        if sub_window:
            sub_window.show()
