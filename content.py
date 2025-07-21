import tkinter as tk
from prob_check import prob_check
from notes_button import notes_feat
import webbrowser
from config import maincolor, contentcolor, hovercolor

class mainContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, background=maincolor)

        # Configure this frame to expand properly
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self, borderwidth=0, background=maincolor)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Create scrollable frame inside the canvas
        self.scrollable_frame = tk.Frame(self.canvas, background=maincolor, padx=8, pady=8)
        self.canvas_frame_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Update scrollregion and width binding
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.canvas_frame_id, width=e.width - self.scrollbar.winfo_width())
        )

        # Cross-platform mousewheel scroll
        def _on_mouse_scroll(event):
            if event.num == 4 or event.delta > 0:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5 or event.delta < 0:
                self.canvas.yview_scroll(1, "units")

        self.canvas.bind_all("<Button-4>", _on_mouse_scroll)
        self.canvas.bind_all("<Button-5>", _on_mouse_scroll)
        self.canvas.bind_all("<MouseWheel>", _on_mouse_scroll)

        self.scrollable_frame.columnconfigure(0, weight=1)


class topic_sect(tk.LabelFrame):

    def __init__(self, title, parent, i=0):
        super().__init__(master=parent,text=title, background=contentcolor,bd=4, padx=5, pady=5, relief="raised")
        self.columnconfigure(0, weight=1)
        self.title = title
        self.grid(sticky='ew', padx=3, pady=3, row=i)
        self.grid_remove()
        self.prob_list = None


class problem(tk.Frame):

    def __init__(self, parent, title, url, pid, sol):
        super().__init__(master=parent, padx=2, pady=2,cursor='hand2',bg=contentcolor)
        name = tk.Label(master=self, text=title, fg='blue')
        name.grid(row=0, sticky='w')
        self.columnconfigure(0, weight=1)
        self.prob_check = prob_check(self, pid, sol,0)
        notes_feat(self, pid,1)
        self.grid_configure(sticky='ew')
        self.bind('<Double-Button-1>',lambda e: webbrowser.open_new(url))
        self.bind('<Button-1>',lambda e: self.prob_check.invoke())
        self.bind("<Enter>", lambda e : self.config(bg=hovercolor))
        self.bind("<Leave>", lambda e : self.config(bg=contentcolor))

