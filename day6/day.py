text = ""

def main():

    f = open("day6\day.txt","r")
    #f = open("day6\sample.txt","r")

    for x in f:
        text = x.strip()

    fish = {}

    # Init to 0
    for i in range(-1,8+1):
        fish[i] = 0
    
    #print(F"Fish: {fish}")

    for t in text.split(','):
        count = fish.get(int(t))
        count += 1
        fish.update({int(t):count})

    print(F"Initial fish: {fish.values()}")

    one(fish)


def one(fish):
    # age by days
    agedfish = age(fish,256)
    
    # Total the aged fish
    total = 0
    print(F"Aged    fish: {agedfish.values()}")
    for v in agedfish.values():
        #print(F"adding val: {v}")
        total += v

    print(F"total fish: {total}")

def age(fishy, days):
    new_fish = {}
    prev_fish = fishy.copy()

    for d in range(days):

        # Age the fish
        for i in range(-1,8):
            #print(F"i is: {i}, it has:{fishy.get(i+1)}")
            before = prev_fish.get(i+1)
            new_fish.update({i:before})

        # Spawn new
        spawn = new_fish.get(-1)
        new_fish.update({8:spawn})

        age6 = new_fish.get(6)
        new_fish.update({6:age6+spawn})
        #print(F"Aged    fish: {new_fish.values()}")

        #pop the drop off
        new_fish.pop(-1)
        prev_fish = new_fish.copy()

    return new_fish

main()