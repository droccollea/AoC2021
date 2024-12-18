
text = []

def main():
    #f = open("day2\day.txt","r")
    f = open("day2\sample.txt","r")

    for x in f:
        text.append(str(x))

#    one()
    two()

def one():
    x_pos = 0
    y_pos = 0
    for i in text:
        op, operand = i.split(" ")
        if op == "forward":
            x_pos += int(operand)
        if op == "up":
            y_pos -= int(operand)
        if op == "down":
            y_pos += int(operand)
    
    print(F"At x:{x_pos}, y:{y_pos}")
    print(F"Product: {x_pos*y_pos}")
        

def two():
    x_pos = 0
    aim = 0
    depth = 0
    for i in text:
        op, operand = i.split(" ")
        if op == "forward":
            x_pos += int(operand)
            depth += aim * int(operand)
        if op == "up":
            aim -= int(operand)
        if op == "down":
            aim += int(operand)
    
    print(F"At x:{x_pos}, y:{aim}, depth:{depth}")
    print(F"Product: {x_pos*depth}")


main()