from src.general import pygame
from src.screen import *


class MenuScreen(Screen):

    def draw(self, surface: pygame.Surface):

        pygame.draw.rect(surface,(255,0,0),pygame.Rect(20,20,100,100))

        return super().draw(surface)