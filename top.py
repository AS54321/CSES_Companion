import tkinter as tk
from unsol_only import action as unso_action
from book_only import action as book_action
from random_prob import action as rand_action
from db_queries import close_db
from config import topcolor, buttoncolor

class topbar(tk.Frame):
    def __init__(self,parent):
        super().__init__(master=parent, height=20, background=topcolor)

        self.columnconfigure(0, weight=1)

        top_buttons(self,0,'View Random', lambda: rand_action(self.master))
        temp = top_buttons(self, 1,'View Bookmarked', lambda : book_action(temp))
        _ = top_buttons(self, 2,'View Unsolved', lambda : unso_action(_))
        top_buttons(self, 3,'Quit', lambda: (close_db(), parent.destroy()))


class top_buttons(tk.Button):
    def __init__(self,parent,col,label,action):
        super().__init__(master=parent, text=label, command=action, bg=buttoncolor)
        self.grid(row=0, stick='e', column=col)



