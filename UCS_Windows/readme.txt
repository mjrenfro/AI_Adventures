1. Marissa Renfro 10651956
2. Python 3.5.2
3.
  find_route.py

    Has general "running" logic
    Calls methods to initialize variables, solve, and print results

  ucs.py

    explore method
      Initializes the frontier to the start city
      Continues to add onto the frontier until the goal city is found
        or there are no unsearched paths in the frontier

    print_path method
      prints the solution path in the specified format

    readin method
      Ensures the correct number of arguments are provided
      Populates the start, goal, and graph variables

    TestUCS class
      Tests the various methods against provided input files and
      other smaller input files

  frontier.py
    Basic priority queue implementation based on heapq
    Also keeps track of the start and goal vertices

4. Since a scripting language was used, compilation is not needed
   In the cmd, enter the following
  _________________________________________________
  | python find_route.py input_file.txt start end |
  _________________________________________________
