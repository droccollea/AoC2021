text = []

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
closing_scorer = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
def main():

    f = open("day10\day.txt","r")
    #f = open("day10\sample.txt","r")

    for line in f:
        text.append(line.strip())
        
    one()


def one():
    opening_chars = "{[(<"
    illegal_chars = []
    close_scores = []
    incomplete_scores = []

    for line in text:
        stack = []
        for c in line:
            # if opening char, append to stack.
            if c in opening_chars:
                stack.append(c)
                #print(F"appened: {c}")
            # else if expected closing, pop off stack
            elif len(stack) > 0 and c == closing.get(stack[-1]):
                stack.pop()
                #print(F"closed: {c}")
            # else illegal char. Record and stop this line
            else:
                illegal_chars.append(c)
                # Clear stack!
                stack = []
                #print(F"illegal: {c}")
                break
    
        # Two
        # If stack not empty, its an incomplete line.
        if len(stack) > 0:
            score = 0
            # reverse close then add close score to a list for later
            stack.reverse()
            for c in stack:
                score = (score * 5) + closing_scorer.get(c)
            print(F"autocomplete score: {score}")
        
            incomplete_scores.append(score)

    # sort scores, get abs of len/2 and take that as the answer.
    incomplete_scores.sort()
    middle = int((len(incomplete_scores)/2))
    print(F"Of {len(incomplete_scores)},middle is : {middle} ")
    print(F"middle is: {incomplete_scores[middle]}")
    

main()