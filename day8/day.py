text = []
sequences = []

segments = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

digit_overlaps = {
    0: [7],
    1:[],
    2: [],
    3: [7],
    4:[],
    5: [],
    6: [5],
    7:[],
    8:[],
    9: [3,4,7]
}

def main():

    f = open("day8\day.txt","r")
    #f = open("day8\sample.txt","r")

    for x in f:
        text.append(x)
    
    #one()
    two()

def one():
    uniques = 0
    for digits in sequences:
        for digit in digits:
            if len(digit) in segments.values():
                #print(F"unique: {digit}")
                uniques += 1
    
    print(F"Uniques: {uniques}")

def two():

    total = 0
    for t in text:
        l,r = t.split(' | ')
        
        mixed = l.split()
        print(F"Mixed seq: {mixed}")

        sorted_seq = []
        for i in mixed:
            sorted_seq.append(''.join(sorted(i)))
        
        print(F"Sorted seq: {sorted_seq}")

        identified = decode(sorted_seq)

        print(F"Decoded: {identified}")
        
        # Decode the pin and add to total
        pin = ''
        for num in r.split():
            # sort num and lookup index in identified list      
            pin += str(identified.index(''.join(sorted(num))))
        print(F"pin is: {pin}")
        total += int(pin)
        print(F"Total: {total}")



def decode(mixed):
    #given a mixed list decode it and return a new list
    decoded = []
    for i in range(10):
        decoded.append('')

    # Find 1,4,7,8
    decoded[1] = locate(mixed,1,1,decoded)
    decoded[4] = locate(mixed,4,4,decoded)
    decoded[7] = locate(mixed,7,7,decoded)
    decoded[8] = locate(mixed,8,8,decoded)

    # Knowing 4, find 9 from 6,9,0 # to find: 23560
    decoded[9] = locate(mixed,9,4,decoded)
            
    # Knowing 1, Find 0 from 0,6 # to find: 2356
    decoded[0] = locate(mixed,0,1,decoded)

    # Only 6 left at that segment length # to find: 235
    decoded[6] = locate(mixed,6,6,decoded)
            
    # Knowing 1, Find 3 from 2,3,5 # to find: 25
    decoded[3] = locate(mixed,3,1,decoded)

    # Knowing 9, find 5 from 2,5 # to find: 5
    decoded[5] = locate(mixed,5,9,decoded)

    # Only 2 left at that segment length - all done?
    decoded[2] = locate(mixed,2,2,decoded)

    #print(F"Decode list: {decoded}")
    return decoded


def locate(mixed,find,containing,identified):

    # Filter out on length and unidentified
    remaining = []
    for cand in mixed:
        if len(cand) == segments.get(find) and cand not in identified:
            remaining.append(cand)

    # Single candidate, return it.
    if len(remaining) == 1:
        #print(F"{find} must be: {remaining[0]}")
        return remaining[0]
    
    #print(F"lookin for subset in these: {remaining}")
    # Look for a subset in the sought item
    subset = identified[containing]
    for cand in remaining:
        matched_segs = 0
        for c in subset:
            if c in cand:
                matched_segs += 1
        if matched_segs == len(subset):
            #print(F"{find} : {subset} in {cand}")
            return cand
        elif find == 5 and matched_segs == len(subset)-1: # special case needs to match all but 1 seg 
            return cand
            #print(F"{find} : {subset} not in {cand}")
    print(F"Didnt find!!: {find}")

main()