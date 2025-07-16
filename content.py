import tkinter as tk
from tkinter import ttk
import webbrowser
import json

class mainContent(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10, relief="ridge")
        ttk.Label(self, text="Problems").pack(anchor="w")

        self.problem_list = tk.Listbox(self)
        self.problem_list.pack(fill="both", expand=True)

        self.mark_button = ttk.Button(self, text="✅ Mark as Solved", command=self.mark_solved)
        self.mark_button.pack(pady=5)

        self.problem_list.bind("<Double-Button-1>", self._open_link)

        self.links = []
        self.ids = []  # store IDs for updating progress
        self.progress = self._load_progress()

    def _load_progress(self):
        try:
            with open("progress.json") as f:
                return json.load(f)
        except:
            return {}

    def _save_progress(self):
        with open("progress.json", "w") as f:
            json.dump(self.progress, f, indent=2)

    def display_problems(self, problems):
        self.problem_list.delete(0, tk.END)
        self.links = []
        self.ids = []

        for p in problems:
            label = f"✅ {p['title']}" if p["id"] in self.progress else f"❌ {p['title']}"
            self.problem_list.insert(tk.END, label)
            self.links.append(p["url"])
            self.ids.append(p["id"])

    def mark_solved(self):
        selection = self.problem_list.curselection()
        if not selection:
            return

        idx = selection[0]
        problem_id = self.ids[idx]
        self.progress[problem_id] = True
        self._save_progress()

        # Refresh current list item text
        title = self.problem_list.get(idx).lstrip("❌✅ ").strip()
        self.problem_list.delete(idx)
        self.problem_list.insert(idx, f"✅ {title}")
        self.problem_list.selection_set(idx)

    def _open_link(self, event):
        index = self.problem_list.curselection()
        if index:
            webbrowser.open(self.links[index[0]])
