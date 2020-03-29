with open('names.txt', encoding='utf8') as f:
    #Read first line to get started
    print(f.tell())
    #Read in all lines first, then loops through
    for one_line in f.readlines():
        print(one_line[:-1], f.tell())

