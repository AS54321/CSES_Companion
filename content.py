import tkinter as tk
from tkinter import ttk
import webbrowser


class mainContent(tk.Frame):
    def __init__(self,parent):
        super().__init__(master=parent, background='#ffff00')
        self.grid(column=0, row=1, sticky=tk.E+tk.W)
        self.columnconfigure(0, weight=1)

        ttk.Label(self, text="Problems").pack(anchor="w")

        self.problem_list = tk.Listbox(self)
        self.problem_list.pack(fill="both", expand=True)

        self.problem_list.bind("<Double-Button-1>", self._open_link)

        self.links = []  

    def display_problems(self, problems):
        self.problem_list.delete(0, tk.END)
        self.links = []

        for p in problems:
            self.problem_list.insert(tk.END, p["title"])
            self.links.append(p["url"])

    def _open_link(self, event):
        index = self.problem_list.curselection()
        if index:
            webbrowser.open(self.links[index[0]])