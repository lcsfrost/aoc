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
import itertools

class PartTwo():
    def __init__(self):
        self.disk_map = self.process_file()
        self.file_name = self.decompress_disk_map(self.disk_map)
        self.block_name_list = self.decompress_disk_map(self.disk_map)

        pass

    def process_file(self) -> str:
        l = []
        with open("input.txt") as file:
            for line in file:
                return line.strip()

    def decompress_disk_map(self, row: str) -> list:
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

    def fill_storage_space(self, file_name_list: list) -> str:
        left = 0
        matching_file_block_search = 0
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
        return file_name_list

    def blockfill_storage_space(self, file_name_list: list) -> str:
        left = 0
        right = len(file_name_list)-1
        end_of_file = len(file_name_list)-1

        #Inline function because I.. don't... know. I just didn't want to refactor this into a class.
        def check_for_block(pointer, length):
            # Returns True if block from pointer to pointer+length all == "."
            for i in range(length+1):
                if file_name_list[pointer].isnumeric() == True: #One of these characters is a number not a '.' "
                    return False
            return True
        
        while left < right and right > left: #Left pointer is within bounds.
            if file_name_list[left].isnumeric() == False and file_name_list[right].isnumeric():
                file_name_list[left] = file_name_list[right] #Replace left value (should be a .) with right value (should be a number)
                file_name_list[right] = "."

            while file_name_list[right].isnumeric() == False: #Rightmost character is not a number, do not swap.
                right -= 1

            #Found an element that is a number.
            #Need to find how many elements are the same number in a row (including the current element).
            search_pointer = right
            current_value = file_name_list[right]
            length = 0
            while file_name_list[search_pointer] == current_value:
                length += 1
                search_pointer -= 1
            search_pointer = 0
            keep_searching = True
            while keep_searching and search_pointer < end_of_file:
                if check_for_block(left, length) == True:
                    keep_searching = False
                    for i in range(length):
                        file_name_list[search_pointer+i] = file_name_list[right-i]    
                        file_name_list[right-i] = "."
                search_pointer += 1
            left +=1
        return file_name_list

    def calc_checksum(self, input: list):
        total = 0
        for i, val in enumerate(input):
            if val.isnumeric() == False:
                return total
            total += i*int(val)
        return total

    def find_first_free_block (self, length):
        self.starting_index = 0
        end_of_list = len(self.file_name)
        left = self.starting_index
        counter = 0
        while left < end_of_list:
            char = self.block_name_list[left]
            if char.isnumeric():
                pass

def solve_part_one():
    x = PartTwo()

    disk_map = x.process_file()
    file_name = x.decompress_disk_map(disk_map)
    filled = x.fill_storage_space(file_name)
    checksum = x.calc_checksum(filled)
    print(checksum)

def solve_part_two():
    x = PartTwo()
    disk_map = x.process_file()
    file_name = x.decompress_disk_map(disk_map)
    filled = x.blockfill_storage_space(file_name)
    checksum = x.calc_checksum(filled)
    print(checksum)

def test_part_one():
    x = PartTwo()
    print("""
###########################################
################## TESTS ##################
###########################################
""")
    a = x.decompress_disk_map("2333133121414131402")
    # A validation
    a_str = "".join(a)
    a_intended_output = "00...111...2...333.44.5555.6666.777.888899"
    a_check = a_str == a_intended_output
    print(f"{a_str = } {a_check = } {a_intended_output = }")

    # B validation
    b = x.fill_storage_space(a)
    b_str = "".join(b)
    b_intended_output = "0099811188827773336446555566.............."
    b_check = b == b_intended_output
    print(f"{b_str = } {b_check = } {b_intended_output = }")
    
    c = x.calc_checksum(b_str)
    c_str = str(c)
    c_intended_output = 1928
    c_check = c == c_intended_output
    print(f"{c_str = } {c_check = } {c_intended_output = }")

    print(x.calc_checksum("0099811188827773336446555566.............."))
    print("""
""")

def test_part_two():
    x = PartTwo()
    print("""
###########################################
################## TESTS ##################
###########################################
""")
    a = x.decompress_disk_map("2333133121414131402")
    # A validation
    a_str = "".join(a)
    a_intended_output = "00...111...2...333.44.5555.6666.777.888899"
    a_check = a_str == a_intended_output
    print(f"{a_str = } {a_check = } {a_intended_output = }")

    # B validation
    b = x.blockfill_storage_space(a)
    b_str = "".join(b)
    b_intended_output = "00992111777.44.333....5555.6666.....8888.."
    b_check = b == b_intended_output
    print(f"{b_str = } {b_check = } {b_intended_output = }")

if __name__ == "__main__":
    test_part_two()