

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip())
    return l

def main():
    solve_part_one()
    solve_part_two()

def solve_part_one():
    s = 0
    l = process_file()
    for row in process_file():
        s += score_row_part_one(row)
    print(s)

def score_row_part_one(row):
    a = set(row[:len(row)//2])
    b = set(row[len(row)//2:])
    c = a.intersection(b)
    print(a,b, c)
    total_priority = 0
    for char in c:
        prio = ord(char)
        prio = prio-64+26 if prio < 95 else prio-96
        print(char, prio)
        total_priority += prio
    return total_priority

def solve_part_two():
    l = process_file()
    i = 0
    total_score = 0
    current_group = []
    while i < len(l)+1:
        if i % 3 == 0:
            if current_group:
                a = set(current_group[0])
                # print(a)
                b = set(current_group[1])
                c = set(current_group[2])
                d = a.intersection(b).intersection(c)
                for char in d:
                    prio = ord(char)
                    prio = prio-64+26 if prio < 95 else prio-96
                    total_score += prio
                print(i, current_group)
                if i == len(l):
                    print(total_score)
                    return total_score
                else:
                    current_group = []
            current_group.append(l[i])
        else:
            current_group.append(l[i])
        i += 1

if __name__ == "__main__":
    main()

# first_half  = s[:len(s)//2]
# second_half = s[len(s)//2:]

    """
PART ONE:
A row is a rucksack's contents
Rucksacks contain items
Every item type is identified by a single character
Each rucksack has two compartments with equal items
Each compartment has an equal number of items

Create sets
Find union
Convert to priority score

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.


ord()-64 or -96

v = ord(char)
v = v-64 if v < 95 else v-96

"""