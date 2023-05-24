# Write a program in a programming language of your choice that, given a string T, construct the grammar produced by the algorithm RE-PAIR.
# Implement also the construction of the grammar in the Chomsky normal form. Compute also the size of the grammar in both cases.
import classes_library

#Extension of the Priority Queue in the class_library file
class RE_PAIRQueue(PriorityQueue):

    #Removes the first maximum in the queue
    def remove_max(self):
            try:
                min_index = 0
                # This search analyze the whole queue for the minimum value. 
                # The order relation is given by the second element of each entry
                for i in self.queue:
                    if i[1] > (self.queue[min_index])[1]:
                        min_index = i
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