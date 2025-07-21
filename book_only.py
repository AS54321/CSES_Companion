import tkinter as tk
import config
from db_queries import check_notes
import bridge

sections = bridge.sections

def action(self):
    config.bookmarked_only = not config.bookmarked_only
    book_onl = config.bookmarked_only
    for sect in sections.values():
        # print(f"{sect.title} 's list is {sect.prob_list}")
        empty = True
        if(sect.prob_list!=None):
            for prob in sect.prob_list.values():
                if(check_notes(prob.prob_check.pid)):
                    if(book_onl):
                        prob.grid_remove()
                    else:
                        prob.grid()
                else:
                    empty = False
                    prob.grid()
            
        if(sect.topic_check.stat.get()):
            if(empty and book_onl):
                sect.grid_remove()
            else:
                sect.grid()
                
    if(book_onl):
        self.configure(text='View All')
    else:
        self.configure(text='View Bookmarks')
