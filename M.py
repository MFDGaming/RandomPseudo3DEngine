import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' # Hide pygame support message
import pygame
import time
from random import Random
import math

class M:
    px = 0.1
    py = 0.1
    pz = 0.1
        
    @staticmethod
    def draw3DLine(point_1: list, point_2: list, color: list) -> tuple:
        try:
            x1 = (point_1[0] - M.px) * (4 / ((point_1[2] - M.pz) * 0.3))
            y1 = (point_1[1] - M.py) * (4 / ((point_1[2] - M.pz) * 0.3))
            x2 = (point_2[0] - M.px) * (4 / ((point_2[2] - M.pz) * 0.3))
            y2 = (point_2[1] - M.py) * (4 / ((point_2[2] - M.pz) * 0.3))
            if (x1 >= 0 and y1 >= 0) and (x2 >= 0 and y2 >= 0):
                pygame.draw.line(M.screen, color, (x1, y1), (x2, y2), 1)
        except:
            return

    @staticmethod
    def run() -> None:
        M.screen.fill([0, 0, 0])
        for z in range(1, 100 * 2, 2):
            for x in range(0, 100 * 100, 100):
                # front
                M.draw3DLine([1.0 + x, 100.0, 3.0 + z], [100.0 + x, 100.0, 3.0 + z], [255, 0, 0])

                M.draw3DLine([100.0 + x, 100.0, 3.0 + z], [100.0 + x, 1.0, 3.0 + z], [255, 0, 0])

                M.draw3DLine([100.0 + x, 1.0, 3.0 + z], [1.0 + x, 1.0, 3.0 + z], [255, 0, 0])

                M.draw3DLine([1.0 + x, 1.0, 3.0 + z], [1.0 + x, 100.0, 3.0 + z], [255, 0, 0])

                # right
                M.draw3DLine([100.0 + x, 100.0, 3.0 + z], [100.0 + x, 100.0, 1.0 + z], [0, 255, 0])

                M.draw3DLine([100.0 + x, 100.0, 1.0 + z], [100.0 + x, 1.0, 1.0 + z], [0, 255, 0])

                M.draw3DLine([100.0 + x, 1.0, 1.0 + z], [100.0 + x, 1.0, 3.0 + z], [0, 255, 0])

                # back
                M.draw3DLine([100.0 + x, 100.0, 1.0 + z], [1.0 + x, 100.0, 1.0 + z], [0, 0, 255])

                M.draw3DLine([1.0 + x, 1.0, 1.0 + z], [100.0 + x, 1.0, 1.0 + z], [0, 0, 255])

                M.draw3DLine([1.0 + x, 1.0, 1.0 + z], [1.0 + x, 100.0, 1.0 + z], [0, 0, 255])

                # left
                M.draw3DLine([1.0 + x, 100.0, 1.0 + z], [1.0 + x, 100.0, 3.0 + z], [255, 255, 255])

                M.draw3DLine([1.0 + x, 1.0, 3.0 + z], [1.0 + x, 1.0, 1.0 + z], [255, 255, 255])
        
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            M.px -= 1
            if M.px == 0:
                M.px -= 1

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            M.px += 1
            if M.px == 0:
                M.px -= 1
                
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            M.pz -= 0.1
            if M.pz == 0:
                M.pz -= 1

        if pygame.key.get_pressed()[pygame.K_UP]:
            M.pz += 0.1
            if M.pz == 0:
                M.pz -= 1
            
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            M.py += 1

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            M.py -= 1
        
        pygame.event.pump()
        pygame.display.flip()
    
    def __init__(self) -> None:
        pygame.init()
        M.screen = pygame.display.set_mode((1024, 512))
        pygame.display.set_caption("...")
        while True:
            M.run()
M()
