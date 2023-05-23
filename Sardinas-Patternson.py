## TO BE CHECKED
import functools

#Given an input we specify, return if the code is UD or not, if it is unbound or not and what is the bound and check whether the possible codifications are.
def sardinas_patterson(C):
    sets = []
    temp_set = []
    
    #First Iteration: Creation of S1 (saved into current set)
    for i in C:
        for j in range(i, len(C)):
            if i.startswith(C[j]) :
                temp_set.append(i.removeprefix(j))
    current_set = temp_set
    temp_set.clear()

    while check(code= C, sets=sets, current_set=current_set) not in [0, 1]:
        sets.append(current_set)
        current_set.clear()

        for i in C:
            for j in current_set:
                if i.startswith(j):
                    temp_set.append(i.removeprefix(j))
                if j.startswith(i):
                    temp_set.append(j.removeprefix(i))
    
        current_set = temp_set
        temp_set.clear()
    print(check(code= C, sets= sets, current_set=current_set))

def check(code, sets, current_set):
    if sets.isEmpty(): return -1
    if intersection(code, current_set).isEmpty(): return 0
    for i in sets:
        if are_equal(i, current_set) or i.isEmpty(): return 1
    
    return 2

def kmm(d, lengths):
    sum = 0 
    for l in lengths:
        sum += pow(d, -l)
    return sum if (sum <= 1) else -1

def intersection(list1, list2):
    return [value for value in list1 if value in list2]


def are_equal(list1, list2):
    return True if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, test_list1, test_list2), True) else False