text = ""
crabs = []

def main():

    f = open("day7\day.txt","r")
    #f = open("day7\sample.txt","r")

    for x in f:
        text = x.strip()
    
    for t in text.split(','):
        crabs.append(int(t))

    #one()
    two()

def one():
    min_pos = min(crabs)
    max_pos = max(crabs)

    moves_to_pos = {}

    # Init the dict min to max?
    for i in range(min_pos,max_pos):
        moves_to_pos.update({i:0})

    # Loop keys and then loop positions
    for pos in range(min_pos,max_pos):
        moves = moves_to_pos.get(pos)
        
        for crab in crabs:
            # compute distance to move and add to moves_to_pos
            moves += abs(crab-pos)
            moves_to_pos.update({pos:moves})
    
    # Report min value
    print(moves_to_pos)
    print(F"Lowest moves is: {min(moves_to_pos.values())}")


def two():
    min_pos = min(crabs)
    max_pos = max(crabs)

    # build fuel cost lookup
    fuel_cost = {0:0}
    for f in range(1,max_pos+1):
        prev = fuel_cost.get(f-1)
        fuel_cost.update({f:prev+f})

    print(F"fuel lookup: {fuel_cost}")

    # Init the dict min to max
    moves_to_pos = {}
    for i in range(min_pos,max_pos):
        moves_to_pos.update({i:0})

    # Loop candidate positions and then crab positions and cost to get there
    for pos in range(min_pos,max_pos):
        moves = 0
        
        for crab in crabs:
            # compute distance to move and add to moves_to_pos
            #print(F"crab at {crab} needs {abs(crab-pos)} to get to {pos}")
            fuel = fuel_cost.get(abs(crab-pos))
            moves += fuel
            moves_to_pos.update({pos:moves})
    
    # Report min value
    print(moves_to_pos)
    print(F"Lowest moves is: {min(moves_to_pos.values())}")
main()