from heapq import *
import itertools
from collections import defaultdict

class Frontier:
    def __init__(self):
        self.pq=[]
        self.entry_finder={}
        self.REMOVED= '<removed-task>'
        self.counter=itertools.count()

    def add_task(task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            remove_task(task)
        count=next(self.counter)
        entry=[priority, count, task]
        self.entry_finder[task]=entry
        heappush(self.pq, entry)

    def remove_task(task):
        'Mark an existing task as REMOVED. Raise KeyError if not found.'
        entry=self.entry_finder.pop(task)
        entry[-1]=self.REMOVED

    def pop_task():
        'Removed and return the lowest priority task. Raise KeyError if empty'
        while self.pq:
            priority, count, task= heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
            raise KeyError('pop from an empty priority queue')
# test_map=defaultdict(list)
# test_map['Denver'].append(('FOCO', 12))
# test_map['Denver'].append(('Bayfield', 2131))
# test_map['Denver'].append(('Pagosa', 123))
# for item in test_map['Denver']:
#     add_task(item, item[1])
#
# while pq:
#     print(pop_task())
