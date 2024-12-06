"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; 
the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

"""




import re





def load_from_file():
    l = []
    with open('games.txt') as file:
        for line in file:
            l.append(line.strip())
    return l


def process_line(line):
    l = line.split(":")
    game_number_str = l[0]
    game_number = int(re.findall(r"\d{1,5}", game_number_str)[0])
    print(game_number_str, game_number)
    game_data_str = l[-1]
    if check_colour(game_data_str):
        return game_number
    else:
        return 0

def check_colour(line):
    color_extracting_regex = r"\d{1,3} blue|\d{1,3} green|\d{1,3} red"  
    games_data = re.findall(color_extracting_regex, line)
    colour_dict = get_rules_dict()
    # print(games_data)
    for i in games_data:
        c = i.strip().split(' ')
        colour = c[-1]
        number = int(c[0])
        if number > colour_dict[colour]:
            print(f"Game invalid, number from game {i} is {number} which is greater than {colour} {colour_dict[colour]}")
            return False
    return True


def get_power(line):
    color_extracting_regex = r"\d{1,3} blue|\d{1,3} green|\d{1,3} red"  
    games_data = re.findall(color_extracting_regex, line)
    colour_dict = {}
    # print(games_data)
    for i in games_data:
        c = i.strip().split(' ')
        colour = c[-1]
        number = int(c[0])
        if colour_dict.get(colour,0) == 0:
            colour_dict[colour] = number
        else:
            if number > colour_dict[colour]:
                colour_dict[colour] = number
    power = 1
    for k, v in colour_dict.items():
        power *= v
    return power

def get_rules_dict():
    d = {
        'red':12,
        'green':13,
        'blue':14
    }
    return d


def main():
    games_list = load_from_file()
    total = 0
    for i in games_list:
        total += get_power(i)
    print(total)


if __name__ == "__main__":
    main()