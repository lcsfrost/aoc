import timeit
from multiprocessing import Pool
import multiprocessing
import math

# def process_file():
#     l = []
#     with open('input.txt') as file:
#         for line in file:
#             l.append(line.strip())
#     return l

def row_generator(filename):
    # This generator yields lines one by one, rather than returning a large list.
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
            # digits = len(str(i))
            digits = int(math.log10(i)) + 1
            concat_val = j * (10 ** digits) + i
            temp_list.append(concat_val)
        l = temp_list
    if target in l:
        return target
    else:
        return 0


def main():
    with Pool(processes=12) as p:
        # imap lazily consumes the generator, so we don't store all lines in memory at once.
        results = p.imap(check_row, row_generator('input.txt'))
        total = sum(results)
    print(total)

if __name__ == "__main__":
    print(multiprocessing.cpu_count())
    duration = timeit.timeit("main()", globals=globals(), number=1)
    print("Duration:", duration)
    #Test 1 speed: 6.630317799994373s
    #Test 2 changes: Stopped copying temp_list, just reassigned l to temp_list
    #Test 2 speed: 6.463524899998447s
    #Test 3 changes: Removing all print statements
    #Test 3 speed: 6.3357784999971045s
    #Test 4 changes: Multiprocessing
    #Test 4 speed: 1.807641599996714s
    #Test 5 changes: Changed from string concatenation to math for concatenating characters
    #Test 5 speed: 1.3771873000077903s
    #Test 6 changes: Changed Pool().map to Pool().imap and changed file loading to file streaming
    #Test 6 speed: 1.284683000005316s