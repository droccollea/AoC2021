
import copy
text = []
coords = []
map = {}

def main():
    f = open("day5\day.txt","r")
    #f = open("day5\sample.txt","r")

    for x in f:
        text.append(str(x.strip()))

    for t in text:
        coords.append(t.split(" -> "))

    #one()
    two()


def one():
    # iterate coords
    for xyxy in coords:
        (x1y1, x2y2) = tuple(xyxy)
        print(F"xyxy:{xyxy}")
        (x1,y1) = x1y1.split(",")
        (x2,y2) = x2y2.split(",")

        # if not h/v continue
        if (x1 != x2) and (y1 != y2):
            print(F"xyxy is diagonal: {xyxy}")
            continue

        # increment map for the coords for each point.
        # Handle x coords (horizontal)
        if (y1 == y2):
            xstep = 1
            if int(x1) > int(x2):
                xstep = -1
            else: 
                xstep = 1

            for x in range (int(x1),int(x2)+xstep,xstep):
                #print(F"x coords from x1 to x2:{x}")
                point = F"{x},{y1}"
                if point in map:
                    hit = map.get(point)
                    hit += 1
                    map.update({point: hit})
                else:
                    map[point] = 1

        # Handle y (vert)
        if (x1 == x2):
            if int(y1) > int(y2):
                ystep = -1
            else: 
                ystep = 1

            for y in range (int(y1),int(y2)+ystep,ystep):
                #print(F"y coords from y1 to y2:{y}")
                point = F"{x1},{y}"
                if point in map:
                    hit = map.get(point)
                    hit += 1
                    map.update({point: hit})
                else:
                    map[point] = 1

    #print(F"{map}")

    overlaps = 0
    for x in map.values():
        if x > 1:
            overlaps += 1
    
    print(f"2+ overlaps:{overlaps}")

def points(x1y1, x2y2):
    diff_x = 0


def two():
    # iterate coords
    for xyxy in coords:
        (x1y1, x2y2) = tuple(xyxy)
        print(F"xyxy:{xyxy}")
        (x1,y1) = x1y1.split(",")
        (x2,y2) = x2y2.split(",")

        # if not h/v continue
        ix1 = int(x1)
        ix2 = int(x2)
        iy1 = int(y1)
        iy2 = int(y2)

        if (ix1 != ix2) and (iy1 != iy2):
            print(F"xyxy is diagonal: {xyxy}")
            if (abs(ix1-ix2) == abs(iy1-iy2)):
                print(F"Good diag")
            else:
                print(F"Bad diag")
            #continue # move this!!

        # increment map for the coords for each point.
        plot (ix1,iy1,ix2,iy2)

    #print(F"{map}")

    overlaps = 0
    for x in map.values():
        if x > 1:
            overlaps += 1
    
    print(f"2+ overlaps:{overlaps}")

def plot(x1,y1,x2,y2):
    start = (x1,y1)
    end = (x2,y2)

    x = x1
    y = y1
    xstep = 0
    ystep = 0
    
    if x1 > x2:
        xstep = -1
    elif x1 < x2: 
        xstep = 1

    if y1 > y2:
        ystep = -1
    elif y1 < y2: 
        ystep = 1

    while True:
        point = (x,y)
        if point in map:
            hit = map.get(point)
            hit += 1
            map.update({point: hit})
        else:
            map[point] = 1
        
        if (x,y) == end:
            return

        #increment x & y
        x += xstep
        y += ystep

main()