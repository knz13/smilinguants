from src.general import *
from src.display import *

class SquareButton:

    def __init__(self,width,height,color=(255,255,255),image=None,on_pressed=None) -> None:
        self.width = width
        self.height = height
        self.image = image
        self.color = color
        self.position = [0,0]
        self.__pressed = False
        self.__on_pressed = on_pressed
        
        Display.on_mouse_down(self.__on_mouse_down)
        Display.on_mouse_up(self.__on_mouse_up)

    def contains_point(self,position):
        if position[0] >= self.position[0] and position[0] <= self.position[0] + self.width:
            if position[1] >= self.position[1] and position[1] <= self.position[1] + self.height:
                return True
        return False

    def __on_mouse_down(self,position):
        if self.contains_point(position):
            self.__pressed = True
    

    def __on_mouse_up(self,position):
        if self.contains_point(position):
            self.__pressed = False
            if callable(self.__on_pressed):
                self.__on_pressed()

    def __del__(self):
        print("deleted button!")
        Display.remove_on_mouse_down(self.__on_mouse_down)
        Display.remove_on_mouse_up(self.__on_mouse_up)


    def draw(self,surface):
        color = animated_or((animated_or(self.color[0]),animated_or(self.color[1]),animated_or(self.color[2])))
        pygame.draw.rect(surface,color,pygame.Rect(animated_or(self.position[0]),animated_or(self.position[1]),animated_or(self.width),animated_or(self.height)))

    