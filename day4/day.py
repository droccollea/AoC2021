
import copy
text = []
caller = []
cards = []

def main():
    f = open("day4\day.txt","r")
    #f = open("day4\sample.txt","r")

    for x in f:
        text.append(str(x.strip()))

    one()
    #two()


def one():
    # Read line
    caller = text[0].split(",")
    print(F"Caller:{caller}")

    # Build cards
    card = []
    row = []
    for i in range(2, len(text)):
        # New card?
        if len(text[i]) == 0:
            card = []
            print(F"New card")
        else:
            row = text[i].split()
            card.append(row)
            if len(card) %5 == 0:
                cards.append(card)
    #print(F"Cards:{cards}")

    # TX cols to rows for simplicity.
    for card in cards:
        new_rows = []
        for i in range(0,5):
            new_row = []
            for row in card:
                new_row.append(row[i])
            new_rows.append(new_row)
        for r in new_rows:
            card.append(r)
    print(F"Cards:{cards}")

    # Iterate called numbers
    winning_cards = []
    for c in caller:
        # Check cards
        for card_id in range(len(cards)):
            # Skip if alrady a winner
            if winning_cards.count(card_id) > 0:
                continue 
            # rows in card
            card = cards[card_id]
            for row in card:
                #number in row
                for num in row:
                    if num == c:
                        #print(F"Hit on:{c}")
                        row.remove(c)
            if check_card(card):
                print(F"Winning card:{card}, id:{card_id}")
                #compute_score(card)
                print(F"Tally:{compute_score(card)*int(c)}")
                winning_cards.append(card_id)
                print(F"wining cards:{winning_cards}")
                #return

    print(F"Cards:{cards}")


def check_card(card):
    for row in card:
        if len(row) == 0:
            return True
    return False

def compute_score(card):
    tally = 0
    #get unique numbers and tally
    unique = []
    for row in card:
        for num in row:
            if unique.count(num) == 0:
                tally += int(num)
                unique.append(num)
    return tally

main()