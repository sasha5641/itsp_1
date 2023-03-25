def raise_to_the_degrees(num, max_degree):
    res = []
    for degree in range (1, max_degree+1):
        #yield num ** degree
        res.append(num ** degree)
    return res

#gen = raise_to_the_degrees(25, 945678765434567656789876)

for element in gen:
    print(element)
