from multiprocessing import Pool
import timeit
import multiprocessing
import math

def row_generator(filename):
    # Row generator rather than returning entire file. didn't actually save much time though
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def check_row(row):
    target, calibration_data = row.split(":")
    target = int(target)
    calibration_data = [int(x) for x in calibration_data.strip().split(" ")]
    l = [calibration_data[0]]
    for i in calibration_data[1:]:
        temp_list = []
        for j in l:
            temp_list.append(j+i)
            temp_list.append(i*j)
            digits = int(math.log10(i)) + 1 #math is faster than len(str(i))
            concat_val = j * (10 ** digits) + i #math is much faster than int(str(j)+str(i)) 
            temp_list.append(concat_val)
        l = temp_list
    if target in l:
        return target
    else:
        return 0

def main():
    with Pool(processes=12) as p:
        #imap over map to make use of generator and get started calculating faster
        results = p.imap(check_row, row_generator('input.txt'))
        total = sum(results)
    print(total)

if __name__ == "__main__":
    print(multiprocessing.cpu_count())
    duration = timeit.timeit("main()", globals=globals(), number=1)
    print("Duration:", duration)

""" 
    Test 1: baseline speed on first solve
    Time: 6.6303s 

    Test 2: Stopped using temp_list.copy() and just reassigned l to temp_list. No need to copy
    Time: 6.4635s
        
    Test 3: Removed all print statements 
    Time: 6.3357s

    Test 4: Set up multiprocessing with Pool().map()
    Time: 1.8076s

    Test 5: Changed from string concatenation to math for concatenating numbers
    Time: 1.3771s

    Test 6: Changed Pool().map to Pool().imap and changed file loading to file streaming
    Time: 1.2846s
    
    Possible improvements: 
        1. Depth first search, return early if number is greater than target, or if match is found.
        2. 
    
    """