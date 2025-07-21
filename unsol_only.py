import config
import bridge
import tkinter as tk

sections = bridge.sections

def action(self):
    config.unsolved_only = not config.unsolved_only
    unsol_onl = config.unsolved_only
    for sect in sections.values():
        # print(f"{sect.title} 's list is {sect.prob_list}")
        empty = True
        if(sect.prob_list!=None):
            for prob in sect.prob_list.values():
                if(prob.prob_check.stat.get()):
                    if(unsol_onl):
                        prob.grid_remove()
                    else:
                        prob.grid()
                else:
                    empty = False
                    prob.grid()
            
        if(sect.topic_check.stat.get()):
            if(empty and unsol_onl):
                sect.grid_remove()
            else:
                sect.grid()
                
    if(unsol_onl):
        self.configure(text='View All')
    else:
        self.configure(text='View Unsolved')