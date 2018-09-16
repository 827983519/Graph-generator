import re
import sys
sys.path.append("/home/wade/Downloads/ECE 650 - Fall 2018 - 9142018 - 1011 AM")
from ag_intersect import *

command = ''
str_name = ''
num = []
street_name = []
street_coor = []
my_dict = {}


def instruction():
    print "\nPlease enter commnd:\n"
    print "a--add a street, \nc--change a street, \nr--remove a street, \ng--generate a graph\n"

def Error_message():
    print "\nError:\n"
    print "\nFor example: a \"Weber Street\" (2,-1) (2,2)"
    print "Please enter again:\n"


def get_command():
    line = sys.stdin.readline()
    if line == "\n":
        return 0
    else:    
        line.strip()
        line = line[:-1]
        return line

def check_command(line): 
    
    
    sp = re.split(r'\s',line)   
    command1 = sp[0].strip()
    

    if command1 != 'a' and command1 != 'c' and command1 != 'r' and command1 != 'g':
        print ("Error: unknown command \"%s\".\n"%(command1))
        return -1
    
    elif command1 == 'a':
        check_command_format("a",line)
    
    elif command1 == 'c':
        check_command_format("c",line)

    elif command1 == 'r':
        check_command_format("r",line) 

    elif command1 == 'g':
        return check_command_format("g",line)   

    

    
def check_command_format(input,line):
    if input == "a" :
        pa = re.compile(r'a +"(.*)" +((\(-?\d+.?-?\d*,-?\d+.?-?\d*\) *)+)')  
        if pa.search(line) == None:
            print "Error:wrong command format.\n"
            return -1
        else:
            sp = re.split(r'\s"|"\s',line)
            str_name = pa.search(line).group(1)
            str_num = pa.search(line).group(2)
    
            num_patt = re.compile(r'\d+')

            pa1 = re.compile(r'\(-?\d+,-?\d+\)')
            check_reap =  pa1.findall(line)

            for i in str_num:
                if i == '.':
                    print "Error:the coordinate should be integer.\n"
                    return -1

            for i in check_reap:
                if check_reap.count(i) != 1:
                    print "Error:Coordinate points are repeated.\n"
                    return -1
            
            
            if my_dict.has_key(str_name):
                print "Error:street already exists.\n"

            if num_patt.findall(str_num) !=  num_patt.findall(sp[2]):
                print "Error:wrong command format.\n"
                return -1
            
            else:
                my_dict[str_name] = str_num
                return 1
    
    if input == "c" :
        pa = re.compile(r'c +"(.*)" +((\(-?\d+.?-?\d*,-?\d+.?-?\d*\) *)+)')
        if pa.search(line) == None:
            print "Error:wrong command format.\n"
            return -1

        else:
            sp = re.split(r'\s"|"\s',line)
            str_name = pa.search(line).group(1)
            str_num = pa.search(line).group(2)
            print str_name
            print str_num
            num_patt = re.compile(r'\d')

            for i in str_num:
                if i == '.':
                    print "Error:the coordinate should be integer.\n"
                    return -1

            if num_patt.findall(str_num) !=  num_patt.findall(sp[2]):
                print "Error:wrong command format.\n"
                return -1
            
            elif my_dict.has_key(str_name) == False:
                print "Error:\'c\' or \'r\' specified for a street that does not exist.\n"
                return -1
            
            else:
                my_dict[str_name] = str_num
                return 1
                print my_dict
            
    
    if input == "r" :
        pa = re.compile(r'r +"(.*)" *')
        if pa.search(line) == None:
            print "Error:wrong command format.\n"
            return -1
        str_name = pa.search(line).group(1)
        if  my_dict.has_key(str_name) == False:
            print "Error:\'c\' or \'r\' specified for a street that does not exist.\n"
            return -1
        else:
            del my_dict[str_name]
            return 1
            print my_dict

    if input == "g" :
        if len(line) != 1 and line != "g":
            print "Error:wrong command format.\n"
            return -1
        else:
            return "g"







def draw_graph():
    street_line = []
    pattern = re.compile(r'-?\d+')
    for i in range(len(my_dict)): 
        temp = []
        num_list = pattern.findall(my_dict.values()[i])
        for j in range(0,len(num_list) - 2 ,2):        
            temp.append(line(point(int(num_list[j]),int(num_list[j + 1])), point(int(num_list[j + 2]), int(num_list[j + 3]))))
        street_line.append(temp)
    print street_line

    intersect_point = get_intersect(street_line)
    print  intersect_point







        
def main():
    instruction()
    while True:
        comm = get_command()
        if comm == 0:
            break
        else:
            ret = check_command(comm)

        if  ret == 'g':
            draw_graph()
    
    

    print 'Finished reading input.\n'
 
    sys.exit(0)

if __name__ == '__main__':
    main()