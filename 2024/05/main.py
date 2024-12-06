
"""
Rules:
Pairs of numbers - key must be printed before value (store in hashmap)

List of pages to be processed using page rules hashmap

Return:
What do you get if you add up the middle page number from those correctly-ordered updates?

X | Y
X must come before Y
Y must come after X
"""


class pageSorter():
    def __init__(self) -> None:
        self.pages_raw_data = self.read_file_data()
        self.prior_pages_rules_dict, self.following_pages_rules_dict = self.extract_rules()
        self.pages_list = self.extract_pages()
        self.part_one_ans, self.part_two_ans = self.validate_part_two()
        pass

    def validate_part_one(self):
        total = 0
        for row in self.pages_list:
            row_safe = True
            for j, page_number in enumerate(row):
                # page_rule_list = set(self.rules_dict[page_number]) #These pages must not appear after page_number
                # next_pages_in_row = set(row[j::])
                prior_page_rule_list = self.prior_pages_rules_dict[page_number] #These pages must not appear after page_number
                following_pages_rule_list = self.following_pages_rules_dict[page_number]
                next_pages_in_row = row[:j]
                following_pages_in_row = row[j::]
                for k in next_pages_in_row:
                    if k in prior_page_rule_list:
                        row_safe = False
                        break
                for k in following_pages_in_row:
                    if k in following_pages_rule_list:
                        row_safe = False
                        break
            if row_safe:
                total += row[len(row)//2] #Whoaaaoa we're halfway theeere
        return total


    def validate_part_two(self):
        """For this one we need to:
        Find the updates which are not in the correct order. 
        What do you get if you add up the middle page numbers after correctly ordering just those updates?
        """
        total = 0
        incorrect_row_total = 0
        for row in self.pages_list:
            row_safe = True
            for j, page_number in enumerate(row):
                # page_rule_list = set(self.rules_dict[page_number]) #These pages must not appear after page_number
                # next_pages_in_row = set(row[j::])
                prior_page_rule_list = self.prior_pages_rules_dict[page_number] #These pages must not appear after page_number
                next_pages_in_row = row[:j]
                for k in next_pages_in_row:
                    if k in prior_page_rule_list:
                        row_safe = False
                        break
            if row_safe:
                total += row[len(row)//2] #Whoaaaoa we're halfway theeere
            else:
                incorrect_row_total += self.reorder_row(row)
        return total, incorrect_row_total
    
    def reorder_row(self, row):
        left = 0
        right = 0
        while left <= len(row)-1:
            right = left
            while right <= len(row)-1:
                if row[right] in self.prior_pages_rules_dict[row[left]]:
                    row[left], row[right] = row[right], row[left]
                    self.reorder_row(row)
                right += 1
            left += 1
        return row[len(row)//2]

    def read_file_data(self):
        file_contents = []
        with open('pages.txt') as file:
            for line in file:
                file_contents.append(line)
        return file_contents

    def extract_rules(self):
        prior_pages_rules_dict = {}
        following_pages_rules_dict = {}
        for row in self.pages_raw_data:
            if "|" in row:
                page_numbers = [int(x) for x in row.split("|")]
                prior_page = page_numbers[0] #Prior Page number - rule exists for this page
                seguiendo_pagina = page_numbers[-1] #Number that must come after prior page
                if prior_pages_rules_dict.get(prior_page, False) == False:
                    prior_pages_rules_dict[prior_page] = [seguiendo_pagina]
                else:
                    l = prior_pages_rules_dict[prior_page]
                    l.append(seguiendo_pagina)
                    prior_pages_rules_dict[prior_page] = l
                if following_pages_rules_dict.get(seguiendo_pagina, False) == False:
                    following_pages_rules_dict[seguiendo_pagina] = [prior_page]
                else:
                    l = following_pages_rules_dict[seguiendo_pagina]
                    l.append(prior_page)
                    following_pages_rules_dict[seguiendo_pagina] = l
            else:
                break #Rows are sorted in source data, can escape when all are processed.
        return prior_pages_rules_dict, following_pages_rules_dict

    def extract_pages(self):
        pages_list = []
        for row in self.pages_raw_data:
            if "," in row:
                row.strip()
                pages_list.append([int(x) for x in row.split(",")])
        return pages_list

    
def main():
    x = pageSorter()
    print(f"{x.part_one_ans = }")
    print(f"{x.part_two_ans = }")

if __name__ == "__main__":
    main()