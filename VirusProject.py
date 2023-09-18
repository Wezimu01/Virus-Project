import sys
import os


#reading variable
def reading():
    global the_lines 
    my_file = open('sfs.py', 'r') #open file for reading
    the_lines = my_file.readlines() #reading the lines into a list
    items = []
    for i in the_lines:
        items.append(i) #adding a newline to the new file
    my_file.close #closing the file


def writing (): #writing variable
    file = open('sfs.py', 'w')
    count = 0
    for x in the_lines:
        if count == 51:
            x = x.replace('\n', '; print( "Virus" ) \n')
        file.write(x)
        count = count + 1

    file.close #closing the file

if __name__ == '__main__':
    reading()
    writing()
