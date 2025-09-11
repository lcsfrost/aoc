

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip().split(' '))
    return l

def main():
    l = process_file()
    for i in l:
        print(i)
    pass





if __name__ == "__main__":
    main()

    """
    No space
    Need to delete files
    Browse filesystem using 
    $ cd
    $ ls
    (lists files and whatnot)
    

    Root directory is called /
    $ are commands you execute
    "cd blah" moves in one level
    "cd .." move up one level
    ls lists all files and directories
    123 abc = file name abc with size of 123
    dir xyz means folder exists wit name of xyz

    nested dict? or a binary tree kind of thing?

    def foo(d):
        for k, v in d.items():
            if 
    
    """

