
class ComponentData:

    def __init__(self, aPiCarHmi):
        self.aPiCarHmi = aPiCarHmi
        self.iDrive_State_Value = 0
        self.iSteering_Value = 90
        self.fThrottle_Value = 0

    def get_drive_state_value(self):
        return self.iDrive_State_Value

    def get_steering_value(self):
        return self.iSteering_Value

    def get_throttle_value(self):
        return self.fThrottle_Value

    def set_drive_state_value(self, iDrive_State_Value):
        self.iDrive_State_Value = iDrive_State_Value

    def set_steering_value(self, iSteering_Value):
        self.iSteering_Value = iSteering_Value
        if self.iSteering_Value >= 180:
            self.iSteering_Value = 180
        if self.iSteering_Value <= 0:
            self.iSteering_Value = 0

    def set_throttle_value(self, fThrottle_Value):
        self.fThrottle_Value = fThrottle_Value


