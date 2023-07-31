from PyQt5 import QtWidgets
from Model.controlElements import ControlElements
from Model.mainWindow import MainWindow


class WindowBuilder:

    def __init__(self, aControlElements, aMainWindow):
        self.aControlElements = aControlElements
        self.aMain_Window = aMainWindow
        self.aMdi_Area = None

    def build_gear_slider_window(self):
        aGear_Slider_Window = QtWidgets.QMdiSubWindow()
        aGear_Slider_Window.setWidget(QtWidgets.QWidget())
        aGear_Slider_Window.setWindowTitle("Gear")
        aGear_Slider_Window.setWindowFlags(aGear_Slider_Window.windowFlags())
        self.aMdi_Area.addSubWindow(aGear_Slider_Window)
        aGear_Slider_Window.setGeometry(1600, 50, 200, 300)
        aGear_Slider_Window.setWidget(self.aControlElements.get_new_gear_slider())

    #def build_main_window(self, aPiCar_Hmi):
        #self.aMain_Window = MainWindow(aPiCar_Hmi, self.aControlElements)

    def build_mdi_area(self):
        self.aMdi_Area = QtWidgets.QMdiArea()
        self.aMain_Window.setCentralWidget(self.aMdi_Area)

    def build_steering_slider_window(self):
        aSteering_Slider_Window = QtWidgets.QMdiSubWindow()
        aSteering_Slider_Window.setWidget(QtWidgets.QWidget())
        aSteering_Slider_Window.setWindowTitle("Steering")
        aSteering_Slider_Window.setWindowFlags(aSteering_Slider_Window.windowFlags())
        self.aMdi_Area.addSubWindow(aSteering_Slider_Window)
        aSteering_Slider_Window.setGeometry(1300, 700, 600, 200)
        aSteering_Slider_Window.setWidget(self.aControlElements.get_new_steering_slider())

    def build_signal_list_window(self):
        aSignal_List_Window = QtWidgets.QMdiSubWindow()
        aSignal_List_Window.setWidget(QtWidgets.QWidget())
        aSignal_List_Window.setWindowTitle("Signal List")
        aSignal_List_Window.setWindowFlags(aSignal_List_Window.windowFlags())
        self.aMdi_Area.addSubWindow(aSignal_List_Window)
        aSignal_List_Window.setGeometry(50, 600, 600, 300)
        aSignal_List_Window.setWidget(self.aControlElements.get_new_signal_list())

    def build_throttle_slider_window(self):
        aThrottle_Slider_Window = QtWidgets.QMdiSubWindow()
        aThrottle_Slider_Window.setWidget(QtWidgets.QWidget())
        aThrottle_Slider_Window.setWindowTitle("Throttle")
        aThrottle_Slider_Window.setWindowFlags(aThrottle_Slider_Window.windowFlags())
        self.aMdi_Area.addSubWindow(aThrottle_Slider_Window)
        aThrottle_Slider_Window.setGeometry(1100, 50, 300, 300)
        aThrottle_Slider_Window.setWidget(self.aControlElements.get_new_throttle_slider())

    def get_main_window(self):
        return self.aMain_Window

    def get_mdi_area(self):
        return self.aMdi_Area

