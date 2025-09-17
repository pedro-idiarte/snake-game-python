from tkinter import *
import random

class Food:

    def __init__(self, canvas, game_width, game_height, space_size, food_color):
        self.canvas = canvas
        self.game_width = game_width
        self.game_height = game_height
        self.space_size = space_size
        self.food_color = food_color
        
        x = random.randint(0, (self.game_width // self.space_size) - 1) * self.space_size
        y = random.randint(0, (self.game_height // self.space_size) - 1) * self.space_size

        self.coordinates = [x, y]
        self.canvas.create_oval(x, y, x + self.space_size, y + self.space_size, 
                               fill=self.food_color, tag="food")