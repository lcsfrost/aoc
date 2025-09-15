

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip())
    return l

def main():
    l = process_file()
    s = _build_dict(l)
    total = 0
    for k,v in s.items():
        total += len(v)
        print(k,v)
    print(total)
    # print(s)
    pass

"Questions for customs; yes or no, a through z"
"Identify Qs for which ANYONE in group answer yes"



def _build_dict(l:list) -> dict:
    i = 0
    group_counter = 0
    group_dict = {}
    def _parse_rows(rows):
        unique_questions = set()
        for i, row in enumerate(rows):
            if i == 0:
                unique_questions = unique_questions.union(set(row))
            else:
                unique_questions = unique_questions.intersection(set(row))
        return unique_questions
    row_list = []
    while i < len(l):
        row = l[i]
        if row:
            row_list.append(row) #Adding line of text for current passport
        else: #Hit a line break signifying end of passport
            new_group = _parse_rows(row_list)
            group_dict[group_counter] = new_group
            group_counter += 1
            row_list = []
        #Last line is not a new line so does not trigger passport creation
        #handling manually
        i += 1
    if row_list:
        new_group = _parse_rows(row_list)
        group_dict[group_counter] = new_group
    return group_dict


if __name__ == "__main__":
    main()

