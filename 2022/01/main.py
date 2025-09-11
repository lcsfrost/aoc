

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip())
    return l

def get_max_score(l):
    max_val = 0
    current_val = 0
    for i in l:
        if i == '':
            if current_val > max_val:
                max_val = current_val
            current_val = 0
        else:
            current_val += int(i)
    return max_val


def get_top_three(l):
    calorie_list = []
    current_val = 0
    for i in l:
        if i == '':
            calorie_list.append(current_val)
            current_val = 0
        else:
            current_val += int(i)
    calorie_list.sort()
    print(calorie_list)
    cal_total = sum(calorie_list[-3::])
    print(cal_total)
    return cal_total

def main():
    l = process_file()
    # max_val = get_max_score(l)
    # print(max_val)
    print(get_top_three(l))



if __name__ == "__main__":
    main()