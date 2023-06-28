import numpy as np
from src.watcher import *
import math

class Easing:

    def easeInOutElastic(x):
        c5 = (2 * math.pi) / 4.5
        return 0 if x == 0 else (1 if x == 1 else (-(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * c5)) / 2 if x < 0.5 else (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * c5)) / 2 + 1))
    def easeOutElasic(x):
        c4 = (2 * math.pi) / 3

        return 0 if x == 0 else (1 if x == 1 else (math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1))
    def easeInOutQuad(x):
        return 2 * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 2) / 2

class Animated:
    animated_list = []

    def __init__(self, value, duration=1,easing=Easing.easeInOutQuad) -> None:
        self.value = value
        self.__interpolating_value = value
        self.__old_value = value
        self.__duration = duration
        self.__current_interp = 0
        self.__easing = easing

        Animated.animated_list.append(self)

    def update(self, delta):
        if self.__current_interp < 1:
            self.__interpolating_value = self.__old_value + self.__easing(self.__current_interp) * (self.value - self.__old_value)
            self.__current_interp += delta/self.__duration
        else:
            self.__old_value = self.value

    def get_current(self):
        return self.__interpolating_value
    
    def set_current(self, value):
        self.__old_value = self.value
        self.__current_interp = 0
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value + other.get_current()
        else:
            return self.__interpolating_value + other

    def __iadd__(self, other):
        if isinstance(other, Animated):
            self.set_current(self.value + other.get_current())
        else:
            self.set_current(self.value + other)
        return self

    def __sub__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value - other.get_current()
        else:
            return self.__interpolating_value - other

    def __isub__(self, other):
        if isinstance(other, Animated):
            self.set_current(self.value - other.get_current())
        else:
            self.set_current(self.value - other)
        return self

    def __mul__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value * other.get_current()
        else:
            return self.__interpolating_value * other

    def __imul__(self, other):
        if isinstance(other, Animated):
            self.set_current(self.value * other.get_current())
        else:
            self.set_current(self.value * other)
        return self

    def __truediv__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value / other.get_current()
        else:
            return self.__interpolating_value / other

    def __itruediv__(self, other):
        if isinstance(other, Animated):
            self.set_current(self.value / other.get_current())
        else:
            self.set_current(self.value / other)
        return self

    def __lt__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value < other.get_current()
        else:
            return self.__interpolating_value < other

    def __le__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value <= other.get_current()
        else:
            return self.__interpolating_value <= other

    def __gt__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value > other.get_current()
        else:
            return self.__interpolating_value > other

    def __ge__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value >= other.get_current()
        else:
            return self.__interpolating_value >= other

    def __eq__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value == other.get_current()
        else:
            return self.__interpolating_value == other

    def __ne__(self, other):
        if isinstance(other, Animated):
            return self.__interpolating_value != other.get_current()
        else:
            return self.__interpolating_value != other

    def __repr__(self) -> str:
        return f'Animated with old_value = {self.__interpolating_value} and value = {self.value}'

    def __del__(self):
        Animated.animated_list.remove(self)