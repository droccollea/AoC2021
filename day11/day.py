grid = []

def main():

    f = open("day11\day.txt","r")
    #f = open("day11\sample.txt","r")

    for line in f:
        row = []
        for o in range(len(line.strip())):
            row.append(int(line[o]))
        grid.append(row)

    one()


def one():
    flash_count = 0

    # Increment all
    for loop in range(500):
        
        for y in range(10):
            for x in range(10):
                grid[y][x] += 1
        
        flashers = []

        #print_grid("after inc")

        # Check flashes - anything == 10, and add to flash list and increment count
        latest = check_flashes()
        flashers.extend(latest)

        #print(F"Loop {loop} flashers: {flashers}")

        # Loop flashes and for each increment neightbours and check if they are to be added to list
        while len(flashers) > 0:
            (x,y) = flashers.pop(0)

            #print(F"Flash length: {len(flashers)}")

            increment_neighbours(x,y)

            #print_grid("after neighbours")
            
            latest = check_flashes()
            for l in latest:
                if l not in flashers:
                    flashers.append(l)
            #print(F"Found another {len(latest)} flashers")
            
            #print_grid()
        # reset the flashers to 0 - anything > 9 and add these to total flashed to date
        flash_this_loop = reset_flashers()
        flash_count += flash_this_loop
        if flash_this_loop == 100:
            print(F"all flashed on {loop+1}")
            break
        #print_grid("after reset " + str(loop))

    print(F"Flashes: {flash_count}")

def increment_neighbours(x,y):            
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if i >= 0 and j >= 0 and i < 10 and j < 10:
                #print(F"incr: {i},{j}")     
                grid[i][j] += 1

def check_flashes():
    flashing = []
    # Check flashes - anything == 10, and add to flash list and increment count
    for y in range(10):
        for x in range(10):
            if grid[y][x] == 10:
                flashing.append((x,y))
                #print(F"Adding {x},{y}")
    return flashing

def reset_flashers():
    count = 0
    for y in range(10):
        for x in range(10):
            if grid[y][x] >= 10:
                grid[y][x] = 0
                count += 1
    return count

def print_grid(s):
    print(F"The grid " + s)
    for y in range(10):
        print(grid[y])

main()