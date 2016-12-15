import Tkinter as tk
from Othello import *

class OthelloGUI:
    def __init__(self, master):
        self.gamehost = Othello(False)
        
        self.width = 700
        self.height = 700
        self.guiwidth = 700
        self.guiheight = 800
        
        self.widthgap = self.width / self.gamehost.board_width
        self.heightgap = self.width / self.gamehost.board_height
        
        self.master = master
        self.master.title('Othello')
        self.master.resizable(width=False, height=False)

        """
        Centralised window
        """
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - self.guiwidth)/2
        y = (sh - self.guiheight)/2
        self.master.geometry('%dx%d+%d+%d' % (self.guiwidth, self.guiheight, x, y))
        
        """
        Draw game board
        """
        self.canvas = tk.Canvas(self.master, bg="#FFD300", width=self.width, height=self.width)
        self.canvas.bind('<Button-1>', self.click_on_board)
        self.canvas.pack()

        i = 0
        while i < self.gamehost.board_width:
            self.canvas.create_line(i * self.widthgap, 0, i * self.widthgap, self.height)
            i += 1
        
        j = 0
        while j < self.gamehost.board_height:
            self.canvas.create_line(0, j * self.heightgap, self.width, j * self.heightgap)
            j += 1
        
        """
        Initialize game board with pieces
        """
        self.refresh_game_board()
        
        """
        Function board
        """
        self.funcboard = tk.Frame(self.master)
        self.funcboard.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.aifirst = tk.IntVar()
        self.firstcb = tk.Checkbutton(self.funcboard, text="AI first", variable=self.aifirst, command=self.click_on_change_first_hand)
        self.undobtn = tk.Button(self.funcboard, text='Undo', command=self.click_on_undo)
        self.startbtn = tk.Button(self.funcboard, text='Start', command=self.click_on_start)
        
        self.funcboard.columnconfigure(0, weight=1)
        self.funcboard.columnconfigure(1, weight=1)
        self.funcboard.columnconfigure(2, weight=1)
        self.funcboard.columnconfigure(3, weight=1)

        self.firstcb.grid(row=1, column=0)
        self.startbtn.grid(row=1, column=1)
        self.undobtn.grid(row=1, column=2)

    def refresh_game_board(self):
        self.canvas.delete("all")
        i = 0
        while i < self.gamehost.board_width:
            self.canvas.create_line(i * self.widthgap, 0, i * self.widthgap, self.height)
            i += 1
        
        j = 0
        while j < self.gamehost.board_height:
            self.canvas.create_line(0, j * self.heightgap, self.width, j * self.heightgap)
            j += 1
            
        for i in xrange(self.gamehost.board_width):
            for j in xrange(self.gamehost.board_height):
                if self.gamehost.board[i][j] != self.gamehost.empty_cell:
                    self.draw_piece(self.gamehost.board[i][j], i, j)
                    
    def draw_piece(self, player, x, y):
        color = 'black' if player == self.gamehost.black_piece else 'white'
        tx = (x + 0.5) * self.widthgap
        ty = (y + 0.5) * self.heightgap
        tr = 0.9*0.5 * self.widthgap
        self.canvas.create_oval(tx-tr, ty-tr, tx+tr,ty+tr, fill=color, width=1)
    
    def click_on_board(self, event):
        x = int(event.x / self.widthgap)
        y = int(event.y / self.heightgap)
        self.gamehost.make_a_move(x, y)
        self.refresh_game_board()
        print 'Make a move on {0}-{1}'.format(x, y)
    
    def click_on_change_first_hand(self):
        print "AI first : {0}".format(self.aifirst.get())
    
    def click_on_start(self):
        print 'Start'
        
    def click_on_undo(self):
        print 'Undo'
    

        
root = tk.Tk()
othello_gui = OthelloGUI(root)
root.mainloop()

