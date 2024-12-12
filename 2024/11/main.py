from collections import deque
from functools import cache
from pathlib import Path
import time
import math
import numpy as np


dirt_tionary = {}

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            for i in line.strip().split(" "):
                l.append(int(i))
    return l


def process_stone(stone, level):
    if level == 0:
        return 1 
    
    
    if (level, stone) in dirt_tionary:
        return dirt_tionary[(level, stone)]
    
    new_stones = []
    if stone == 0:
        new_stones.append(1)
    else:
        num_digits = math.floor(math.log(stone,10)) + 1
        if num_digits % 2 == 0:
            half = num_digits // 2
            first_half = stone // 10**half
            second_half = stone-first_half*10**half
            new_stones.extend((first_half, second_half))
        else:
            new_stones.append(stone * 2024)
    total_count = sum(process_stone(s, level - 1) for s in new_stones)

    dirt_tionary[(level, stone)] = total_count
    return total_count

def count_stones(stones, apply_count):
    total = 0
    for stone in stones:
        total += process_stone(stone, apply_count)
    return total

def main():
    stones = process_file()
    start = time.perf_counter()
    print(f"Number of stones after 25 blinks: {count_stones(stones, 25)}")
    print(f"Number of stones after 75 blinks: {count_stones(stones, 75)}")
    print(time.perf_counter()-start)


    
if __name__ == "__main__":
    main()
