import Tkinter as tk
import Othello

class OthelloGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Othello')
        self.centerWindow()
    
    def centerWindow(self):
        w = 800
        h = 600
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
root = tk.Tk()
othello_gui = OthelloGUI(root)
root.mainloop()