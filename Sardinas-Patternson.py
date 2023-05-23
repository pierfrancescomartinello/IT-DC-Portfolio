#Given an input we specify, return if the code is UD or not, if it is unbound or not and what is the bound and check whether the possible codifications are.
def sardinas_patterson(s0):
    sets = []
    set = []
    
    for i in range(1, len(s0)):
        for j in range(i, len(s0)):
            if i.startswith(j) :
                set.append(i.removeprefix(j))
    sets.append(set)
    current_set = set
    set.clear()

    for i in s0:
        for j in current_set:
            if i.startswith(j) :
                set.append(i.removeprefix(j))
            if j.startswith(i) :
                set.append(j.removeprefix(i))
   
    current_set = set
    set.clear() 
    check, value = check(sets, current_set)
    sets.append(set)
    pass

def check(sets, current_set):
    
    pass

def kmm(d, lengths):
    sum = 0 
    for l in lengths:
        sum += pow(d, -l)
    return sum if (sum <= 1) else -1