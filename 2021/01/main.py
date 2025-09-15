import os



def process_file():
    l = []
    path = os.path.join(os.getcwd(), "input.txt")
    print(path)
    with open("input.txt") as file:
        for line in file:
            l.append(int(line.strip()))
    return l

def part_one():
    l = process_file()
    i = 1
    count = 0
    while i < len(l):
        if l[i] > l[i-1]:
            count +=1
        i +=1
    return count

def part_two():
    l = process_file()
    i = 3
    count = 0
    while i < len(l):
        prev = sum(l[i-x] for x in range(1,4)) #three
        cur = sum(l[i-x] for x in range(0,3))
        if cur > prev:
            count +=1
        i +=1
    return count

def main():
    ans = part_one()
    print(ans)
    ans = part_two()
    print(ans)

if __name__ == "__main__":
    main()