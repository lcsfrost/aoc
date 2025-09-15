

def load_expense_report():
    expense = []
    with open("input.txt") as file:
        for line in file:
            expense.append(int(line.strip()))
    return expense

def part_one():
    target = 2020
    expenses = load_expense_report() 
    odds = []
    evens = []
    for i in expenses:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    for i in evens:
        for j in evens:
            if i+j == target:
                return i*j
    for i in odds:
        for j in odds:
            if i+j == target:
                return i*j
    
def part_two():
    expenses = load_expense_report() 
    target = 2020
    i,j,k = 0,0,0
    l = len(expenses)-1
    while i < l:
        j=0
        while j<l:
            k=0
            while k <l:
                s = sum([expenses[i],expenses[j],expenses[k]])
                if s == target:
                    return expenses[i]*expenses[j]*expenses[k]
                k += 1
            j += 1
        i += 1

def main():
    x = part_one()
    print(x)
    y = part_two()
    print(y)
if __name__ == "__main__":
    main()