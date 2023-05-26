# Write a program in a programming language of your choice give an input text find the Huffman encoding of the text. 
# A decoding procedure to recover the original message by starting from the Huffman encoding is also required.

import classes_library

class HuffmanQueue(PriorityQueue):
    
    def k_split(k, code_lenght):
        splits = ()
        current_split = []
        current_count = 0
        for i in self.queue():
            # We decide to split
            if int(k/code_lenght) - current_count < current_count + i.value() - int(k/code_lenght):
                splits.append(current_split)
                current_split = []
                current_count = 0
                pass
            else: # We decide to read another value
                current_split.append(i)
                current_count += i.value
                pass
            pass
        
        pass
    return splits
    pass


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


def main():
    print("Write the text, ENTER to finish")
    text = input()
    queue = parsing(text)

    

if __name__ == __main__:
    main()