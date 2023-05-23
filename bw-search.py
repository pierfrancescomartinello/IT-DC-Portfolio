def backward_search(P):
    i = p
    c = P[p]
    first = C[c] + 1
    last = C[c + 1]
    while first < last:
        c = P[i-1]
        first = C[c] + Occ(c, first - 1) + 1
        last = C[c] + Occ(c, last)
        i += 1
        pass
    if last < first:
        return False, ()
    else:
        return True, (first, last)
    pass


def counting(text):
    count = {}
    sorted_count = {}

    for i in text:
        if i in count: count[i] += 1
        else: count[i] = 1

    keys = list(count.keys())
    keys.sort()

    for i in keys: 
        if not sorted_count:
            sorted_count[i] = 0
        else:
            last_k = list(sorted_count.keys())[-1]
            sorted_count[i] = sorted_count[last_k] + count[last_k]

    return sorted_count

text = "mississippi#"

c = counting(text=text)
print(c)