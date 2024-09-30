# Going to make a program to visualize the sorting algorithm

import pygame
pygame.init()

import my_objects
import constants as C

import random

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
        self.window = pygame.Surface((C.WIDTH, C.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        # in seconds
        self.deltaTime = 0
        self.offset = pygame.Vector2(0,0)
        self.fix = 1

        self.start()
    

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.bubble_sort()
            self.update()
            self.draw()

            pygame.display.flip()

            self.deltaTime = self.clock.tick(500) / 1000
    
    def bubble_sort(self):
        if self.do:
            if self.remove_last_color:
                self.bars[self.current-1].color = C.WHITE
                self.remove_last_color = False
            print(f"doing iteration: {self.iteration+1}:{self.current+1}")
            self.bars[self.current].color = C.BLUE
            self.bars[self.current + 1].color = C.BLUE
            if self.bars[self.current].size > self.bars[self.current + 1].size:
            
                k = self.bars[self.current].get_pos()
                self.bars[self.current].position = self.bars[self.current + 1].get_pos()
                self.bars[self.current + 1].position = k
                
                q = self.bars[self.current]
                self.bars[self.current] = self.bars[self.current+1]
                self.bars[self.current+1] = q
            
            
            if self.current < len(self.bars) - 2 - self.iteration:
                self.current += 1
                self.remove_last_color = True
            else:
                self.current = 0
                self.iteration += 1
                self.bars[-self.iteration].color = C.GREEN
                self.bars[-self.iteration -1].color = C.WHITE
            if self.iteration >= len(self.bars) -1 : 
                self.do = False 
                print("Finished")
                self.bars[0].color = C.GREEN

    def update(self):
        height = self.screen.get_height()
        width = self.screen.get_width()
        if (height / C.HEIGHT) <= (width/C.WIDTH):
            self.fix = (height / C.HEIGHT)
            self.offset.x = (width - (C.WIDTH * self.fix)) / 2
            self.offset.y = 0
        else:
            self.fix = (width / C.WIDTH)
            self.offset.x = 0
            self.offset.y = (height - (C.HEIGHT * self.fix)) / 2

        
        for i in range(len(self.bars)):
            self.bars[i].update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.window.fill("black")
        for i in range(len(self.bars)):
            self.bars[i].draw(self.window)

        self.screen.blit(pygame.transform.scale(self.window, ( int(C.WIDTH*self.fix), int(C.HEIGHT*self.fix) )), self.offset)

    def start(self):
        self.bars = []
        quantity = 50
        dif = 50 / quantity
        width = C.WIDTH / quantity - dif
        for i in range(quantity):
            self.bars.append(my_objects.Bar(random.randint(1,C.HEIGHT), [i * (width + dif) ,0], width))
        
        # Variables for loop
        self.do = True
        self.iteration = 0
        self.current = 0
        self.remove_last_color = False


if __name__ == "__main__":
    game = Game()
    game.run()    

pygame.quit()