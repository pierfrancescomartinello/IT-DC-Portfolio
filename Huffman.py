import classes_library



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
