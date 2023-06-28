from src.general import pygame
from src.screen import *
from src.square_button import *


class MenuScreen(Screen):

    def __init__(self) -> None:
        super().__init__()

        self.__main_button = SquareButton(100,100,color=[255,Animated(0),0],on_pressed=lambda: self.__on_press_button())
        self.__main_button.position[0] = Animated(0)
        self.__index = 0

    def __on_press_button(self):
        self.__main_button.position[0] += [Display.size()[0]-100,-Display.size()[0]+100][self.__index]
        self.__main_button.color[1] += [255,-255][self.__index]
        self.__index += 1
        if self.__index >1:
            self.__index = 0

    def draw(self, surface: pygame.Surface):

        self.__main_button.draw(surface)

        return super().draw(surface)