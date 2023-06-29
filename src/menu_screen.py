from src.general import pygame
from src.screen import *
from src.square_button import *
import random


class MenuScreen(Screen):

    def __init__(self) -> None:
        super().__init__()

        self.__main_button = SquareButton(100,100,color=[Animated(0),Animated(0),Animated(0)])
        self.__main_button.position[0] = Animated(0)
        self.__main_button.position[1] = Animated(0)
        self.__index = 0

        Display.on_mouse_down(self.__on_mouse_down)

    def __on_mouse_down(self,pos):
        self.__main_button.position[0].value = pos[0]
        self.__main_button.position[1].value = pos[1]

        self.__main_button.color[0].value = random.choice([255,10,100])
        self.__main_button.color[1].value = random.choice([255,10,100])
        self.__main_button.color[2].value = random.choice([255,10,100])
    

    def draw(self, surface: pygame.Surface):

        self.__main_button.draw(surface)

        return super().draw(surface)