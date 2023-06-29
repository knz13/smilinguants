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
        self.__dict__["value"] = value
        self._interpolating_value = value
        self._old_value = value
        self._duration = duration
        self._current_interp = 0
        self._easing = easing

        Animated.animated_list.append(self)

    def update(self, delta):
        if self._current_interp < 1:
            self._interpolating_value = self._old_value + self._easing(self._current_interp) * (self.__dict__["value"] - self._old_value)
            self._current_interp += delta/self._duration
        else:
            self._old_value = self.__dict__["value"]

    @property
    def value(self):
        return self._interpolating_value

    @value.setter
    def value(self, value):
        self._old_value = self._interpolating_value
        self._current_interp = 0
        self.__dict__["value"] = value
    
    def __add__(self, other):
        if isinstance(other, Animated):
            return self.value + other.value
        else:
            return self.value + other

    def __iadd__(self, other):
        if isinstance(other, Animated):
            self.value += other.value
        else:
            self.value += other
        return self

    def __sub__(self, other):
        if isinstance(other, Animated):
            return self.value - other.value
        else:
            return self.value - other

    def __isub__(self, other):
        if isinstance(other, Animated):
            self.value -= other.value
        else:
            self.value -= other
        return self

    def __mul__(self, other):
        if isinstance(other, Animated):
            return self.value * other.value
        else:
            return self.value * other

    def __imul__(self, other):
        if isinstance(other, Animated):
            self.value *= other.value
        else:
            self.value *= other
        return self

    def __truediv__(self, other):
        if isinstance(other, Animated):
            return self.value / other.value
        else:
            return self.value / other

    def __itruediv__(self, other):
        if isinstance(other, Animated):
            self.value /= other.value
        else:
            self.value /= other
        return self

    def __lt__(self, other):
        if isinstance(other, Animated):
            return self.value < other.value
        else:
            return self.value < other

    def __le__(self, other):
        if isinstance(other, Animated):
            return self.value <= other.value
        else:
            return self.value <= other

    def __gt__(self, other):
        if isinstance(other, Animated):
            return self.value > other.value
        else:
            return self.value > other

    def __ge__(self, other):
        if isinstance(other, Animated):
            return self.value >= other.value
        else:
            return self.value >= other

    def __eq__(self, other):
        if isinstance(other, Animated):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, Animated):
            return self.value != other.value
        else:
            return self.value != other

    def __repr__(self) -> str:
        return f'Animated with old_value = {self.__interpolating_value} and value = {self.value}'

    def __del__(self):
        Animated.animated_list.remove(self)
