
class Fan:
    # Three constant fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Constructor
    def __init__(self, speed=SLOW, on=True, radius=6.0, color="blue"):
        self.__speed = speed
        self.__on = bool(on)
        self.__radius = float(radius)
        self.__color = str(color)\

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, new_speed):
        if new_speed in (Fan.SLOW, Fan.MEDIUM, Fan.FAST):
            self.__speed = new_speed
        else:
            raise ValueError("Invalid speed")

    @property
    def is_on(self):
        return self.__on
    @is_on.setter
    def is_on(self, activity):
        self.__on = bool(activity)

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, new_radius):
        self.__radius = float(new_radius)

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, new_color):
        self.__color = str(new_color)











