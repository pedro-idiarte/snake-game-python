from tkinter import *

class Snake:

    def __init__(self, canvas, space_size, body_parts, snake_color):
        self.canvas = canvas
        self.space_size = space_size
        self.body_size = body_parts
        self.snake_color = snake_color
        self.coordinates = []
        self.squares = []

        for i in range(0, body_parts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + self.space_size, y + self.space_size, 
                                                 fill=self.snake_color, tag="snake")
            self.squares.append(square)