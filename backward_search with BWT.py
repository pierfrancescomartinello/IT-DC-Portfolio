# pseudo code
# C[] the vector that counts how many elements are smaller that the element in position i( for the first one is always 1 due to the $ symbol)
#i = P, c = P[p], First = C[c] + 1, last=  C[c+1]
# While( first<= last)and i >=2:
#   c = P[i-1]
#   First =  C[c] + occ[c, first - 1 ] + 1
#   Last = C[c] + Occ[c, last];
#   i--