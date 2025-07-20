import tkinter as tk
from tkinter import ttk

def insert_text():
    text_widget.insert(tk.END, "Hello! This is a line of text.\n")

def get_text():
    content = text_widget.get("1.0", tk.END)  # From line 1, char 0 to end
    print("Text content:\n", content)

def clear_text():
    text_widget.delete("1.0", tk.END)

root = tk.Tk()
root.title("Text Widget Example")

# Create frame for layout
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

# Configure resizing
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

# Create Text widget
text_widget = tk.Text(frame, wrap="word", height=10, width=50)
text_widget.grid(row=0, column=0, sticky="nsew")

# Add vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
text_widget.configure(yscrollcommand=scrollbar.set)

# Buttons
btn_frame = ttk.Frame(frame)
btn_frame.grid(row=1, column=0, columnspan=2, pady=10)

ttk.Button(btn_frame, text="Insert Text", command=insert_text).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Get Text", command=get_text).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Clear Text", command=clear_text).grid(row=0, column=2, padx=5)

root.mainloop()
