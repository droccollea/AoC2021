depths = []

def main():
    f = open("day1\day1.txt","r")
    #f = open("day1\sample.txt","r")

    for x in f:
        depths.append(int(x))

#    one()
    two()

def one():
    increments = 0
    for x in range(len(depths)-1):
        if depths[x] < depths[x+1]:
            increments += 1

    print(F"depths:{len(depths)}")
    print(F"increments: {increments}")
    #1665

def two():
    increments = 0
    for x in range(len(depths)-3):
        if (depths[x] + depths[x+1] + depths [x+2]) < (depths[x+1] + depths[x+2] + depths [x+3]):
            increments += 1
    print(F"increments: {increments}")


main()