'''
import numpy as np 
import matplotlib.pyplot as pyplot


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
        i = int(f)
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



def dist_generation(n):
    Seq = []
    n = int(input("Number of values: "))
    dist = int(input("Enter 0 for normal distribution, 1 for binomial"))
    if dist == 0:
        mu = float(input("Mean: "))
        sigma = float(input("Standard deviation: "))
        Seq = np.random.default_rng().normal(mu, sigma, n)
    elif dist == 1:
        n = float(input("n: "))
        p = float(input("p: "))
        Seq = np.random.default_rng().binomial(n, p, n)

    distribution_plot(Seq)

if __name__ == "__main__":
    dist_generation(100)

'''




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


def levenshtein_decoding(code):#299
    '''   
    c = 0
    n = 1
    to_Ret = ""
    temp_value = "1"
    first_value = True # That means a new word has to be read
    for index, i in enumerate(code):
        if first_value is True:
            #New code
            if i == "1":
                c += 1
            else:
                if c in (0,1):
                    to_Ret += "{} ".format(c)
                    temp_value = ""
                    c = 0
                    pass
                else:
                    first_value = False
                    c -= 1

            #Old code
            
            if i == "0":
                to_Ret = "0 "
            else:
                c+=1
                first_value = not first_value
            
        
        else:
            if n > 1:
                temp_value += i
                n -= 1
            else:
                temp_value += i

                if c == 1:
                    to_Ret += "{} ".format(temp_value)
                    temp_value = ""
                    n = 1
                else:
                    n = int(temp_value, 2)
                
                temp_value = "1"
                c -= 1

            pass
        
        #New code
        else:
            if i == "1": 
                c +=1
            else:
                l = index
                for counting_var in range(c-2):
                    
                    m = binary_to_integer("1" + code[l:l+n+1])
                    print("m = ", m)
                    l += n
                    n = m

                to_Ret += str(n) +" "

                n = 1
                c = 0
                first_value = not first_value
        pass

        
    return to_Ret
    
    '''
    c = 0
    n = 1
    to_ret = ""
    first_value = True
    p = 0
    while p <len(number):
        if number[p] == "0":
            if c == 0:
                to_ret += "0 "
                p += 1
            else:
                p += 1
                for it in range(1, c):
                    n = binary_to_integer("1" + number[p:p +n])
                    p += n
                    pass
                to_ret += "{} ".format(n)
        else:
            c += 1
            p += 1
        pass
    return to_ret
    '''
'''  

def levenshtein_decoder(number_str):
    c = 0
    n = 1
    number = ["1"]

    # decoding == True -> decoding
    # decoding == False -> reading
    decoding = True

    for i in number_str:
        if decoding:
            if i == "1":
                c += 1
            else:
                if c == 0:
                    yield "0"
                elif c == 1:
                    yield "1"
                    c = 0
                else:
                    decoding = False
                    c -= 1
        else: # if not decoding:
            if n > 1:
                number.append(i)
                n -= 1
            else: # elif n > 0:
                number.append(i)

                # If this is the last iteration for the c counter.
                if c == 1:
                    yield "".join(number)
                    decoding = True
                    n = 1
                else:
                    n = int("".join(number), 2)

                number = ["1"]
                c -= 1



def levenshtein_decoding(number_str):
    return " ".join(str(int(i, 2))
                    for i in levenshtein_decoder(number_str))

if __name__ == "__main__":
    f = levenshtein_coding("0 1 12 14 17")
    print(f)
    l = levenshtein_decoding(f)
    print(l)
    pass