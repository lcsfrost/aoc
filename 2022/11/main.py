import re



class Monkey():
    def __init__(self, rows) -> None:
        "Monkey num, starting item, operation, test conditions, true, false"
        self.build_monkey(rows)
        self.inspection_count = 0
        pass

    def __str__(self) -> str:
        l = ['']
        l.append(f"Monkey Id: {self.id} | Inspections: {self.inspection_count}")
        l.append(f"Item list: {self.item_list}")
        # l.append(f"Operation: {self.operation_str}")
        # old=100
        # l.append(f"{self.operation_str = } = " + str(eval(f"{self.operation_str}")))
        # l.append(f"Test: Divide by {self.test_divisor}, pass to {self.true_monkey_id} or {self.false_monkey_id}")
        # l.append(f"{self.inspection_count = }")
        return '\n'.join(l)

    def build_monkey(self, rows):
        for row in rows:
            a, b, c = row.partition(":")
            if "Monkey" in a:
                self.id = int(re.findall(r"\d+", a)[0])
            elif "Starting" in a:
                self.item_list = [int(x.strip()) for x in c.split(",")]
            elif "Operation" in a:
                self.operation_str = ''.join(c.split(" ")[-3:])
            elif "Test" in a:
                self.test_divisor = int(re.findall(r"\d+", c)[0])
            elif "true" in a:
                self.true_monkey_id = int(re.findall(r"\d+", c)[0])
            elif "false" in a:
                self.false_monkey_id = int(re.findall(r"\d+", c)[0])

    def take_turn(self):
        d = []
        while self.item_list:
            old = self.item_list.pop(0)
            new = eval(self.operation_str)
            new = new % self.modulo_val
            new_monkey_id = self.test_item(new)
            d.append([new_monkey_id, new])
            self.inspection_count += 1
        return d

    def test_following_value(self):
        old = self.item_list.pop(-1)
        print("Id:", self.id, "value: ", old)
        new = eval(self.operation_str)      
        new_monkey_id = self.test_item(new)
        return [[new_monkey_id, new]]

    def accept_item(self, item):
        self.item_list.append(item)

    def test_item(self, item):
        # print(item % self.test_divisor)
        if item % self.test_divisor == 0:
            return self.true_monkey_id
        else:
            return self.false_monkey_id

    def set_supermod_val(self, v):
        self.modulo_val = v

class MonkeyHandler():
    def __init__(self) -> None:
        self.build_monkeys()

    def process_file(self):
        l = []
        with open("input.txt") as file:
            for line in file:
                l.append(line.strip())
        return l

    def build_monkeys(self):
        self.monkey_dict = {}
        i = 0
        l = self.process_file()
        while i < len(l):
            if "Monkey" in l[i]:
                id = int(re.findall(r"\d+", l[i])[0])
                monkey_data = l[i:i+6]
                self.monkey_dict[id] = Monkey(monkey_data)
            i += 1

    def process_round(self):
        for monkey in self.monkey_dict.values():
            turn_results = monkey.take_turn()
            for result in turn_results:
                id = result[0]
                item = result[-1]
                self.monkey_dict[id].accept_item(item)

    def show_monkeys(self, i = None):
        if i is not None:
            print("\n"*5)
            print(f"{'=':=<20} Round number {i} {'=':=<20}")
        for v in self.monkey_dict.values():
            print(v)

    def test_route(self, id = 0):
        d = self.monkey_dict[id].test_following_value()
        for result in d:
            id = result[0]
            item = result[-1]
            self.monkey_dict[id].accept_item(item)
        return id

def main():
    Monkeh = MonkeyHandler()
    modulo_val = 0
    for k,v in Monkeh.monkey_dict.items():
        if k == 0:
            modulo_val = v.test_divisor
        else:
            modulo_val *= v.test_divisor
    for v in Monkeh.monkey_dict.values():
        v.set_supermod_val(modulo_val)
    i = 0
    monkey_id = 2
    id_list = [monkey_id]

    while i < 10000:
        Monkeh.process_round()
        # monkey_id = Monkeh.test_route(monkey_id)
        # id_list.append(monkey_id)
        Monkeh.show_monkeys(i+1)
        i += 1


if __name__ == "__main__":
    main()


"""
starting items listed current worry level for each item


Operation shows how worry level changes as an item is inspected
old = current_worry_level
new = eval(operation)
ezps

Test outlines how to test your worry level and determine where to throw it next

AFTER a monkey inspects
but BEFORE it tests your worry level
Your worry level is divided by three and rounded down (floored)

Monkeys take turns inspecting and throwing items.
Monkey turn:
1. Inspect all items one at a time in the order listed

Monkey 0 goes first
Monkey 1 goes next, etc.

All monkeys taking a turn = 1 round.

Thrown items go to end of target monkey's list

Turn:
1. Multiply by formula
Worry floored by 3
Item with worry level 500 thrown to target monkey

"""