class Eyes:
    def __init__(self, canvas, width, height):
        self.canvas = canvas

        """Left eye coords"""
        self.left_start_x = None 
        self.left_start_y = None 

        self.left_end_x = None 
        self.left_end_y = None 

        """Right eye coords"""
        self.right_start_x = None 
        self.right_start_y = None 

        self.right_end_x = None 
        self.right_end_y = None 

        """taking 1/12 as one unit"""
        self.width = width / 12
        self.height = height / 12

        """Initiate left and right eye"""
        self.right_eye = None
        self.left_eye = None

    def arc_eye(self):
        self.left_start_x = self.width
        self.left_start_y = self.height * 2
        self.left_end_x = self.width * 5
        self.left_end_y = self.height * 6

        self.right_start_x = self.width * 7
        self.right_start_y = self.height * 2
        self.right_end_x = self.width * 11
        self.right_end_y = self.height * 6
        
        self.left_eye = self.canvas.create_arc(self.left_start_x, self.left_start_y, self.left_end_x, self.left_end_y,
                                               start=0, extent=180, fill="blue", outline="blue")
        self.right_eye = self.canvas.create_arc(self.right_start_x, self.right_start_y, self.right_end_x, self.right_end_y,
                                                start=0, extent=180, fill="blue", outline="blue")

    def round_eye(self):
        self.left_start_x = self.width
        self.left_start_y = self.height 
        self.left_end_x = self.width * 5
        self.left_end_y = self.height * 5

        self.right_start_x = self.width * 7
        self.right_start_y = self.height
        self.right_end_x = self.width * 11
        self.right_end_y = self.height * 5

        self.left_eye = self.canvas.create_oval(self.left_start_x, self.left_start_y, self.left_end_x, self.left_end_y, fill="blue", outline="blue")
        self.right_eye = self.canvas.create_oval(self.right_start_x, self.right_start_y, self.right_end_x, self.right_end_y, fill="blue", outline="blue")


    def closed_eye(self):
        self.left_start_x = self.width
        self.left_start_y = self.height * 3
        self.left_end_x = self.width * 5
        self.left_end_y = self.height * 3.5

        self.right_start_x = self.width * 7
        self.right_start_y = self.height * 3
        self.right_end_x = self.width * 11
        self.right_end_y = self.height * 3.5

        self.left_eye = self.canvas.create_rectangle(self.left_start_x, self.left_start_y, self.left_end_x, self.left_end_y, fill="blue", outline="blue")
        self.right_eye = self.canvas.create_rectangle(self.right_start_x, self.right_start_y, self.right_end_x, self.right_end_y, fill="blue", outline="blue")


    def watermelon_eye(self):
        self.left_start_x = self.width
        self.left_start_y = self.height
        self.left_end_x = self.width * 5
        self.left_end_y = self.height * 5

        self.right_start_x = self.width * 7
        self.right_start_y = self.height
        self.right_end_x = self.width * 11
        self.right_end_y = self.height * 5

        self.left_eye = self.canvas.create_arc(self.left_start_x, self.left_start_y, self.left_end_x, self.left_end_y, start=-45, extent=-180, fill="blue", outline="blue")
        self.right_eye = self.canvas.create_arc(self.right_start_x, self.right_start_y, self.right_end_x, self.right_end_y, start=225, extent=180, fill="blue", outline="blue")

    def crescent(self):
        self.left_start_x = self.width
        self.left_start_y = self.height * 3
        self.left_end_x = self.width * 5
        self.left_end_y = self.height * 6

        self.right_start_x = self.width * 7
        self.right_start_y = self.height * 3
        self.right_end_x = self.width * 11
        self.right_end_y = self.height * 6

        self.left_eye = self.canvas.create_arc(self.left_start_x, self.left_start_y, self.left_end_x, self.left_end_y, start=-20, extent=220, fill="blue", outline="blue")
        self.right_eye = self.canvas.create_arc(self.right_start_x, self.right_start_y, self.right_end_x, self.right_end_y, start=-20, extent=220, fill="blue", outline="blue")



