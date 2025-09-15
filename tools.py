import argparse
import os
import pyperclip
import shutil

def init_new_challenge(year, day, input = False):
    target_folder = os.path.join(os.getcwd(), year, f"{day:0>2}")
    os.makedirs(target_folder, exist_ok=True)
    template_path = os.path.join(os.getcwd(),"Config/template.py")
    print(template_path)
    template_target = os.path.join(target_folder, "main.py")
    print(template_target)
    shutil.copy2(template_path, template_target)
    with open(template_path, "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if 'YEAR_PLACEHOLDER' in lines[i]:
            lines[i] = lines[i].replace('YEAR_PLACEHOLDER', year)
        if 'DAY_PLACEHOLDER' in lines[i]:
            lines[i] = lines[i].replace('DAY_PLACEHOLDER', f"{day:0>2}")
    with open(template_target, "w") as f:
        f.writelines(lines)
    if input:
        input_path = os.path.join(target_folder, "input.txt")
        with open(input_path, "w") as f:
            instructions = pyperclip.paste().replace('\r','')
            f.write(instructions)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aoc arguments")
    parser.add_argument("-y", required=False)
    parser.add_argument("-d", required=False)
    parser.add_argument("-input", required=False)
    args = parser.parse_args()
    if args.y and args.d:
        init_new_challenge(args.y, args.d, input = args.input)
