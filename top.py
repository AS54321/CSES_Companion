import tkinter as tk
from tkinter import ttk
from bridge import unsolved, bookmark
from db_queries import close_db
class topbar(tk.Frame):
    def __init__(self,parent):
        super().__init__(master=parent, height=20, background='#00ffff')

        self.columnconfigure(0, weight=1)

        bookmark(self).grid(row=0, column=0, stick='e')
        unsol = unsolved(self)
        unsol.grid(row=0, column=1, stick='e')
        quit = ttk.Button(master=self, text="Quit", command=lambda: (close_db(), parent.destroy()))
        quit.grid(row=0, column=2, stick='e')

