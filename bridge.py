from Regions.content import topic_sect
from Data.db_queries import fetch_topics
from Checkboxes.topic_check import topic_check

sections = {}

def initialize(side, main):
    topic_names = fetch_topics()
    for tid,name in topic_names:
        temp = topic_sect(name, main, tid)
        sections[tid] = temp
        temp.topic_check = topic_check(side, name, sections[tid], tid)
