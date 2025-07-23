from Data.db_queries import fetch_notes, db_update_notes
import tkinter as tk
from tkinter import ttk


class notes_feat(tk.Button):
    def __init__(self,parent,pid, col):
        super().__init__(master=parent, text='✍️', command= lambda : self.notetake(pid))
        self.grid(row=0, column=col, sticky='e')
    
    def notetake(self,pid):
        note = fetch_notes(pid)
        note_win = tk.Toplevel(self.master)
        note_win.title("Add notes")
        note_win.resizable(False,False)
        notes_text = tk.Text(note_win, wrap="word")
        notes_text.grid(row=0, column=0, sticky="nsew")
        notes_text.insert("1.0", note)

        btn_frame = ttk.Frame(note_win)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=10)
        butt = ttk.Button(btn_frame, text="Save and Continue", command=lambda: (self.insert(note, pid,notes_text.get("1.0", tk.END)),note_win.destroy()))
        butt.grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Clear Text", command=lambda: (notes_text.delete("1.0", tk.END), self.insert(note, pid,''))).grid(row=0, column=2, padx=5)

    def insert(self,note, pid,content):
        if(note==content): return
        if(content=='\n'): content = '' 
        # print("something")
        db_update_notes(content,pid)