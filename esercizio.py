import math

#Done
def coherence(probability_set):
    return True if (probability_set.sum() == 1) else False

#Done
def entropy(base, probability_set):
    sum = 0
    for i in probability_set:
        sum = sum + i*math.log(i, base)
    return sum

#Not Done
def prefix(lengths, d):
    sum = kraft_mc(lengths, d)
    if sum != 1:
        return NULL
    grouping = {}
    for element in lengths:
        grouping[element] += 1
    
    #For the level n the number of "available leaves" for a d-ary tree is the products for i = 0 to n-1 of (d - grouping[i])d
    power = 1
    for k,v in grouping:
        if v < d*power:
            pass
        elif v >d*power:
            #It is not possible to construct the prefix code
            pass
        else:
            #If this condition is reached and we reached the maximum lenght of the code, we got the code, else the code is unobtainable
            if k == lengths.maximum():
                pass
            else:
                pass
            pass
        pass
        power *= v
    
    pass

#Done
def acd(base, code):
    sum = 0
    for i in code:
        sum = sum + i[1]*math.log(i[2], base)
    return sum

#Not done
def shannon(alph):
    pass

#Done
def binary_shannon_fano(probability_dict):
    bs_dict = {}
    sorted_probability_dict = sorted(probability_dict.items() , key = lambda x:x[1], reverse=True)

    for k, v in sorted_probability_dict:
        bs_dict[k] = ''
    return binary_shannon_fano_subroutine(sorted_probability_dict, bs_dict)

#Done
def binary_shannon_fano_subroutine(partition, bs_dict):
    if len(partition) == 1:
        return bs_dict
    partiton_sum = 0
    split = 0
    #Count of the total probability analyzed
    probability = partition.values().sum()
    #Deciding on where to split
    for k, v in partition:
        if partiton_sum >= probability/2 : break
        if partiton_sum + v - probability/2 > partition_sum - probability/2:
            break
        else:
            partiton_sum += v
            split += 1
       
    d1 = dict(list(partition.items())[:split])
    d2 = dict(list(partition.items())[split:])
    for k, v in d1:
        bs_dict[k] = bs_dict[k].append('0')
    bs_dict = binary_shannon_fano_subroutine(d1, bs_dict)
    for k,v in d2:
        bs_dict[k] = bs_dict[k].append('1')
    bs_dict = binary_shannon_fano_subroutine(d2, bs_dict)
 
#Done
def kraft_mc(lenghts, d):
    sum = 0
    for length in lengths:
        sum = sum + math.pow(d, -lenght)
    return sum