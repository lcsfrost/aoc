

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip())
    return l[0]

def solve_part_one(s):
    i = 14
    target_len = 14
    end = len(s)
    while i < end:
        letter_set = [] #Add last four chars
        for j in range(target_len):
            letter_set.append(s[i-j-1])
        print(letter_set, s[i], s[i-20:i])
        if len(set(letter_set)) == target_len:
            
            return i
        i +=1

def main():
    signal = process_file()
    x = solve_part_one(signal)
    print(x)
    pass

"""Signal is interpreted one character at a time

Detect start of packet marker
start of packet: 4 characters that are all different

Identify the first position where the four most recently 
received characters were all different.

# of chars from beginning of before to end of four-character marker

PART TWO:
Need to look for messages
Start of message = 14 distinct characters rather than 4
"""

if __name__ == "__main__":
    main()