
class PriorityQueue():
    def __init__(self):
        self.queue = []

    def __str___(self):
        return ' '.join(str(i) for i in self.queue)

    def isEmpty(self):
        return len(self.queue()) == 0

    def insert(self, data):
        self.queue.append(data)

    def remove_min(self):
            try:
                min_index = 0
                for i in self.queue:
                    if i[1] < (self.queue[min_index])[1]:
                        min_index= i
                item = self.queue[i]
                del self.queue[i]
                return item
            except IndexError:
                print()
                exit()

    def len(self):
        count = 0
        for i in self.queue:
            count += 1
        return count


def parsing(text):
    counting = {}
    for i in text:
        if i not in counting:
            counting[i] = 1
        else:
            counting[i] += 1
    return counting


def encoding(queue, characters):
    encoding = {}
    value = ''
    for i in queue:
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


print("Write the text, ENTER to finish")
text = input()
queue = PriorityQueue()
parsed_text = parsing(text)
code = ''

print(parsed_text)
input()
#Inserting the values of the code into the priority queue
for k, v in parsed_text.items():
    queue.insert((k,v))

#printing snippet
for i in queue.queue:
    print(i)
#end of snippet

while queue.len() != 1:
    (k1,v1) = queue.remove_min()
    (k2,v2) = queue.remove_min()
    queue.insert(k1.append(k2), v1+v2)

(queue, probability_value) = queue.remove_min()

encoding = encoding(queue, parsed_text.keys())

for i in text:
    code.append(encoding[i])

print(code)
