import tkinter as tk 

class Mouth: 
	def __init__(self, canvas, x, y): 
		self.canvas = canvas
		self.x = x
		self.y = y 

	def draw_mouth(self): 
		self.canvas.