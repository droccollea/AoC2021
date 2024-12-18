
text = []
gamma_and_epsilon = []

def main():
    f = open("day3\day.txt","r")
    #f = open("day3\sample.txt","r")

    for x in f:
        text.append(str(x))

    #one()
    two()

def one():
    # map/dict of bits
    bits = {}
    # Init to 0
    for i in range(0,len(text[0])-1):
        bits[i] = 0

    # iterate report and add 1s to the map by pos using nested loop
    for i in text:
        count = 0
        for j in range(0,len(i)):
            if i[j] == '1':
                count = bits.get(j) + 1
                bits[j] = count
    print(F"bits:{bits}")

    # get length of report halve it. If pos > half report lenth add pos to the gamma, else epsilon

    gamma = ""
    epsilon = ""
    pivot = len(text) /2
    for k in range(len(bits.keys())):
        if bits.get(k) > pivot:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(F"Gamma: {gamma}; Epsilon: {epsilon}")
    # convert to decimal and multiply 
    print(F"Gamma as dec:{bin2dec(gamma)}; Epsilon:{bin2dec(epsilon)}; Power:{bin2dec(gamma)*bin2dec(epsilon)}")

    gamma_and_epsilon.append(gamma)
    gamma_and_epsilon.append(epsilon)
    
def bin2dec(binary):
    dec = 0
    unit = 1
    reversed = binary[::-1]
    for i in reversed:
        print(F"i: {i}; unit: {unit}: dec:{dec}")
        dec += int(i) * unit
        unit *= 2
    return dec

def reduce_list(pos, list, mode):
    next_list = []
    count = 0
    pivot = len(list)/2

    if pivot < 1:
        #done
        return list

    for l in list:
        if l[pos] == '1':
            count += 1
    find = 0

    if mode == "msb":
        if count >= pivot:
            find = '1'
        else:
            find = '0'
    else:
        if count >= pivot:
            find = '0'
        else:
            find = '1'

    print(F"Count:{count}; pivot:{pivot} Looking for:{find}")
    for i in list:
        if i[pos] == find:
            next_list.append(i)

    return next_list

def two():
    
    # clone text and iterate line length
    
    oxy = 0
    co2 = 0
    # return new list with most significant in that col
    new_text = text.copy()
    for i in range(0, len(text[0])-1):
        new_text = reduce_list(i,new_text,"msb")

    print(new_text)
    oxy = bin2dec(new_text[0].strip())

    # return new list with least significant in that col
    new_text = text.copy()
    for i in range(0, len(text[0])-1):
        new_text = reduce_list(i,new_text,"lsb")

    print(new_text)
    co2 = bin2dec(new_text[0].strip())

    print(F"lifesupp:{oxy*co2}")
    

main()