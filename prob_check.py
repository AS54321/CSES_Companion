import tkinter as tk
from db_queries import db_toggle_prob

class prob_check(tk.Checkbutton):
    def __init__(self, parent, pid, stat,col):
        self.stat = tk.BooleanVar()
        self.stat.set(stat)
        self.pid = pid
        super().__init__(master=parent,variable=self.stat,command=self.update_output)
        self.grid(row=0, column=col,sticky='e')

    def update_output(self):
        db_toggle_prob(self.pid)
        if(self.stat.get()):
            self.master.configure(background='lightblue')
        else:
            self.master.configure(background='#00ff00')