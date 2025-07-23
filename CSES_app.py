import tkinter as tk
from tkinter import ttk
from Regions.side import sidebar
from Regions.top import topbar
from Regions.content import mainContent
from bridge import initialize

class CSES_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSES Problem Browser")
        self.geometry("700x500")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.topbar = topbar(self)
        self.topbar.grid(row=0,columnspan=2,sticky="new")
        
        self.sidebar = sidebar(self)
        self.sidebar.grid(row = 1,column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        self.main = mainContent(self)
        self.main.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        

        initialize(self.sidebar,self.main.scrollable_frame)
