import re

#Match all instances of "mul(1-3 numbers, 1-3numbers)"
#Multiply together
#Sum totals


### mul     [(]\d{1,3},\d{1,3}[)]



def process_file():
    file_total = 0
    do_state = True
    with open("mult.txt") as file:
         for line in file:
            line_total, do_state = extract_and_multiply_numbers(line, do_state)
            file_total += line_total
    return file_total

def extract_and_multiply_numbers(str, do_state = True):
        re_str = r"mul[(]\d{1,3},\d{1,3}[)]|do[(][)]|don[']t[(][)]"
        mul_str_list = re.findall(re_str,str)
        line_total_sum = 0
        for str in mul_str_list:
            if str == "do()":
                do_state = True
                continue
            if str == "don't()":
                do_state = False
                continue
            if str == None:
                continue
            if do_state == True:
                just_numbers = re.findall(r'\d{1,3}',str)
                product = int(just_numbers[0]) * int(just_numbers[1])
                line_total_sum += product
        return line_total_sum, do_state

def test():
    test_str_list = ["mul(4,5)",
            "lum(4,5)",
            "mul(a,6)",
            "mul(323,456)",
            "mul(1234,5678"
]
    total = 0

    for i in test_str_list:
        product = extract_and_multiply_numbers(i)
        total += product
    print(total)

if __name__ == "__main__":
    print(process_file())