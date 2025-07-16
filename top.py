import tkinter as tk
from tkinter import ttk


class topbar(tk.Frame):
    def __init__(self,parent):
        super().__init__(master=parent, height=20, background='#00ffff')
        self.grid(column=0,sticky=tk.E+tk.W)
        self.columnconfigure(0, weight=1)
        quit = ttk.Button(master=self   , text="Quit", command=parent.destroy)
        quit.grid(row=0, column=0, sticky=tk.E+tk.W)
