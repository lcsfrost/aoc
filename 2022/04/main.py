

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip())
    return l

def main():
    l = process_file()
    c = 0
    for i in l:
        c += check_row(i)
    print(c)
    l = process_file()
    c = 0
    for i in l:
        c += check_row_two(i)
    print(c)

def check_row(row):
    a_range, b_range = row.split(',')
    a_range = a_range.split('-')
    b_range = b_range.split('-')
    print_row(row)
    a_start = int(a_range[0])
    b_start = int(b_range[0])
    a_end = int(a_range[1])
    b_end = int(b_range[1])
    
    if a_start <= b_start and a_end >= b_end:
        print("A range contains B", a_range, b_range)
        return 1
    elif a_start >= b_start and a_end <= b_end:
        print("B range contains A", a_range, b_range)
        return 1
    else:
        print("Row doesn't contain shit", a_range, b_range)
        return 0
    
def check_row_two(row):
    a_range, b_range = row.split(',')
    a_range = a_range.split('-')
    b_range = b_range.split('-')
    print_row(row)
    a_start = int(a_range[0])
    b_start = int(b_range[0])
    a_end = int(a_range[1])
    b_end = int(b_range[1])
    
    if a_start < b_start and a_end < b_start:
        print("B Range is before A Range", a_range, b_range)
        return 0
    elif a_start > b_end and a_end > b_end:
        print("A range is after B range", a_range, b_range)
        return 0
    else:
        print("Row doesn't contain shit", a_range, b_range)
        return 1
    

def print_row(row):
    print('\n\n')
    a_range, b_range = row.split(',')
    a_range = a_range.split('-')
    b_range = b_range.split('-')
    s = ''
    for i in range(100):
        if i >=int(a_range[0]) and i <=int(a_range[1]):
            s += '|'
        else:
            s += '.'
    print(s)
    s = ''
    for i in range(100):
        if i >=int(b_range[0]) and i <=int(b_range[1]):
            s += '|'
        else:
            s += '.'
    print(s)

"""
Section have ID numbers

Section pairs are provided as so:
2-4, 6-8
2-3,4-5

etc
Split on , then -
min and max to see if sections are contained within each other?


Count how many assignment pairs there are where one range fully contains the other

if start<start and end > end
"""















if __name__ == "__main__":
    main()