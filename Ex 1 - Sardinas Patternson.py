# Write a program in a programming language of your choice that applies the Sardinas-Patterson
# algorithm and returns the type of code received as input.

# Given an input we specify, return if the code is UD or not.
def sardinas_patterson(C):
    # Initialization of the list of set Si
    sets = []

    # Initialization of the sets used during the the iterations of the algorithm
    current_set = set()
    previous_set = set()

    # First Iteration: Creation of S1 (saved into previous_set)
    for i in C:
        for j in C:
            #If j = iW, with W different then the empty word, we add W to the current_set
            if i.startswith(j):
                suffix = i.removeprefix(j)
                if suffix != "": current_set.add(suffix)
    
    # The following 2 lines of code can be optimised by using only current_set. 
    # It was leaved in this way purposely to leave the structure similar to the while loop underneath
    previous_set = current_set.copy()
    current_set.clear()

    # The while loops until we have the confirmation that the code is UD/Not UD
    while (l:=check(code= C, sets=sets, previous_set=previous_set)) in (-1, 2):
        sets.append(previous_set)

        # We loop the sets S0 and the Si-1 (being at the iteration i)
        for i in C:
            for j in previous_set:
                # We check wheter |i| < (or >) |j|. We do not consider the words at all when they are of equal length
                if len(i) > len(j):
                    #If j = iW, with W different then the empty word, we add W to the current_set
                    if i.startswith(j):
                        if (prefix:=i.removeprefix(j)) != "": current_set.add(prefix)
                elif len(i)< len(j):
                    #If i = jW, with W different then the empty word, we add W to the current_set
                    if j.startswith(i):
                        if (prefix:=j.removeprefix(i)) != "": current_set.add(prefix)

    
        previous_set = current_set.copy()
        current_set.clear()
    
    print(l)

# This function checks if the conditions needed to determine wether the code is UD or not are met.
def check(code, sets, previous_set):
    # This condition is met only when we are ready to determine S2
    # if len(sets) == 0: return -1

    # This condition is met only when the intersection between Sn and S0 is not empty (The code is not UD)
    if len(l:=intersection(code, previous_set)) != 0: return ("\tNon empty intersection, the code is not UD. The intersection is: " + str(l))

    # This condition is met only when the last set analysed is empty. In the case that this set is S1, we specify that the code is prefix
    if len(previous_set) == 0: return "\tLast set analysed is empty, the code is UD. \n\t- The code also has a bounded deciphering delay." + "\n\t- The code is prefix." if len(sets) == 0 else ""

    # This condition is met when Sj = Si for some 0<j<i
    for i in sets:
        if i == previous_set: return ("\tTwo sets are equal: " + str(i) + " and "+ str(previous_set) + ".\n\tThe code is UD. \n\t - The code has an unbounded deciphering delay.")
    
    # If none of the previous condition is met, then it is not possible to determine the nature of the code. Hence we return
    return 2


def intersection(list1, list2):
    return [value for value in list1 if value in list2]



if __name__ == "__main__":
    print("SARDINAS-PATTERNSON")
    C = input("Please input the words divided by a space. Press ENTER to finish\n\t").split()
    sardinas_patterson(C) if len(C) != 0 else print("You have not entered a valide code")

    while input("Want to check another code? [Y/n]  ") in ("Y", "y"):
        C = input("\n\tPlease input the words divided by a space\n\t").split()
        sardinas_patterson(C)
    print("Exiting...")
    pass
