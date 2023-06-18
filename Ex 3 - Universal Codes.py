# Write a program in a programming language of your choice 
# that computes all the universal codes of integers we have studied (both encoding and decoding).
import math
import matplotlib.pyplot as pyplot
import numpy as np

# Returns the base 10 representation of an integer
def binary_to_integer(binary_integer):
    value = 0
    for i in binary_integer:
        value += value
        if i == "1":
            value +=1
    return value

# Returns the unary encoding of the number
def unary_encoding(number):
    return "0" * (number-1) + "1"

# Returns the number whose unary encoding is given as a parameter
def unary_decoding(code):
    return code.count("0")

#--------

# Returns the gamma encoding for a single number
def gamma_coding_sn(number):
    binary = bin(int(number))[2:]# We trucate the "0x" in the output of the bin() function
    return "0" * (len(binary) - 1) + binary

#Returns the gamma encoding for a series of number
def gamma_coding(numbers):
    to_ret = ""
    temp_number = "" #Temporary number
    for number in numbers:
        if number == " ":
            code += gamma_coding_sn(temp_number)# If we read a number we call the gamma_coding_sn() procedure
            temp_number = ""
        else:
            temp_number += number
    return to_ret

# Returns the gamma decoding
def gamma_decoding(code): # 283
    l = 0
    num = ""
    decode = ""
    read = False # will be True when a value has been completely read
    for index, char in enumerate(code):
        if read is True: # If the value has been decoded, we enter this dummy loop l times
            l -= 1
            if l == 0:
                read = False # Here we are ready to read another value
            continue
        if char == "0": # if the character read is "0" we increment ò
            l += 1
        elif char == "1":# otherwise

            for i in range(l+1):# We read the l +1 values
                num += code[index + i]
            read = True #The number is read
            decode += str(binary_to_integer(num)) + " " # We add the value to return 
            num = ""
    return decode

#----
# Returns the delta coding of a series of numbers
def delta_coding(numbers):
    code = ""
    temp_number = ""
    for index, number in enumerate(numbers):
        if number == " ": # Here we have read a whole number
            code += gamma_coding_sn(len(bin(int(temp_number))[2:])) + bin(int(temp_number))[3:] #Get the encoding
            temp_number = ""
        elif index == len(numbers) -1:# We read the last character
            temp_number += number
            code += gamma_coding_sn(len(bin(int(temp_number))[2:])) + bin(int(temp_number))[3:]
            temp_number = ""
        else:
            temp_number += number
    return code


# Returns the delta decoding of a code
def delta_decoding(code):
    l = 0
    num = ""
    decode = ""
    read = False # Will be true when a number will be scanned
    for index, char in enumerate(code):

        # Scan of values already considered
        if read is True:
            l -= 1
            if l == 0:
                read = False
            continue
        # Scan of the first zeros
        if char == "0":
            l += 1
        elif char == "1": # If we get a 1...
            n = binary_to_integer(code[index: index + l + 1]) - 1 # ... we scan N
            num = code[index +l +1: index +l +n +1] # ... we get the number
            read = True
            print("1" + num)
            decode += str(binary_to_integer( "1" + num)) + " " # Add it to the decoding
            num = ""
            bin_num = ""
            l += n
    return decode

#----

# Return the Fibonacci Encoding of a series of numbers
def fibonacci_encoding(numbers):
    number = ""
    code = ""
    for index, i in enumerate(numbers):
        if i == " ":# If we reach a space we get the code of the number we just finished reading
            code += fibonacci_encoding_sn(int(number))
            number = ""
        elif index == len(numbers) -1:
            number += i
            code += fibonacci_encoding_sn(int(number))
            number = ""
        else:
            number += i
        
    return code

# Returns the Fibonacci Encoding of a series of numbers
def fibonacci_encoding_sn(number):
    code = 0
    code_length = 0
    indexes = []
    while number != 0: # Until the sum is complete
        it_index = ReverseBinetFormula(int(number)) # Get index of the largest Fibonacci Number smaller than number
        #At the first iteration code_lenght is set to the longest
        if code_length == 0: code_lenght = it_index - 1
        number -= BinetFormula(it_index) # subtract the "it_index"-th Fibonacci number from number
        code += int(math.pow(2,(it_index -2) if it_index >1 else 0)) 
    return (bin(code)[2:][::-1]) + "1"

# Get the Fibonacci decoding of a code
def fibonacci_decoding(code):
    sum = 0
    to_ret = ""
    temp_index = 0 
    read = False # Will be True when a number is read
    for index, i in enumerate(code):
        if read == True: # If we have finished reading a number...
                sum = 0
                temp_index = index 
                if i == "1":# ... if the last number read is "1" we add the i+2 th Fibonacci Number to the sum
                    sum += BinetFormula(index - temp_index + 2)
                read = not read #Set to False
        elif index == 0 and i == "1": # if we read the first character
            sum += BinetFormula(index - temp_index + 2)
            continue

        elif index != 0 and read == False:
            #If there are two consecutive "1"
            if i == "1" and code[index - 1] == "1":
                to_ret += str(sum) + " "
                read = not read #Set to True
            else:
                if i == "1":
                    sum += BinetFormula(index - temp_index + 2)

    return to_ret

# Returns the Levenshtein Coding for a series of numbers
def levenshtein_coding(numbers):#297
    number = ""
    code = ""
    for index, i in enumerate(numbers):
        if i == " ":# When we encounter a space ...
            code += levenshtein_coding_sn(int(number)) # ...we code the number
            number = ""
        elif index == len(numbers) -1:
            number += i
            code += levenshtein_coding_sn(int(number))# The codification of the last number
            number = ""
        else:
            number += i
        
    return code

# Returns the Levenshtein Coding of a single number
def levenshtein_coding_sn(number):
    if number == 0:
        return "0"
    else:
        code = ""
        c = 1
        m = number
        while m != 0:
            bin_rep = bin(int(m))[3:] #Get the binary representation of M without the leading "1"
            code = bin_rep + code
            if bin_rep != "": # If the binary representation is not empty
                c += 1
                m = len(bin_rep)# Set m to the lenght of the binary representation
            else:
                code = "1" * c + "0" + code
                m = 0
    return code

# Returns the Levenshtein Decoding for a code
def levenshtein_decoding(code):#299
    
    c = 0
    n = 1 # Number of bits to read 
    to_ret = ""
    p = 0 # Temporary index
    while p <len(number):
        if number[p] == "0": # If we have read only a 0... 
            if c == 0:
                to_ret += "0 " # ...we output a 0
                p += 1
            else:
                p += 1
                for it in range(1, c): # Read N bits c-1 times
                    n = binary_to_integer("1" + number[p:p +n]) #Update N
                    p += n #update the index
                    pass
                to_ret += "{} ".format(n)
        else:
            c += 1
            p += 1
        pass
    return to_ret


# Returns the Rice Code
def rice_coding(k, number):
    q = int((number-1) // math.pow(2,k))# Get the quotient
    r = int((number-1) % math.pow(2,k))# Get the remainder
    br = bin(r)[2:]
    return unary_encoding(int(q + 1)) + "0" *(k-len(br)) + br

# Returns the Rice Decoding
def rice_decoding(k, code):
    to_ret = ""
    temp_number = ""
    c = 0
    already_read = False # Will be True if we have read the number
    for index, char in enumerate(code):
        if already_read: # We enter this dummy loop c times for any number
            c-=1
            if c == 0 : 
                already_read = not already_read
                temp_number = ""
                
        else:        
            temp_number += char
            if char == "1":
                num = code[index+1:index+k+1] # Get the number
                number = int(unary_decoding(temp_number) * math.pow(2, k) + binary_to_integer(num) + 1)# Decode it
                to_ret += str(number) + " "
                temp_number == ""
                already_read = not already_read
                c = k
            pass
    return to_ret

#Find the index of the largest Fibonacci number smaller than num
def ReverseBinetFormula(num):
    return math.floor((math.log(num * math.sqrt(5)))/(math.log(1 + math.sqrt(5) ) - math.log(2))) if num != 0 else 0

#Find the i-th Fibonacci number using the Binet formula
def BinetFormula(index):
    return int(f'{(math.pow((1 + math.sqrt(5))/2, index) - math.pow( (1 - math.sqrt(5))/2, index)) /(math.sqrt(5)):.0f}')

#------------------------------
#PLOTTING FUNCTIONS
#------------------------------

# Plot the lenght of Binary, Gamma, Delta, Fibonacci, Rice (with k = 5 and 7) for n numbers
def n_plot(n):
    
    binary= []
    gamma= []
    delta = []
    fib= []
    rice5 = []
    rice7 = []

    for i in range(1, n):
        binary.append( len(bin(i)[2:]))
        gamma.append( len(gamma_coding_sn(i)))
        delta.append( len((delta_coding(str(i)))))
        fib.append( len(fibonacci_encoding_sn(i)))
        rice5.append( len(rice_coding(5, i)))
        rice7.append( len(rice_coding(7, i)))
        
    fig, ax = pyplot.subplots()

    ax.plot(binary, color= "green", label = "Binary")
    ax.plot(gamma, color="red", label = "Gamma")
    ax.plot(delta, color="blue", label = "Delta")
    ax.plot(fib, color="yellow", label = "Fibonacci")
    ax.plot(rice5, color="pink", label = "Rice (k = 5)")
    ax.plot(rice7, color="black", label = "Rice (k = 7)")
    ax.legend(loc = "upper left")
    pyplot.show()
    pass

# Plot the lenght of Binary, Gamma, Delta, Fibonacci, Rice (with k = 5 and 7) 
# for 1 and n numbers of the form x0x1 for x between 1 and n 
def x0x1_plot(n):
    binary= []
    gamma= []
    delta = []
    fib= []
    rice5 = []
    rice7 = []

    for i in range(n-1):
        l = int(str(i) + "0" + str(i) + "1") if i != 0 else 0
        binary.append( len(bin(l)[2:]))
        gamma.append( len(gamma_coding_sn(l)))
        delta.append( len((delta_coding(str(l)))))
        fib.append( len(fibonacci_encoding_sn(l)))
        rice5.append( len(rice_coding(5, l)))
        rice7.append( len(rice_coding(7, l)))
        
    fig, ax = pyplot.subplots()

    ax.plot(binary, color= "green", label = "Binary")
    ax.plot(gamma, color="red", label = "Gamma")
    ax.plot(delta, color="blue", label = "Delta")
    ax.plot(fib, color="yellow", label = "Fibonacci")
    ax.plot(rice5, color="pink", label = "Rice (k = 5)")
    ax.plot(rice7, color="black", label = "Rice (k = 7)")
    ax.legend(loc = "upper left")
    pyplot.show()
    pass
    pass

# Plot the lenght of Binary, Gamma, Delta, Fibonacci, Rice (with k = 5 and 7) for n numbers
def distribution_plot(dis_func):
    
    binary= []
    gamma= []
    delta = []
    fib= []
    rice5 = []
    rice7 = []

    for f in dis_func:
        i = int(-f if f< 0 else f)
        binary.append( len(bin(i)[2:]))
        gamma.append( len(gamma_coding_sn(i)))
        delta.append( len((delta_coding(str(i)))))
        fib.append( len(fibonacci_encoding_sn(i)))
        rice5.append( len(rice_coding(5, i)))
        rice7.append( len(rice_coding(7, i)))
        
    fig, ax = pyplot.subplots()

    ax.plot(binary, color= "green", label = "Binary")
    ax.plot(gamma, color="red", label = "Gamma")
    ax.plot(delta, color="blue", label = "Delta")
    ax.plot(fib, color="yellow", label = "Fibonacci")
    ax.plot(rice5, color="pink", label = "Rice (k = 5)")
    ax.plot(rice7, color="black", label = "Rice (k = 7)")
    ax.legend(loc = "upper left")
    pyplot.show()
    pass


# Generates n values using a probability distribution 
def dist_generation():
    Seq = []
    n = int(input("Number of values: "))
    dist = int(input("Enter 0 for normal distribution, 1 for binomial"))
    if dist == 0:
        mu = float(input("Mean: "))
        sigma = float(input("Standard deviation: "))
        Seq = np.random.default_rng().normal(mu, sigma, n)
    elif dist == 1:
        n = int(input("n: "))
        p = float(input("p: "))
        while p<0 or p>1 or p is None:
            p = float(input("p: "))
        Seq = np.random.default_rng().binomial(n, p, n)

    distribution_plot(Seq)
    pass

if __name__ == "__main__":
    dist_generation(100)
    
'''
if __name__ == "__main__":
    dis = dist_generation(380)
    distribution_plot(dis)
    pass




if __name__ == "__main__":
    n = "14 16 17 18 74 "
    l = levenshtein_coding(n)
    print("{} = {}".format(n,l))
    j = levenshtein_decoding(l)
    print(j)
'''