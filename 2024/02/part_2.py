
##########################
# Part 1 Rules
# 1. Levels must be all increasing or all decreasing
# 2. Difference between numbers must be between 1 and 3 inclusive.
##########################
# Part 2 Rules
# 1. Problem Dampener exists - you can allow one unsafe condition.
##########################

import csv

def is_safe(row, loop_level = 0):
    copied_row = row.copy() #Copying row each loop to preserve original for recursion purposes
    if loop_level > len(row):
        return False #We've tested all iterations removing 1 element, and none passed.
    
    if loop_level != 0: #Don't need to remove anything for first iteration. 
        copied_row.pop(loop_level-1)
    i = 1
    safety_violation_counter = 0
    comparison_dict = {}
    while i <= len(copied_row)-1:
        if abs(copied_row[i]-copied_row[i-1]) not in [1,2,3]:
            safety_violation_counter += 1
        if copied_row[i] > copied_row[i-1]:
            comparison_dict["greater"] = comparison_dict.get("greater",0) +1
        else: 
            comparison_dict["lesser"] = comparison_dict.get("lesser",0) +1
        i +=1

    if len(comparison_dict) == 1 and safety_violation_counter == 0:
        return True
    else:
        loop_level +=1
        print(copied_row, comparison_dict, False)
        return is_safe(row,loop_level)

def main():
    safety_dict = {}
    with open("reports.txt") as f:
        reader = csv.reader(f, delimiter=' ')
        
        for i in reader:
            i = [int(j) for j in i]
            report_safety_bool = is_safe(i)
            safety_dict[report_safety_bool] = safety_dict.get(report_safety_bool, 0) + 1
    print(safety_dict)

def tests():
    l_test = [[1,2,3],[3,2,1],[3,5,1],[1,8,20],[1,10,2,3],[1,10,15,2,3], [48,46,45,44,40,41]]

    for i in l_test:
        print(is_safe(i))

if __name__ == "__main__":
    main()