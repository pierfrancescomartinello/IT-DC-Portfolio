# Write a program in a programming language of your choice give an input text find the Huffman encoding of the text. 
# A decoding procedure to recover the original message by starting from the Huffman encoding is also required.
from collections import Counter
import classes_library

#Procedure necessary to compute the probability of each symbol in the code
def probability_reading_with_queue(text):
    queue = classes_library.PriorityQueue()
    parsed_text = Counter(text)

    #Put the values of parsed text into queue
    for k, v in parsed_text.items():
        queue.insert((k,v))

    return queue

# THIS PROCEDURE DOES NOT WORK
# Procedure necessary to compute the Huffman code
def huffman(queue):

    dictionary = {}

    # Until the queue has only one element
    while queue.len() != 1:
        # Remove the first minimum
        (k1,v1) = queue.remove_min()
        # If the key is not a list, we simply initialize its entry on the dictionary
        if type(k1) != list:
            dictionary[k1] = "0"
        else:# else we add the prefix "0" to each value of the list
            dictionary ={k:("0{}".format(v) if k in k1 else v ) for (k,v) in dictionary.items()}

        #Remove the second minimum
        (k2,v2) = queue.remove_min()

        # If the key is not a list, we simply initialize its entry on the dictionary
        if type(k2) != list:
            dictionary[k2] = "1"
        else:# else we add the prefix "0" to each value of the list
            dictionary ={k:("1{}".format(v) if k in k2 else v ) for (k,v) in dictionary.items()}

        # Insert the combined value back together in the priority queue
        if type(k1) != list and type(k2) != list:
            queue.insert(([k1,k2], v1+v2))
        elif type(k1) == list:
            queue.insert(([k1.append(k2)], v1+v2))
        else:
            queue.insert(([k2.append(k1)], v1+v2))
        
    
    return dictionary

# Given an input of the type "((a,b),((c,d),(e,f)))" we return the value relative the elements (a,b,c,d,e,f)
def tree_linearization(code):
    # Initialize the dicitonary and the initial empty value
    encoding = {}
    value = ''
    # Reading the code
    for i in code:
        # If we read "(" we append a 0 into the string value
        if i == '(':
            value += ('0')
        # If we read "," we delete the last "bit" and insert a 1
        elif i == ',':
            value = value[:-1]
            value += ('1')
        # If we read ")" we delete the last "bit"
        elif i == ')':
            value = value[:-1]
        else: # If we read a symbol, insert it in the dictionary
            encoding[i] = value
        pass
    return encoding

# My implementation of the Huffman encoding,
# using a string to represent all the Huffman tree
def my_huffman(queue):
    # Until the queue has only one value
    while queue.len() != 1:
        #We pop the two smallest value
        (k1,v1) = queue.remove_min()

        (k2,v2) = queue.remove_min()
        
        # Insert the value [(k1,k2), v1+v2] into the queue
        queue.insert(["({},{})".format(k1,k2), v1+v2])
    
    # Return the key
    (k, v) = queue.remove_min()
    return k
    
# A simple method to encode the text using the encoding dictionary
def encoding(text, encoding):
    coding = ""
    for elem in text:
        coding += encoding[elem]
    return coding


# A simple method to decode the encoded text using the encoding dictionary
def decoding(coded_text, encoding):
    # We transpose the dictionary
    encoding_transpost = {v:k for k,v in encoding.items()}
    # The temporary value where we store the bits being red
    temp_value = ""
    # The value where the decodification is stored
    decoding = ""
    # We read the coded text
    for i in coded_text:
        temp_value += i
        # If the value is in the dictionary, we add its decodification to the output
        if temp_value in encoding_transpost.keys():
            decoding += encoding_transpost[temp_value]
            temp_value = ""

    return decoding





if __name__ == "__main__":
    print("Huffman")
    C = input("Please input the words divided by a space. Press ENTER to finish\n\t")
    if len(C) != 0:
        huffman_dictionary = my_huffman(probability_reading_with_queue(C))
        l = tree_linearization(huffman_dictionary)
        print("\tThe encoding of \"{}\" is: {}".format(C, f:= encoding(C, l)))
        if len(input("\tDo you want to decode it? Press a key to do it, ENTER if not: ")) != 0: print("\tThe decoding of \"{}\" is {}".format(f, decoding(f, l)))
    else:
        print("You have not entered a valide code")
    

    while input("Want to check another code? [Y/n]  ") in ("Y", "y"):
        C = input("Please input the words divided by a space. Press ENTER to finish\n\t")
        if len(C) != 0:
            huffman_dictionary = my_huffman(probability_reading_with_queue(C))
            l = tree_linearization(huffman_dictionary)
            print("\tThe encoding of \"{}\" is: {}".format(C, f:= encoding(C, l)))
            if len(input("\tDo you want to decode it? Press a key to do it, ENTER if not: ")) != 0: print("\tThe decoding of \"{}\" is {}".format(f, decoding(f, l)))
        else:
            print("You have not entered a valide code")
    print("Exiting...")
    exit()