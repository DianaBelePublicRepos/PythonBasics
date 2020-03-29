with open('names.txt', encoding='utf8') as f:
    #Read first line to get started
    print(f.tell())
    one_line = f.readline()
    #Keep reading one line at a time until there are no more
    while one_line:
        print(one_line[:-1], f.tell())
        one_line = f.readline()