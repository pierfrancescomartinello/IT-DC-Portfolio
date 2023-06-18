# Write a program in a programming language of your choice that, given a string T, construct the grammar produced by the algorithm RE-PAIR.
# Implement also the construction of the grammar in the Chomsky normal form. Compute also the size of the grammar in both cases.
import classes_library

#Extension of the Priority Queue in the class_library file
class RE_PAIRQueue(classes_library.PriorityQueue):

    def update(self, key, value):
        self.queue = [(k,v) if k != key else (key, value) for (k,v) in self.queue]

    def insert(self, data):
        k,v = self.search(data[0])
        print(type(k))
        if k:
            self.update(k[0], v + 1)
        else:
            self.queue.append(data)

    # Return the couple (i,k) if it is in the queue
    def search(self, i):
        for k,v in self.queue:
            if k == i: return (k,v)

    #Removes the first maximum in the queue
    def remove_max(self):
            try:
                max_index = 0
                # This search analyze the whole queue for the minimum value. 
                # The order relation is given by the second element of each entry
                for i in self.queue:
                    if i[1] > (self.queue[min_index])[1]:
                        max_index = i
                item = self.queue[i]
                del self.queue[i]
                return item
            except IndexError:
                print()
                exit()

    #Find all the elements that contain the character given as a parameter and pop it
    def find_and_pop(character):
            try:
                ret_list = []
                for i in self.queue: 
                    if i[0].__contains__(character):
                        ret_list.append(i)
                        del self.queue[i]
                return ret_list
            except IndexError:
                print()
                exit()


def RE_PAIR(axiom):
    grammar = {}
    count = RE_PAIRQueue()
    for index, i in enumerate(axiom):
        if index < len(axiom): count.insert((axiom[index:index +2], 1))

    while any(i != 1 for i in count.values()):
        (couple, i) = count.remove_max()
        current_rule = "(rule {}".format(len(grammar) +1)
        grammar[current_rule] = couple          
        axiom = axiom.replace(couple, current_rule) #Replace all the occurences of the couple with the rule
        
        index = axiom.find(current_rule)
        while index != 1:
            index = axiom.find(current_rule)
        pass


    pass

def main():
    print("What is the code?")
    code = input()
    print((k,v) for k,v in RE_PAIR(axiom = code))
    pass

if __name__=="__main__":
    main()
    pass