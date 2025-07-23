from Data.db_queries import fetch_random
import tkinter as tk
import bridge
from Regions.content import topic_sect, problem

sections = bridge.sections
def action(parent):
        win = tk.Toplevel(parent)
        # win.geometry("600x400")
        win.title("Random")
        win.resizable(False, False)
        display_problems(win)


def display_problems(parent):
    list = []
    for sect in sections.values():
        if(sect.topic_check.stat.get()):
            list.append(sect.topic_check.tid)
    problist = fetch_random(list)

    sect = topic_sect('Random Problems', parent)
    sect.grid()

    for pid, title, url, sol in problist:
        prob = problem(sect, title, url, pid, sol)
        # prob.name.configure(width=50)
        prob.grid()
