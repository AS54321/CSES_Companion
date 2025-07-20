from content import topic_sect
import tkinter.ttk as ttk
from db_queries import fetch_topics, check_notes
import config
from topic_check import topic_check

sections = {}

class unsolved(ttk.Button):
    def __init__(self,parent):
        super().__init__(master=parent, text='View Unsolved', command=self.action)
    
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

class bookmark(ttk.Button):
    def __init__(self,parent):
        super().__init__(master=parent, text='View Bookmarked', command=self.action)
    
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


def initialize(side, main):
    topic_names = fetch_topics()
    for tid,name in topic_names:
        temp = topic_sect(name, main, tid)
        sections[tid] = temp
        temp.topic_check = topic_check(side, name, sections[tid], tid)
