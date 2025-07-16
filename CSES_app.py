import tkinter as tk
from tkinter import ttk
from side import sidebar
from top import topbar
from content import mainContent
import json

class CSES_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSES Problem Browser")
        self.geometry("700x500")

        
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        
        self.sidebar = sidebar(self, self.load_problems)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.main = mainContent(self)
        self.main.grid(row=0, column=1, sticky="nsew")

    def load_problems(self, topic):
        try:
            with open("cses_problems_by_topic.json") as f:
                data = json.load(f)
        except Exception as e:
            print("Error loading JSON:", e)
            return

        problems = data.get(topic, [])
        self.main.display_problems(problems)
