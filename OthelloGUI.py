import Tkinter as tk
from Othello import *

class OthelloGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Othello')
        self.gamehost = Othello(False)
        
        self.centerWindow()

    def centerWindow(self):
        w = 700
        h = 800
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
root = tk.Tk()
othello_gui = OthelloGUI(root)
root.mainloop()