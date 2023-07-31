from threading import Thread
from time import sleep
from PiCar.main import PiCar
from Model.windowBuilder import WindowBuilder
from Model.ComponentData import ComponentData
from Model.controlElements import ControlElements
from Model.mainWindow import MainWindow


class Model:

    def __init__(self):
        self.aPiCar = PiCar()
        self.aPiCar.run_picar()
        self.aPiCarHmi = self.aPiCar.get_hmi_instance()
        self.aComponent_Data = ComponentData(self.aPiCarHmi)
        self.aControlElements = ControlElements(self.aComponent_Data)
        self.aMainWindow = MainWindow(self.aPiCarHmi, self.aControlElements)
        self.aWindow_Builder = WindowBuilder(self.aControlElements, self.aMainWindow)

    def build_and_run_picar(self):
        self.aPiCar.program_loop()

    def build_windows(self):
        #self.aWindow_Builder.build_main_window(self.aPiCarHmi)
        self.aWindow_Builder.build_mdi_area()
        self.aWindow_Builder.build_gear_slider_window()
        self.aWindow_Builder.build_steering_slider_window()
        self.aWindow_Builder.build_throttle_slider_window()
        self.aWindow_Builder.build_signal_list_window()

    def get_main_window(self):
        return self.aWindow_Builder.get_main_window()

    def get_mdi_area(self):
        return self.aWindow_Builder.get_mdi_area()

    def start_picar_thread(self):
        picar_thread = Thread(target=self.build_and_run_picar)
        picar_thread.start()
        sleep(3)
        print("PiCar ready")

    def set_throttle_value(self, fThrottle_Value):
        self.aComponent_Data.set_throttle_value(fThrottle_Value)

    def set_drive_state_value(self, iDrive_State_Value):
        self.aComponent_Data.set_drive_state_value(iDrive_State_Value)

    def set_gear_state_to_park(self):
        iDrive_State_Value = 0
        self.aComponent_Data.set_drive_state_value(iDrive_State_Value)

    def set_gear_state_to_forward(self):
        iDrive_State_Value = 1
        self.aComponent_Data.set_drive_state_value(iDrive_State_Value)

    def set_gear_state_to_reverse(self):
        iDrive_State_Value = 3
        self.aComponent_Data.set_drive_state_value(iDrive_State_Value)

    def set_steering_value(self, iSteering_Value):
        self.aComponent_Data.set_steering_value(iSteering_Value)

    def get_drive_state_value(self):
        return self.aComponent_Data.get_drive_state_value()

    def get_steering_value(self):
        return self.aComponent_Data.get_steering_value()

    def get_throttle_value(self):
        return self.aComponent_Data.get_throttle_value()
