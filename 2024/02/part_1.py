
##########################
# Part 1 Rules
# 1. Levels must be all increasing or all decreasing
# 2. Difference between numbers must be between 1 and 3 inclusive.
##########################


##########################
# Part 2 Rules
# 1. Problem Dampener exists - you can allow one unsafe condition.
##########################

import csv

d = {}

def is_safe(l):
    i = 1
    safety_counter = 0
    comparison_dict = {}
    while i <= len(l)-1:
        if abs(l[i]-l[i-1]) not in [1,2,3]:
            safety_counter += 1
            return False
        if l[i] > l[i-1]:
            comparison_dict["greater"] = comparison_dict.get("greater",0) +1
        else: 
            comparison_dict["lesser"] = comparison_dict.get("lesser",0) +1
        i +=1
    
    print(l, comparison_dict)
    if len(comparison_dict) == 1:
        #Only greater or lesser numbers, no mix
        return True
    else:
        return False


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
    l_test = [[1,2,3],[3,2,1],[3,5,1],[1,8,20]]

    for i in l_test:
        print(is_safe(i))

if __name__ == "__main__":
    main()