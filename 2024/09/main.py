"""Rules:
Disk map alterates between representing files and free space.
12345 = 1 block file, 2 blocks free space, 3 block file, 4 blocks free space, 5 block file
90909 = 9 block files separated by 0 blocks of memory
Each file on disk has an ID number based on the order of the files as they appear BEFORE they are rearranged, starting with ID 0.

So the desk map 12345 has three files.

1. Create files based on the disk map showing space used, and the current ID number, like so:
    12345 = 0..111....22222
    1 = 1 block with ID 0
    2 = 2 free spaces, respented by "."
    3 = 3 block with ID 1

    
Each individual file has a file number 

"""
import re

def main():
    disk_map = process_file()
    file_name = create_file_name(disk_map)
    filled = fill_storage_space(file_name)
    checksum = calc_checksum(filled)
    # print(file_name)
    print(checksum)

def process_file() -> str:
    l = []
    with open("input.txt") as file:
        for line in file:
            return line.strip()

def create_file_name(row) -> list:
    l = []
    file_id = 0
    for i, num in enumerate(row):
        if i & 1 == 1: #Divisible by 2
            a = "."
        else:
            a = str(file_id)
            file_id += 1
        for i in range(int(num)):
            l.append(a)
    return l

def fill_storage_space(file_name_list) -> str:
    left = 0
    right = len(file_name_list)-1
    end_of_file = len(file_name_list)-1
    while left < right:
        if file_name_list[left].isnumeric() == False and file_name_list[right].isnumeric():
            file_name_list[left] = file_name_list[right] #Replace left value (should be a .) with right value (should be a number)
            file_name_list[right] = "."
        while file_name_list[left].isnumeric(): #Leftmost character is a number, do not replace
            left +=1
        while file_name_list[right].isnumeric() == False: #Rightmost character is not a number, do not swap.
            right -= 1
    return "".join(file_name_list)

def calc_checksum(input):
    total = 0
    for i, val in enumerate(input):
        if val.isnumeric() == False:
            return total
        total += i*int(val)
    return total

def test():
    print("""
###########################################
################## TESTS ##################
###########################################
""")
    a = create_file_name("2333133121414131402")
    # A validation
    a_str = "".join(a)
    a_intended_output = "00...111...2...333.44.5555.6666.777.888899"
    a_check = a_str == a_intended_output
    print(f"{a_str = } {a_check = } {a_intended_output = }")

    # B validation
    b = fill_storage_space(a)
    b_str = str(b)
    b_intended_output = "0099811188827773336446555566.............."
    b_check = b == b_intended_output
    print(f"{b_str = } {b_check = } {b_intended_output = }")
    
    c = calc_checksum(b_str)
    c_str = str(c)
    c_intended_output = 1928
    c_check = c == c_intended_output
    print(f"{c_str = } {c_check = } {c_intended_output = }")

    print(calc_checksum("0099811188827773336446555566.............."))
    print("""
""")


if __name__ == "__main__":
    main()
    test()