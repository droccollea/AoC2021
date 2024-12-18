grid = []

def main():

    f = open("day9\day.txt","r")
    #f = open("day9\sample.txt","r")

    for line in f:
        x=[]
        for c in line.strip(): 
            x.append(int(c))
        grid.append(x)
    
    low_points = one()
    two(low_points)

def one():

    # Work across and down the grid
    # Check top, right and below for lower else assume current is lowest
    low_points=[]
    for y in range(len(grid)):
        lowest = grid[0][0]
        for x in range(len(grid[y])):
            # If new low point add it and 
            if low_point(x,y,lowest):
                low_points.append((x,y))
                lowest = grid[y][x]
    
    print(F"Low points: {low_points}")

    total = 0
    for point in low_points:
        x,y = point
        total += grid[y][x] + 1
    print(F"Risk: {total}")
    #610 too high!
    return low_points

def low_point(x,y,lowest):
    # return true if point is lower than neighbours
    checking=grid[y][x]
    if checking < above(x,y) and checking < right(x,y) and checking < below (x,y) and checking < left (x,y) :
        return True

def above(x,y):
    if y-1 <0:
        return 99
    return grid[y-1][x]

def right(x,y):
    if x+1 >= len(grid[0]):
        return 99
    return grid[y][x+1]

def left(x,y):
    if x-1 < 0:
        return 99
    return grid[y][x-1]

def below(x,y):
    if y+1 >= len(grid):
        return 99
    return grid[y+1][x]

def two(low_points):
    # iterate low points.
    # for each point add all non-9 neighbours to a list
    # allow this to recurse but stop if all non-9 neighbours already found or there are none  

    basins = {}
    for (x,y) in low_points:
        basins.update({(x,y): explore(x,y,[])})

    # Sort basins and tally top 3
    print(F"Basins: {basins}")
    lengths = []
    for basin in basins.keys():
        lengths.append(len(basins.get(basin)))
        print(F"Basin at point: {basin} length: {len(basins.get(basin))}")
    
    lengths.sort()
    print(F"lengths: {lengths}")
    tally = 1
    for l in range(len(lengths)-3,len(lengths)):
        tally *= lengths[l]

    print (F"Tally is: {tally}")

def explore(x,y,points):
    # If out of bounds, already seen or a 9 return now
    # else add this point and recurse l/u/d/r neighbours
    print(F"explore points: {points}")
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or (x,y) in points or grid[y][x] == 9:
        return points
    points.append((x,y))
    print(F"explore points2: {points}")
    return explore(x,y+1, explore(x+1,y, explore(x,y-1, explore(x-1,y, points))))

main()