import pygame
import numpy as np
import sys
from Constants import SCREEN_SIZE, FONT

# I made this class for easy text managing lol
class TextBox:
    def __init__(self, text:str="Placeholder", position:tuple[int,int]=np.array(SCREEN_SIZE)/2):
        self.text = text
        self.font = FONT
        self.color: tuple[int,int,int] = (255, 255, 255)
        self.position: tuple[int,int] = position

        self.surface = self.font.render(text, True, self.color)
        self.rect = self.surface.get_rect(center=self.position)

    def setText(self, text: str) -> None:
        self.surface = self.font.render(text, True, self.color)
        self.rect = self.surface.get_rect(center=self.position)
    
    def setPosition(self, position: tuple[int,int]) -> None:
        self.position = position
        self.rect = self.surface.get_rect(center=position)

    def draw(self, screen) -> None:
        screen.blit(self.surface, self.rect)