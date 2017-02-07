#reading in file and populating graph
import sys
from collections import defaultdict
import json

graph=defaultdict(list)

if len(sys.argv)<2:
    sys.exit('Too few arguments')

# print (sys.argv)
with open (sys.argv[1]) as f:
    for line in f.readlines():
        a,b, dist=line.split()
        if a =="END":
            break
        graph[a].append((b, int(dist)))

print(json.dumps(graph, sort_keys=True, indent=4))
