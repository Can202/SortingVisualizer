import pygame
import pygame.draw
import constants as C

class Bar:
    def __init__(self, _size = 100, _position = [0,0], _width = 50) -> None:
        self.size = _size
        self.position = _position
        self.width = _width
        self.color = C.WHITE
        self.update()
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def update(self):
        self.rect = pygame.Rect(self.position[C.X], self.position[C.Y] - self.size + C.HEIGHT, self.width, self.size)

    def get_pos(self):
        return self.position
    def set_pos(self, _pos):
        self.position = _pos

