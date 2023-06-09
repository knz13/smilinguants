from src.general import *
from src.animated import *


class Display:
    __screen_var = None
    __clock = None
    __running = True
    __fill_color = (255,255,255)
    __current_screen = None
    __notifier = Events(["onMouseDown","onMouseUp","onKeyDown","onKeyUp","onMouseMove"])
    __delta = 0
    __size = ()
    
    def initialize(width=800,height=600) -> None:
        pygame.init()
        
        Display.__screen_var = pygame.display.set_mode((width, height))
        Display.__size = (width,height)

        Display.__clock = pygame.time.Clock()
        
        while Display.__running:

            for i in Animated.animated_list:
                i.update(Display.__delta)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Display.__running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Display.__notifier.onMouseDown(pygame.mouse.get_pos())

                if event.type == pygame.MOUSEBUTTONUP:
                    Display.__notifier.onMouseUp(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    Display.__notifier.onKeyDown(event.key)
                if event.type == pygame.KEYUP:
                    Display.__notifier.onKeyUp(event.key)
                if event.type == pygame.MOUSEMOTION:
                    Display.__notifier.onMouseMove(pygame.mouse.get_pos())


            Display.__screen_var.fill(Display.__fill_color)

            if Display.__current_screen:
                Display.__current_screen.draw(Display.__screen_var)

            pygame.display.flip()

            Display.__delta = Display.__clock.tick(60)/1000

        
        pygame.quit()

    def size():
        return Display.__size
    
    def on_mouse_move(func):
        Display.__notifier.onMouseMove += func

    def remove_on_mouse_move(func):
        Display.__notifier.onMouseMove -= func

    def on_mouse_down(func):
        Display.__notifier.onMouseDown += func

    def remove_on_mouse_down(func): 
        Display.__notifier.onMouseDown -= func

    def on_mouse_up(func):
        Display.__notifier.onMouseUp += func

    def remove_on_mouse_up(func): 
        Display.__notifier.onMouseUp -= func

    def on_key_down(func):
        Display.__notifier.onKeyDown += func

    def remove_on_key_down(func): 
        Display.__notifier.onKeyDown -= func

    def on_key_up(func):
        Display.__notifier.onKeyUp += func

    def remove_on_key_down(func): 
        Display.__notifier.onKeyUp -= func

    def set_screen(screen):
        Display.__current_screen = screen

    def set_fill_color(color):
        Display.__fill_color = color