import math
from matplotlib import pyplot as plt

#Function to calculate the delta code
def delta(i):
    value = ''
    N = math.floor(math.log2(i))

    for j in range(1, N):
        value += '0'

    value += gamma(N + 1)

    bi = bin(i)[2:]

    value += bi
    return value

#Function to calculate the gamma code
def gamma(i):
    value = ''
    N = math.floor(math.log2(i))

    for j in range(1, N):
        value +='0'
    bi = bin(i)[2:]

    value += bi
    return value


def main():
    deltas = []
    gammas = []
    deltas_l = []
    gammas_l = []
    binarye = []
    for i in range(1,1000):
        gamma_i = gamma(i)
        gammas.append(gamma_i)
        gammas_l.append(len(gamma_i))

        delta_i = delta(i)
        deltas.append(delta_i)
        deltas_l.append(len(delta_i))

        binarye_i = math.floor(math.log2(i)) + 1
        binarye.append(binarye_i)

    #A = gamma/binary
    a =[]
    b =[]
    running_avg_delta=[]
    running_avg_gamma=[]
    value_d = 0
    value_g = 0
    for i in range(len(gammas)):
        a.append(int(gammas[i])/binarye[i])
        b.append(int(deltas[i])/binarye[i])
        value_g += int(gammas[i])
        value_d += int(deltas[i])
        running_avg_delta.append(value_d/(i + 1))
        running_avg_gamma.append(value_g/(i + 1))
        
    #B = delta/binary

    

    #plt.plot(a, label='Gamma/Binary')
    #plt.plot(b, label='Delta/Binary')

    #plt.plot(running_avg_delta, label="Delta running mean")
    #plt.plot(running_avg_gamma, label='Gamma running mean')
    gammaint = []
    deltaint = []
    for i in range(len(gammas)):
        gammaint.append(int(gammas[i]))
        deltaint.append(int(deltas[i]))
    plt.plot(gammas_l[0:50], label="Gamma")
    plt.plot(deltas_l[0:50], label="Delta")
    plt.legend()
    plt.show()
    pass


if __name__== '__main__':
    main()