#The syntax for seek is file.seek(position[whence])
with open('names.txt', encoding='utf8') as f:
    #Read first line to get started
    print(f.tell())
    endoftheroad = len(f.readlines())
    print(endoftheroad)
    one_line = f.readline()
    f.seek(endoftheroad)
    print(f.tell())
    #We reset the pointed back to the top of the file
    f.seek(0)
    print(f.tell())