import tkinter as tk 
from eye import Eyes
from mouth import Mouth
import time


class ExpressionAnimation: 
    def __init__(self, canvas): 
        self.canvas = canvas 
        self.eyes = Eyes(self.canvas, width=600, height=600)
        self.mouth = Mouth(self.canvas, width=600, height=600)

    def smiling(self): 
        self.canvas.delete("all")
        self.eyes.arc_eye()
        self.mouth.bowl()

    def laughing(self): 
        self.canvas.delete("all")
        self.eyes.arc_eye()
        self.mouth.laugh()

    def angry(self): 
        self.canvas.delete("all")
        self.eyes.watermelon_eye()
        self.mouth.upward_spike()

    def joy(self): 
        self.canvas.delete("all")
        self.eyes.crescent()
        self.mouth.full_bowl()

    def dead_stare(self): 
        self.canvas.delete("all")
        self.eyes.round_eye()
        self.mouth.rect_mouth()
    
    def normal(self):
        self.canvas.delete("all")
        self.eyes.round_eye()
        self.mouth.rect_mouth()

    def blinking(self):
        num_blinks = 2  # You can adjust the number of blinks
        blink_duration = 1  # Adjust the duration of each blink

        for _ in range(num_blinks):
            self.canvas.delete("all")
            self.eyes.round_eye()
            self.mouth.rect_mouth()
            self.canvas.update()  # Update the canvas to show the current frame
            time.sleep(blink_duration)

            self.canvas.delete("all")
            self.eyes.closed_eye()  # Assuming you have a method to define the normal eye state
            self.mouth.rect_mouth()
            self.canvas.update()
            time.sleep(blink_duration)



        



