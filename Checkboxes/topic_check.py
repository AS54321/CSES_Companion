import tkinter as tk
import config
from Data.db_queries import fetch_problems
from Regions.content import problem

class topic_check(tk.Checkbutton):
    def __init__(self, parent, label, sect, tid):
        self.stat = tk.BooleanVar()
        self.stat.set(False)
        self.sect = sect
        self.tid = tid
        super().__init__(parent,variable=self.stat,text=label,command=self.update_output, width=24,anchor='w', bg=config.buttoncolor)
        self.pack(anchor='w',padx=1.5,pady=2.4)


    def update_output(self):
        sect = self.sect
        flag = config.unsolved_only
        if(self.stat.get()):
            if(sect.prob_list==None):
                probs = fetch_problems(self.tid)
                sect.prob_list = {}
                for pid, title, url, sol in probs:
                    # print(f"you requested problem {title} to appear")
                    if((not sol) or (not flag)):
                        prob = problem(sect, title, url, pid, sol)
                        sect.prob_list[pid] = prob
                        

            empty = True            
            for prob in sect.prob_list.values():
                if(prob.prob_check.stat.get()):
                    if(flag):
                        prob.grid_remove()
                    else:
                        prob.grid()
                else:
                    empty = False
                    prob.grid()
            if(not(flag and empty)):
                sect.grid()
                

            # print(f"you requested topic {tid} to appear")
            
            # self.stat.set(True)
            

        else:
            sect.grid_remove()
            # self.stat.set(False)