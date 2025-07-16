import tkinter as tk
from tkinter import ttk
class sidebar(tk.Frame):
    def __init__(self, parent, on_topic_select):
        super().__init__(parent, relief="ridge")
        self.on_topic_select = on_topic_select

        ttk.Label(self, text="Topics").pack(anchor="w")

        self.topic_list = tk.Listbox(self)
        self.topic_list.pack(fill="both", expand=True)


        topics = ["Dynamic Programming", "Sorting"]
        for topic in topics:
            self.topic_list.insert(tk.END, topic)

        self.topic_list.bind("<<ListboxSelect>>", self._on_select)

    def _on_select(self, event):
        selection = self.topic_list.curselection()
        if selection:
            topic = self.topic_list.get(selection[0])
            self.on_topic_select(topic)