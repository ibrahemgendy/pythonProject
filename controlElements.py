from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget,QLabel
from PyQt5.QtCore import QSettings
from Model.ComponentData import ComponentData
from PiCar.main import PiCar


class ControlElements:

    def __init__(self, aComponentData):
        self.aComponent_Data = aComponentData
        self.throttle_item = None
        self.steering_angle_item = None
        self.gear_state_item = None
        self.saved_throttle_value = self.aComponent_Data.get_throttle_value()
        self.saved_steering_value = self.aComponent_Data.get_steering_value()
        self.saved_gear_value = self.aComponent_Data.get_drive_state_value()
        #self.load_settings()


    def get_new_gear_slider(self):
        aSlider_Orientation = QtCore.Qt.Vertical
        aGear_Slider = QtWidgets.QSlider(aSlider_Orientation)
        aGear_Slider.setMinimum(0)
        aGear_Slider.setMaximum(2)
        aGear_Slider.setValue(self.aComponent_Data.get_drive_state_value())
        aGear_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        aGear_Slider.setTickInterval(1)
        aSlider_Labels = QtWidgets.QVBoxLayout()
        aSlider_Labels.addWidget(QtWidgets.QLabel("R"))
        aSlider_Labels.addSpacing(10)
        aSlider_Labels.addWidget(QtWidgets.QLabel("D"))
        aSlider_Labels.addSpacing(25)
        aSlider_Labels.addWidget(QtWidgets.QLabel("P"))
        aLayout = QtWidgets.QHBoxLayout()
        aLayout.addWidget(aGear_Slider)
        aLayout.addLayout(aSlider_Labels)
        aWidget = QtWidgets.QWidget()
        aWidget.setLayout(aLayout)
        #aGear_Slider.valueChanged.connect(self.on_gear_slider_change)
        aGear_Slider.valueChanged.connect(self.update_gear_state)
        return aWidget

    def get_new_steering_slider(self, lmax=30, rmax=150):
        aSlider_Orientation = QtCore.Qt.Horizontal
        aSteering_Slider = QtWidgets.QSlider(aSlider_Orientation)
        aSteering_Slider.setMinimum(lmax)
        aSteering_Slider.setMaximum(rmax)
        aSteering_Slider.setValue(self.aComponent_Data.get_steering_value())
        aSteering_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        aSteering_Slider.setTickInterval(10)
        steering_min_label = QtWidgets.QLabel(str(lmax))
        steering_max_label = QtWidgets.QLabel(str(rmax))
        aLayout = QtWidgets.QHBoxLayout()
        aLayout.addWidget(steering_min_label)
        aLayout.addWidget(aSteering_Slider)
        aLayout.addWidget(steering_max_label)
        aWidget = QtWidgets.QWidget()
        aWidget.setLayout(aLayout)
        #aSteering_Slider.valueChanged.connect(self.on_steering_slider_change)
        aSteering_Slider.valueChanged.connect(self.update_steering_angle)
        return aWidget

    def get_new_throttle_slider(self):
        aSlider_Orientation = QtCore.Qt.Vertical
        aThrottle_Slider = QtWidgets.QSlider(aSlider_Orientation)
        aThrottle_Slider.setMinimum(0)
        aThrottle_Slider.setMaximum(100)
        aThrottle_Slider.setValue(self.aComponent_Data.get_throttle_value())
        aThrottle_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        aThrottle_Slider.setTickInterval(10)
        aSlider_Labels = QtWidgets.QVBoxLayout()
        aSlider_Labels.setContentsMargins(0, 0, 0, 0)
        aSlider_Labels.setSpacing(0)
        aLabel_0 = QtWidgets.QLabel("100")
        aLabel_50 = QtWidgets.QLabel("50")
        aLabel_100 = QtWidgets.QLabel("0")
        spacer_item = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        aSlider_Labels.addWidget(aLabel_0)
        aSlider_Labels.addItem(spacer_item)
        aSlider_Labels.addWidget(aLabel_50)
        aSlider_Labels.addItem(spacer_item)
        aSlider_Labels.addWidget(aLabel_100)
        aLayout = QtWidgets.QHBoxLayout()
        aLayout.addWidget(aThrottle_Slider)
        aLayout.addLayout(aSlider_Labels)
        aWidget = QtWidgets.QWidget()
        aWidget.setLayout(aLayout)
        #aThrottle_Slider.valueChanged.connect(self.on_throttle_slider_change)
        aThrottle_Slider.valueChanged.connect(self.update_requested_throttle)
        return aWidget

    def save_settings(self):
        settings = QSettings("MyApp", "PiCar")
        settings.setValue("throttle_value", self.saved_throttle_value)
        settings.setValue("steering_value", self.saved_steering_value)
        settings.setValue("gear_value", self.saved_gear_value)

    def load_settings(self):
        settings = QSettings("MyApp", "PiCar")
        self.saved_throttle_value = settings.value("throttle_value", self.aComponent_Data.get_throttle_value(), type=int)
        self.saved_steering_value = settings.value("steering_value", self.aComponent_Data.get_steering_value(), type=int)
        self.saved_gear_value = settings.value("gear_value", self.aComponent_Data.get_drive_state_value(), type=int)

    def get_new_signal_list(self):
        output_list = QTreeWidget()
        output_list.setColumnCount(3)
        output_list.setHeaderLabels(["Unit", "Output Name", "Value"])
        output_list.setHeaderHidden(False)
        output_list.setRootIsDecorated(False)
        unit_column = output_list.headerItem()
        unit_column.setText(0, "Unit")
        name_column = output_list.headerItem()
        name_column.setText(1, "Output Name")
        value_column = output_list.headerItem()
        value_column.setText(2, "Value")
        output_list.setColumnWidth(0, 120)
        output_list.setColumnWidth(1, 270)
        output_list.setColumnWidth(2, 120)
        self.add_signal_item(output_list, "Degrees", "ACTUAL_STEERING ANGLE", "90")
        self.add_signal_item(output_list, "gear_state", "ACTUAL_DRIVE STATE", "'P'")
        self.add_signal_item(output_list, "m/s", "ACTUAL_THROTTLE_VALUE", "0.00")
        layout = QVBoxLayout()
        layout.addWidget(output_list)
        widget = QWidget()
        widget.setLayout(layout)
        self.throttle_item = self.add_signal_item(output_list, "m/s", "REQUESTED_THROTTLE_VALUE", str(self.aComponent_Data.get_throttle_value()))
        self.steering_angle_item = self.add_signal_item(output_list, "Degrees", "REQUESTED STEERING ANGLE", str(self.aComponent_Data.get_steering_value()))
        self.gear_state_item = self.add_signal_item(output_list, "gear_state", "REQUESTED DRIVE STATE", "'P'")
        return widget

    def add_signal_item(self, output_list, unit, name, value):
        item = QTreeWidgetItem(output_list, [unit, name, value])
        return item

    def update_requested_throttle(self, value):
        if self.throttle_item:
            self.throttle_item.setText(2, str(value))
            self.saved_throttle_value = value

    def update_steering_angle(self, value):
        if self.steering_angle_item:
            self.steering_angle_item.setText(2, str(value))
            self.saved_steering_value = value

    def update_gear_state(self, value):
        if self.gear_state_item:
            if value == 0:
                self.gear_state_item.setText(2, "'P'")
            elif value == 1:
                self.gear_state_item.setText(2, "'D'")
            elif value == 2:
                self.gear_state_item.setText(2, "'R'")
            self.saved_gear_value = value

    #def on_throttle_slider_change(self):
        #self.saved_throttle_value = self.aComponent_Data.get_throttle_value()
        #self.update_requested_throttle(self.saved_throttle_value)
        #return self.saved_throttle_value

    #def on_steering_slider_change(self):
        #steering_value = self.aComponent_Data.get_actual_steering_angle()
        #self.update_steering_angle(steering_value)
        #return steering_value

    #def on_gear_slider_change(self):
        #gear_value = self.aComponent_Data.get_actual_gear_state()
        #self.update_gear_state(gear_value)
        #return gear_value