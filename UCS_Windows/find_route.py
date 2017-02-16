from ucs import *


if __name__ =='__main__':
  graph, start, end=readin()
  f=Frontier(start,end)
  path, cost=explore(graph,f)
  print_path(path, cost)
