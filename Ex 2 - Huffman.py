# Write a program in a programming language of your choice give an input text find the Huffman encoding of the text. 
# A decoding procedure to recover the original message by starting from the Huffman encoding is also required.

import classes_library


def parsing(text):
    queue = PriorityQueue()
    counting = {}
    for i in text:
        if i not in counting:
            counting[i] = 1
        else:
            counting[i] += 1

    for k, v in parsed_text.items():
        queue.insert((k,v))
    return queue

def huffman(queue):
    dictionary = {}

    while queue.len() != 1:
        (k1,v1) = queue.remove_min()
        if type(k1) != list:
            dictionary[k1] = "0"
        else:
            for i in k1:
                dictionary[i] = "0" + dictionary[i]
            pass

        (k2,v2) = queue.remove_min()
        if type(k2) != list:
            dictionary[k2] = "1"
        else:
            for i in k2:
                dictionary[i] = "1" + dictionary[i]
            pass


        if type(k1) != list and type(k2) != list:
            queue.append(([k1,k2], v1+v2))
        elif type(k1) == list:
            queue.append((k1.append(k2), v1+v2))
        else:
            queue.append((k2.append(k2), v1+v2))
        
    
    return dictionary

def tree_linearization(code, characters):
    encoding = {}
    value = ''
    for i in code:
        if i == '(':
            value.append('0')
        elif i == ';':
            value = value[:-1]
            value.append('1')
        elif i == ')':
            value = value[:-1]
        else:
            encoding[i] = value
        pass
    return encoding

# My implementation of the Huffman encoding,
# using a string to represent all the 
def my_huffman(queue):
    while queue.len() != 1:
        (k1,v1) = queue.remove_min()

        (k2,v2) = queue.remove_min()
        
        queue.add("({}, {})".format(k1,k2))
    (k, v) = queue.remove_min()
    return k
    
def encoding(text, encoding):
    coding = ""
    for elem in text:
        coding += encoding[elem]
    return coding


def decoding(coded_text, encoding):
    encoding_transpost = {v: k for k,v in encoding.items()}
    temp_value = ""
    decoding = ""
    for i in coded_text:
        temp_value += i
        if temp_value in encoding_transpost.keys():
            decoding += encoding_transpost[temp_value]
            temp_value = ""

    return decoding

    
def main():
    print("Write the text, ENTER to finish")
    text = input()
    queue = parsing(text)

    

if __name__ == __main__:
    main()