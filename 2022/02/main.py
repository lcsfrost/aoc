D = {"AX":3,
"AY":6,
"AZ":0,
"BX":0,
"BY":3,
"BZ":6,
"CX":6,
"CY":0,
"CZ":3,}

D1 = {"AX":0+3,
"AY":3+1,
"AZ":6+2,
"BX":0+1,
"BY":3+2,
"BZ":6+3,
"CX":0+2,
"CY":3+3,
"CZ":6+1,}


D2 = {"X":1,"Y":2,"Z":3}



def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            a, b = line.strip().split(" ")
            
            l.append((a, b))
    return l

def score_row(row):
    a, b = row
    c = a+b
    print(f"Opponent throws {D1[a]} and you throw {D1[b]} for {D[c]} points")

    return D[c] + D2[b]

def score_part_two(row):
    a, b = row
    c = a+b
    return D1[c]

def main():
    l = process_file()
    score = 0
    for row in l:
        score += score_part_two(row)
    print(score)


if __name__ == "__main__":
    main()