from collections import defaultdict
import re

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip())
    return l

def validate_height(h_str):
        x = re.findall(r"\d+|\w+",h_str)
        # print(x, h_str)
        if len(x) != 2:
            return False
        height = int(x[0])
        unit = x[1]
        if unit == 'cm':
            return height >= 150 and height <= 193
        elif unit == 'in':
            return height >=59 and height <=76
        else:
            return False

FIELDS ={
'byr': lambda p: all([len(p)==4, int(p)>=1920, int(p)<=2002]),
'iyr': lambda p: all([len(p)==4, int(p)>=2010, int(p)<=2020]),
'eyr': lambda p: all([len(p)==4, int(p)>=2020, int(p)<=2030]),
'hgt': lambda p: validate_height(p),
'hcl': lambda p: bool(re.match(r"^#[0-9a-f]{6}$", p)),
'ecl': lambda p: p in ["amb", "blu", "brn", "gry", "grn", 'hzl', 'oth'],
'pid': lambda p: bool(re.match(r"^\d{9}$", p)),
'cid': lambda p: True,
}

FIELD_RULES ={
'byr':"""four digits; at least 1920 and at most 2002.""",
'iyr':"""four digits; at least 2010 and at most 2020.""",
'eyr':"""four digits; at least 2020 and at most 2030.""",
'hgt':"""num followed by in/cm; cm values between 150 and 193; in values between 59 and 76""",
'hcl':"""a # followed by exactly six characters 0-9 or a-f""",
'ecl':"""Exactly one of: amb blu brn gry grn hzl oth.""",
'pid':"""a nine-digit number, including leading zeroes.""",
'cid':"""ignored, missing or not."""
}



def validate_passports(passport, strict = False):
    required_fields = set(FIELDS.keys())
    required_fields.remove('cid')
    passport_fields = set(passport.keys())
    try:
        passport_fields.remove('cid')
    except KeyError as e:
        pass
    if strict == True:
        print(f"{"Valid": <5} | {"Cat": <5} | {'Value': <12} | Rules for Category")
        for k, v in passport.items():
            valid_bool = FIELDS[k](v)
            print(f"{str(valid_bool): <5} | {str(k): <5} | {v: <12} | {FIELD_RULES[k]}")
            if not valid_bool:
                passport["Valid"] = False
                return passport
    #Get failure code if already set, or return all fields present check
    passport["Valid"] = passport.get("Valid", required_fields == passport_fields)
    return passport

def part_two():
    l = process_file()
    passport_dict = _build_dict(l)
    count_d = defaultdict(int)
    for k,v in passport_dict.items():
        print(f"Passport # {k+1}")
        passport = validate_passports(v, strict=True)
        x = passport["Valid"]
        print(f"Result for Passport # {k+1} - {x}\n\n\n")
        count_d[x] += 1
    print(count_d)



def main():
    part_two()
    # part_one()


def part_one():
    l = process_file()
    passport_dict = _build_dict(l)
    count_d = defaultdict(int)
    for k,v in passport_dict.items():
        passport = validate_passports(v)

        x = passport["Valid"]
        count_d[x] += 1
    print(count_d)

def _build_dict(l:list) -> dict:
    i = 0
    passport_counter = 0
    passport_dict = {}
    def _parse_rows(rows):
        value_dict = {}
        for i in rows:
            key_value_pairs = i.split(' ')
            for key_val_str in key_value_pairs:
                x = key_val_str.split(':')
                k = x[0]
                v = x[1]
                value_dict[k] = v
        return value_dict
    row_list = []
    while i < len(l):
        row = l[i]
        if row:
            row_list.append(row) #Adding line of text for current passport
        else: #Hit a line break signifying end of passport
            new_passport = _parse_rows(row_list)
            passport_dict[passport_counter] = new_passport
            passport_counter += 1
            row_list = []
        #Last line is not a new line so does not trigger passport creation
        #handling manually
        new_passport = _parse_rows(row_list)
        passport_dict[passport_counter] = new_passport
        i += 1
    return passport_dict

if __name__ == "__main__":
    main()