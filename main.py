problem = True
n = 5
while problem:
    n_s = input("Give the quantity of bars to sort: ")
    if n_s.isdigit():
        n = int(n_s)
        problem = False
problem = True
fps = 60
while problem:
    fps_s = input("How many operations at most do you want to do per second: ")   
    if fps_s.isdigit():
        fps = int(fps_s)
        problem = False

list_of_sorting=["bubble_sort", "bogo_sort"]
problem = True
s = -2
while problem:
    for i in range(len(list_of_sorting)):
        print(f"[{i+1}] {list_of_sorting[i].replace('_',' ').title()}")
    
    s_s = input("Select: ")
    if s_s.isdigit():
        s = int(s_s) - 1
    if s >= 0 and s < len(list_of_sorting):
        problem = False

import Sorting
Sorting.main(n, list_of_sorting[s], fps)
