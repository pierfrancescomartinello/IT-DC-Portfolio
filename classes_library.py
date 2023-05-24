# This class implements a priority queue
class PriorityQueue():
    # Initialization
    def __init__(self):
        self.queue = []

    # Unused method to print the queue
    def __str___(self):
        return ' '.join(str(i) for i in self.queue)

    # Checking whether the queue is empty
    def isEmpty(self):
        return len(self.queue()) == 0

    # The value inserted (data) is of the form (<letter>, probability)
    def insert(self, data):
        self.queue.append(data)

    # Remove the first minimum found in the queue
    def remove_min(self):
            try:
                min_index = 0
                # This search analyze the whole queue for the minimum value. 
                # The order relation is given by the second element of each entry
                for i in self.queue:
                    if i[1] < (self.queue[min_index])[1]:
                        min_index = i
                item = self.queue[i]
                del self.queue[i]
                return item
            except IndexError:
                print()
                exit()

    # Check how many values are in the queue
    def len(self):
        count = 0
        for i in self.queue:
            count += 1
        return count