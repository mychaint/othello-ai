import Tkinter as tk
from Othello import *

class OthelloGUI:
    def __init__(self, master):
        self.gamehost = Othello(False)
        self.ai = None
        self.vsai = tk.IntVar()
        self.aifirst = tk.IntVar()
        self.current_piece = self.gamehost.black_piece
        self.player = 'P1'
        
        self.width = 500
        self.height = 500
        self.guiwidth = 500
        self.guiheight = 600
        
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
        self.statuboard = tk.Frame(self.master)
        self.statuboard.pack(fill=tk.X, side=tk.TOP)
        self.funcboard = tk.Frame(self.master)
        self.funcboard.pack(fill=tk.X, side=tk.TOP)
        
        self.statuslabel = tk.Label(self.statuboard, text='Status: ')
        self.modelabel = tk.Label(self.statuboard, text='P V P')
        self.turnlabel = tk.Label(self.statuboard, text='P first')
        self.victorylabel = tk.Label(self.statuboard, text='Victor: ')        

        self.aicb = tk.Checkbutton(self.funcboard, text="Vs. AI", variable=self.vsai, command=self.click_on_change_mode)
        self.firstcb = tk.Checkbutton(self.funcboard, text="AI first", variable=self.aifirst, command=self.click_on_change_first_hand)
        self.undobtn = tk.Button(self.funcboard, text='Undo', command=self.click_on_undo)
        self.startbtn = tk.Button(self.funcboard, text='New Game', command=self.click_on_start)
        
        self.statuboard.columnconfigure(0, weight=1)
        self.statuboard.columnconfigure(1, weight=1)
        self.statuboard.columnconfigure(2, weight=1)
        self.statuboard.columnconfigure(3, weight=1)
        self.funcboard.columnconfigure(0, weight=1)
        self.funcboard.columnconfigure(1, weight=1)
        self.funcboard.columnconfigure(2, weight=1)
        self.funcboard.columnconfigure(3, weight=1)
        
        self.statuslabel.grid(row=1, column=0)
        self.modelabel.grid(row=1, column=1)
        self.turnlabel.grid(row=1, column=2)
        self.victorylabel.grid(row=1, column=3)
        
        self.aicb.grid(row=1, column=0)
        self.firstcb.grid(row=1, column=1)
        self.startbtn.grid(row=1, column=2)
        self.undobtn.grid(row=1, column=3)

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
    
    """
    GUI Events
    """        
    def click_on_board(self, event):
        if self.gamehost.isstarted:
            x = int(event.x / self.widthgap)
            y = int(event.y / self.heightgap)
            
            if self.gamehost.make_a_move(self.current_piece, x, y):
                self.refresh_game_board()
                self.current_piece = self.gamehost.black_piece if self.current_piece == self.gamehost.white_piece else self.gamehost.white_piece
            else:
                print 'Bad Move'
    
    def click_on_change_mode(self):
        print "mode {0}".format(self.vsai.get())
        
    def click_on_change_first_hand(self):
        print "AI first : {0}".format(self.aifirst.get())
    
    def click_on_start(self):
        self.gamehost.start_game()
        self.refresh_game_board()
        
    def click_on_undo(self):
        print 'Undo'
    
    def initialisedAI(self):
        if self.gamehost.vsai:
            self.gamehost.initialiseAI()
        else:
            self.gamehost.deleteAI()
        
root = tk.Tk()
othello_gui = OthelloGUI(root)
root.mainloop()

