#New name to add with the \n to mark the end of the line
new_name = "Peña Calderon\n"

#Open names.txt in append mode with encoding
with open('names.txt', 'a', encoding='utf-8') as f:
    #Add the new name and \n to the end of the file
    f.write(new_name)

#File closes automatically after indentation
print('Done\n')
#Re-open the file with encoding and display contents
with open('names.txt',encoding='utf-8') as f:
    print(f.read())