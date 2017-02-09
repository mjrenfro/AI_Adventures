'''Implements Uniform-Cost Search to report the optimal length
and the distance between each node in the solution path'''

import sys
from collections import defaultdict #for the graph
from frontier import Frontier #for uniform_cost_search frontier
import unittest #for testing

def explore(graph,frontier):
    #hack way to ensure the first pop is treated like a tuple of tuples, cause why classes?
    frontier.add_task(((frontier.start,0),), 0)

    while frontier.entry_finder:
        cost,path=frontier.pop_task()

        head=path[len(path)-1][0]

        if (head==frontier.goal):
            return path,cost

        #not going to backtrack
        for edge in [e for e in graph[head] if e[0] not in [x[0] for x in path]]:
            frontier.add_task(tuple(list(path)+[(edge[0],edge[1])]),cost+edge[1] )

    #frontier is none, so there is not a solution
    return None, "infinity"

def print_path(path,cost):
    if path ==None:
        print("\ndistance: ",cost)
        print("route: ")
        print ("none")
        return
    print("\ndistance: ",cost, "km")
    print("route: ")

    path=list(path)
    prev=path.pop(0)

    while path:
        curr=path.pop(0)
        #TODO: Figure out how to do this correctly with string formatting
        print(prev[0]+" to "+curr[0]+", "+str(curr[1])+ " km")
        prev=curr

#reads in all variables for the search and returns them
def readin():
    #name of exe, filename, start, goal
    if len(sys.argv)<4:
        sys.exit('Too few arguments')

    start=sys.argv[2]
    goal=sys.argv[3]

    graph=defaultdict(list)

    with open (sys.argv[1]) as f:
        for line in f.readlines():
            a,b, dist=line.split()
            if a =="END":
                break
            graph[b].append((a, int(dist)))
            graph[a].append((b, int(dist)))

    return graph, start, goal

class TestUCS(unittest.TestCase):
    def test_results(self):
        sys.argv=['something', 'input1.txt', 'Luebeck', 'Stuttgart']
        graph, start, end=readin()
        f=Frontier(start, end)
        path,cost = explore(graph, f)
        print_path(path,cost)



    #does readin() consider all parts of the graph
    def test_readin(self):
        sys.argv=['something', 'test_input.txt', 'S', 'G']
        expected=defaultdict(list)

        expected['S'].append(('A',1))
        expected['S'].append(('G',12))

        expected['A'].append(('S',1))
        expected['A'].append(('B',3))
        expected['A'].append(('C', 1))

        expected['B'].append(('A', 3))
        expected['B'].append(('D', 3))

        expected['C'].append(('A',1))
        expected['C'].append(('D',1))
        expected['C'].append(('G',2))

        expected['D'].append(('C',1))
        expected['D'].append(('B',3))
        expected['D'].append(('G',3))

        expected['G'].append(('D',3))
        expected['G'].append(('C',2))
        expected['G'].append(('S',12))

        for key in expected:
            expected[key].sort()

        #sorts all the keys
        graph, start, goal=readin()
        result=sorted(graph.items())
        #sorts the contents of each map
        r_dict=defaultdict(list)
        for r in result:
            r_dict[r[0]]=r[1]

        for key in r_dict:
            r_dict[key].sort()

        self.assertEqual(expected, r_dict)

    #is the correct path returned when possible
    def test_possible_path(self):
        sys.argv=['something', 'test_input.txt', 'S', 'G']
        graph, start, end=readin()
        f=Frontier(start, end)

        path,cost = explore(graph, f)
        expected_path=(('S',0), ('A',1), ('C',1), ('G',2))
        self.assertEqual(expected_path, path)
    def test_possible_cost(self):
        sys.argv=['something', 'test_input.txt', 'S', 'G']
        graph, start, end=readin()
        f=Frontier(start, end)

        path,cost = explore(graph, f)
        expected_cost=4
        self.assertEqual(expected_cost,cost)

    #is the appropriate indicator returned when path is impossible
    def test_impossible_path(self):
        sys.argv=['something', 'island_input.txt', 'S', 'P']
        graph, start, end=readin()
        f=Frontier(start, end)

        path,cost = explore(graph, f)
        expected_path=None
        expected_cost="infinity"
        self.assertEqual(expected_cost, cost)
        self.assertEqual(expected_path, path)
