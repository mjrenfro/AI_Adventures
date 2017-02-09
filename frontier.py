#Code from online description of Priority Queues in Python

from heapq import *
import itertools
from collections import defaultdict

class Frontier:
    def __init__(self, start, goal):
        self.pq=[]
        self.entry_finder={}
        self.REMOVED= '<removed-task>'
        self.counter=itertools.count()
        self.start=start
        self.goal=goal

    def add_task(self,task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            remove_task(task)
        count=next(self.counter)
        entry=[priority, count, task]
        self.entry_finder[task]=entry
        heappush(self.pq, entry)



    def remove_task(self,task):
        'Mark an existing task as REMOVED. Raise KeyError if not found.'
        entry=self.entry_finder.pop(task)
        entry[-1]=self.REMOVED

    def pop_task(self):
        'Removed and return the lowest priority task. Raise KeyError if empty'
        while self.pq:
            priority, count, task= heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return priority,task
            raise KeyError('pop from an empty priority queue')
