import re
"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""


def read_file():
    l = []
    with open('input.txt') as f:
        for line in f:
            l.append(line.strip())
    return l

def part_one():
    total = 0
    for i in read_file():
        matches = re.findall(r"\d",i)
        calibration_value = int(matches[0] + matches[-1])
        total += calibration_value
    return total

def part_two():
    total = 0
    regex_str = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))"
    conversion_dict = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
    }
    for i in read_file():
        matches = re.findall(regex_str,i)
        first = conversion_dict.get(matches[0], matches[0])
        last = conversion_dict.get(matches[-1], matches[-1])
        s = int(first + last)
        total += s
        print(f"{i    =    }{matches = }    {s = }")
    return total

print(part_two())
# print(part_one())