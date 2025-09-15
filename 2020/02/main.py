import re

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append([int(x) if x.isdigit() else x for x in re.findall(r"\w+", line.strip())])

    return l

def part_one():
    pass_audit_list = process_file()
    return sum([validate_pass(x, 0) for x in pass_audit_list])

def part_two():
    pass_audit_list = process_file()
    return sum([validate_pass(x, 1) for x in pass_audit_list])

def validate_pass(pass_data, rule_set):
    match rule_set:
        case 0:
            return _sled_rules(pass_data)
        case 1:
            return _toboggan_rules(pass_data)
    
def _toboggan_rules(row):
    min = row[0] -1 #Converting from nth char to index
    max = row[1] -1 #Converting from nth char to index
    char = row[2] #char 
    pass_str = row[3] #str
    if (pass_str[min] == char) ^ (pass_str[max] == char):
        return 1
    else:
        return 0

def _sled_rules(row):
    min = row[0]
    max = row[1]
    char = row[2]
    pass_str = row[3]
    s = sum([1 for x in pass_str if x == char])
    if s >= min and s <= max:
        return 1
    else:
        return 0

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()