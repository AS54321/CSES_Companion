import tkinter as tk
from tkinter import ttk
import random
import json


class sidebar(tk.Frame):

    def select_specific_problem(self, name):
        for i in range(self.master.main.problem_list.size()):
            if self.master.main.problem_list.get(i) == name:
                self.master.main.problem_list.selection_clear(0, tk.END)
                self.master.main.problem_list.selection_set(i)
                self.master.main.problem_list.see(i)
                break

    def _random_problem(self):
        try:
            with open("cses_problems_by_topic.json") as f:
                data = json.load(f)
        except Exception as e:
            print("Failed to load JSON:", e)
            return

        all_topics = list(data.keys())
        if not all_topics:
            return

        topic = random.choice(all_topics)
        problem = random.choice(data[topic])

        self.on_topic_select(topic)
        self.after(100, lambda: self.select_specific_problem(problem["name"]))

    def __init__(self, parent, on_topic_select):
        super().__init__(parent, relief="ridge")
        self.on_topic_select = on_topic_select

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)  # Let listbox expand

        # Random button
        self.random_btn = ttk.Button(self, text="Random Problem", command=self._random_problem)
        self.random_btn.grid(row=0, column=0, sticky="ew", pady=5)

        # Topics label
        ttk.Label(self, text="Topics").grid(row=1, column=0, sticky="w")

        # Topics listbox
        self.topic_list = tk.Listbox(self)
        self.topic_list.grid(row=2, column=0, sticky="nsew")

        topics = ["Dynamic Programming", "Sorting"]
        for topic in topics:
            self.topic_list.insert(tk.END, topic)

        self.topic_list.bind("<<ListboxSelect>>", self._on_select)

    def _on_select(self, event):
        selection = self.topic_list.curselection()
        if selection:
            topic = self.topic_list.get(selection[0])
            self.on_topic_select(topic)
