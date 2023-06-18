#Given an input we specify, return if the code is UD or not, if it is unbound or not and what is the bound and check whether the possible codifications are.
def sardinas_patterson(C):
    sets = []
    temp_set = set()
    current_set = []

    #First Iteration: Creation of S1 (saved into current set)
    for i in C:
        for j in C:
            if i.startswith(j):
                prefix = i.removeprefix(j)
                if prefix != "": temp_set.add(prefix)
    current_set = temp_set.copy()
    temp_set.clear()

    while (l:=check(code= C, sets=sets, current_set=current_set)) in (-1, 2):
        sets.append(current_set)

        for i in C:
            for j in current_set:
                if len(i) > len(j):
                    if i.startswith(j):
                        if (prefix:=i.removeprefix(j)) != "": temp_set.add(prefix)
                elif len(i)< len(j):
                    if j.startswith(i):
                        if (prefix:=j.removeprefix(i)) != "": temp_set.add(prefix)

    
        current_set = temp_set.copy()
        temp_set.clear()
    print(l)

def check(code, sets, current_set):
    if len(sets) == 0: return -1
    if len(l:=intersection(code, current_set)) != 0: return ("Non empty intersection, the code is not UD. The intersection is: " + str(l))
    if len(current_set) == 0: return "Current set is empty, the code is UD"
    for i in sets:
        if i == current_set: return ("Two sets are equal: " + str(i) + " and "+ str(current_set) + ".\nThe code is UD")
    
    return 2


def intersection(list1, list2):
    return [value for value in list1 if value in list2]


if __name__ == "__main__":
    main()
    #Caso non UD
    C = ("010","0001","0110","1100","00011","00110","11110","101011")
    sardinas_patterson(C)

    print("\n\n\n\n")
    C = ("abc", "abcd","e","dba","bace","ceac","ceab","eabd")
    sardinas_patterson(C)

