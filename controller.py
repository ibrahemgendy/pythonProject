

class Controller:

    def __init__(self, aModel, aView):
        self.__aModel = aModel
        self.__View = aView

    def run(self):
        self.__View.run_ui()

    def get_drive_state_value(self):
        return self.__aModel.get_drive_state_value()

    def get_throttle_value(self):
        return self.__aModel.get_throttle_value()

    def get_steering_value(self):
        return self.__aModel.get_steering_value()

    def set_throttle(self, iValue):
        self.__aModel.set_throttle_value(iValue)

    def set_steering(self,iValue):
        self.__aModel.set_steering_value(iValue)

    def set_gear_state_to_park(self):
        self.__aModel.set_gear_state_to_park()

    def set_gear_state_to_forward(self):
        self.__aModel.set_gear_state_to_forward()

    def set_gear_state_to_reverse(self):
        self.__aModel.set_gear_state_to_reverse()
