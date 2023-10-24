class Mouth:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width / 8
        self.height = height / 8

        self.mouth = None 

    def rect_mouth(self): 
        self.mouth = self.canvas.create_rectangle(self.width * 3, self.height * 4, self.width * 5, self.height * 4.5, fill="blue", outline="blue")

    def bowl(self):
        self.mouth = self.canvas.create_arc(self.width * 3, self.height * 4, self.width * 5, self.height * 5,
                                            start=0, extent=-180, style="arc", outline="blue", width="20")
        
    def flip_bowl(self): 
        self.mouth = self.canvas.create_arc(self.width * 3, self.height * 4, self.width * 5, self.height * 5,
                                            start=0, extent=180, style="arc", outline="blue", width="20")
        
    def full_bowl(self): 
        self.mouth = self.canvas.create_arc(self.width * 3, self.height * 4, self.width * 5, self.height * 5,
                                            start=0, extent=-180, style="chord", outline="blue", fill="blue", width="20")
        
        
