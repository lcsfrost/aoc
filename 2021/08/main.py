import os

Y = '2021'
D = '08'

"""
Quick notes and problem description:

Got into crab hole
Whale pursuing me; smashed entrance to cave.


4: 4
7: 3
1: 2
8: 7


Enry:
Left is 10 unique signal patterns | and then four digit output value

for char in l:
    length = len(char):


def parse_row(row):
    if len(char) == 2: #2 line segments
        set(char) = 1
    if len(char) == 4: #Four line segments
        set(char) = 4
    if len
"""



def solve_part_one():
    signal_list = process_file()
    
    d = {}
    # for i, j in signal_list:
        # print(i, j)
    build_dict(signal_list[0][0])
    return

def solve_part_two():
    l = process_file()
    return

def build_dict(signal_patterns):
    """Accepts list of 10 signal segment patterns
    returns dict where set is key, value is number associted with pattern.

    """
    d = {}
    while len(d) < len(signal_patterns):
        i = 0
        print(d)
        print(sorted([x for x in d.values()]))
        while i < len(signal_patterns):
            segments_set = set(tuple(signal_patterns[i]))
            segment_count = len(segments_set)
            segment_tuple = tuple(segments_set)
            if segment_tuple not in d:
                print(segment_count, segments_set)
                match segment_count:
                    case 6: #6 segments, can be 6, or 0
                        one_matches = [k for k, v in d.items() if v == 1]
                        four_matches = [k for k, v in d.items() if v == 4]
                        if one_matches: #Checks if 1 is in dictionary
                            if len(segments_set.intersection(set(one_matches[0]))) == 1: #1 and 6 have 1 line segment in common
                                d[segment_tuple] = 6
                            elif len(segments_set.intersection(set(one_matches[0]))) == 2:
                                if len(segments_set.intersection(set(four_matches[0]))) == 3:
                                    d[segment_tuple] = 0 #matches 0 AND 9. No good. 
                                elif len(segments_set.intersection(set(four_matches[0]))) == 4:
                                    d[segment_tuple] = 9
                    case 5: #5 segments, can be 2, 5, or 3\
                        one_matches = [k for k, v in d.items() if v == 1]
                        four_matches = [k for k, v in d.items() if v == 4]
                        if one_matches:
                            if len(segments_set.intersection(set(one_matches[0]))) == 2: #Matches 3
                                d[segment_tuple] = 3
                            elif len(segments_set.intersection(set(four_matches[0]))) == 3: #Matches 5
                                d[segment_tuple] = 5
                            elif len(segments_set.intersection(set(four_matches[0]))) == 2: #Matches 5
                                d[segment_tuple] = 2
                    case 2:
                        d[segment_tuple] = 1
                    case 3:
                        d[segment_tuple] = 7
                    case 4:
                        d[segment_tuple] = 4
                    case 7:
                        d[segment_tuple] = 8
            i += 1
    for k, v in dict(sorted(d.items(), key = lambda item: item[1])).items():
        print(v, k)
    return d



def process_file():
    l = []
    if os.path.basename(os.getcwd()) == 'aoc':
        input_path = os.path.join(os.getcwd(), Y,D,"input.txt")
    else:
        input_path = "input.txt"
    with open(input_path) as file:
        for line in file:
            a, _, b = line.strip().partition(" | ")
            a = a.split(" ")
            b = b.split(" ")
            l.append([a, b])
    return l

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {part_one_ans}")
    print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()