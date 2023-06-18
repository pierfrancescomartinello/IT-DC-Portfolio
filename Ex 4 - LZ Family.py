# Write a program in a programming language of your choice, that given a text T outputs the LZ77 encoding and the LZss encoding of the text.
# A paramter of the program should be W, the length of the search buffer.
import math


# Returns the LZ77 Encoding for a word
# The parameter width is the dimension of the search buffer
def lz77_encoding(width, word):
    code = []
    p = 0
    while p < len(word):# Until the whole word is read
        # Search for the beginning and the length of the longest common subsequence
        # (In case that p-width <= 0 or the width = 0 the serach buffer starts from the beginning of the word)
        beginning, length = lcs(word[0 if width == 0 or p-width <= 0 else p-width :p] , word[p:]) 
        if p + length != len(word): code.append((beginning, length, word[p+length])) # Usual case
        else: code.append((beginning, length, ""))# When we have reached the end of the word
        p += length +1
    return code

# Returns the LZ77 Decoding for a code
def lz77_decoding(code):
    word = ""
    p = 0
    for i in code: # For each triplets (i[0],i[1],i[2])
        if i[0] >= i[1]: # In case the length is smaller or equal to the offset
            word += word[p-i[0]:p-i[0]+i[1]] + i[2] # We append the right substring and the value of i[2]
        else: # Otherwise we get sure to add the remaning word with multiplicity dictated by (length -offset)/offset 
            word += word[p -i[0]:p] + (word[p -i[0]:p +i[1] -i[0]-i[0]] * int(i[1] -i[0]/i[0]))+ i[2]
        p += i[1] +1
        pass
    return word


#---------------
# Returns the LZss Encoding for a word
# The parameter width is the dimension of the search buffer
def lzss_encoding(width, word): #410
    code = []
    p = 0
    while p < len(word): # Until the whole word is read
        # Search for the beginning and the length of the longest common subsequence
        # (In case that p-width <= 0 or the width = 0 the serach buffer starts from the beginning of the word)
        beginning, length = lcs(word[0 if width == 0 or p-width <= 0 else p-width :p] , word[p:])
        if beginning == 0 and length == 0: # In case we find a new character... 
            code.append((0, word[p+length])) # ... we add (0, <character>)
            p += length + 1
        else: # In case we find a correspondence... 
            code.append((beginning, length))# ... we add (beginning, length)
            p += length
    return code


# Returns the LZss Decoding for a code
def lzss_decoding(code): #410
    word = ""
    p = 0
    for i in code: # For any pair in the codebook
        if isinstance(i[1], str): # If the second value is a character...
            word += i[1] #... we append it to the word
            p += 1
        else: #If the second value is a number, we add the proper substring
            word += word[p -i[0]:p +i[1]-i[0]] + (word[p -i[0]:p +i[1]-i[0]-i[0]]* int(i[1]-i[0]/i[0]) if i[0]<i[1] else "")
            p += i[1]
        pass
    return word


#---------------------
# Return the Longest Common Substring
def lcs(search_buffer, look_ahead_buffer):
    (index, length) = (0,0)
    for i in range(f:=len(search_buffer)): # For each suffix of search buffer we get the longest prefix with the smallest index possible
        l = longest_prefix(search_buffer[i:], look_ahead_buffer)
        if l > length:
            (index, length) = (f - i, l)
        elif index > f- i and length == l:
            (index, length )= (f -i, l)

    # In the case (f,f,x) with f != 0
    if index == length and index != 0: 
        # We check if there is the possibility that the lenght extends further
        # I.E.: search_buffer = WB and look_ahead_buffer = BL
        extended_length = 1
        prev_length = length
        temp_length = longest_prefix(search_buffer[f-index:] + look_ahead_buffer[:extended_length], look_ahead_buffer)

        while prev_length != temp_length:
            prev_length = length + extended_length
            extended_length += 1
            temp_length = longest_prefix(search_buffer[f-index:] + look_ahead_buffer[:extended_length], look_ahead_buffer)
        length = temp_length
    

    return index, length

# Get the longest prefix of 2 strings
def longest_prefix(str1, str2):
    length = 0
    for i in range(min(len(str1), len(str2))):# Iteratively search if the prefix extends at step i
        if str1[i] == str2[i]:
            length += 1
        else:
            return length
    return length

# Get the array L of the Borrows-Wheeler Transform without cyclic rotations
def BWT(T):
    T += "$" # Our EOF symbol
    l = [T[i:i+1] for i in range(len(T))]
    l.sort()
    return l

# Get the Equal letter Runs for a code that is the number of substrings 
# that are made only by more that one repetition of a character
def ELR(T):
    a = ""
    b = T[0]
    elr = 0
    for i in range(1,len(T)):
        if b == T[i] and a != b: elr += 1 # We get here when the last three characters met are "zll" with z !=l
        a = b
        b = T[i]
    return elr              


# Return a list of i indexes for i the rows of the text
# such that checklist[i] is True iff r = O(zlog^2 n) and z = O(rlogn)
def experiment(text, width):
    checkList = []
    count = 0
    with open(text, "r") as text:
        for line in text.readlines(): # We read the text line by line
            count += 1
            n = len(line)
            r = len(lz77_encoding(width, line))
            z = ELR(BWT(line))
            checkList.append(r <= z*math.pow(math.log2(n), 2) and z <= r*math.log2(n))

            pass
        pass
    return checkList.count(True), checkList.count(False)

    

if __name__ == "__main__":
    check = input("Enter O for LZ, 1 if experiment: ")
    while check not in("1", "0"):
        check = input("Wrong input. Enter O for LZ, 1 if experiment: ")
    if check == "1":
        width = int(input("Enter an integer: "))
        t,f = experiment("alice.txt", width=width)
        print("Number of lines for which the statement holds: ", t, "\nNumber of lines for which the statement does not hold: ", f)
    else:
        alg = input("O for LZ77, 1 for LZss, press ENTER for exiting: ")
        while(alg != ""):
            if alg == "0":
                code = lz77_encoding(width=int(input("Insert a width: ")), word=input("Enter the word: "))
                dec = input(code, "\n Enter Y if want to decode it: ")
                if dec in ("Y", "y"):
                    word = lz77_decoding(code=code)
            elif alg == "1":
                code = lzss_encoding(width=int(input("Insert a width: ")), word=input("Enter the word: "))
                dec = input(code, "\n Enter Y if want to decode it: ")
                if dec in ("Y", "y"):
                    word = lzss_decoding(code=code)
            else:
                alg = input("Wrong input. O for LZ77, 1 for LZss, press ENTER for exiting: ")
            print("\n\n\n")


    pass
    

