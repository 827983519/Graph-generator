import re
import sys
import time

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
        print "\n"
        return 0
    else:    
        line.strip()
        line = line[:-1]
        return line

def check_command(line): 
    
    
    sp = re.split(r'\s',line)   
    command1 = sp[0].strip()
    

    if command1 != 'a' and command1 != 'c' and command1 != 'r' and command1 != 'g':
        print ("Error: unknown command \"%s\""%(command1))
        return -1
    
    elif command1 == 'a':
        check_command_format("a",line)
             
    elif command1 == 'c':
        check_command_format("c",line) 

    elif command1 == 'r':
        check_command_format("r",line) 

    elif command1 == 'g':
        check_command_format("g",line)   

    

    
def check_command_format(input,line):
    if input == "a" :
        pa = re.compile(r'a +"(.*)" +((\(\d+,\d+\) *)+)')
        if pa.search(line) == None:
            print "Error:wrong command format"
            return -1

        else:
            sp = re.split(r'\s"|"\s',line)
            str_name = pa.search(line).group(1)
            str_num = pa.search(line).group(2)
            
            num_patt = re.compile(r'\d')

            if num_patt.findall(str_num) !=  num_patt.findall(sp[2]):
                print "Error:wrong command format"
                return -1
            
            else:
                my_dict[str_name] = str_num
    
    if input == "c" :
        pa = re.compile(r'c +"(.*)" +((\(\d+,\d+\) *)+)')
        if pa.search(line) == None:
            print "Error:wrong command format"
            return -1

        else:
            sp = re.split(r'\s"|"\s',line)
            str_name = pa.search(line).group(1)
            str_num = pa.search(line).group(2)
            
            num_patt = re.compile(r'\d')

            if num_patt.findall(str_num) !=  num_patt.findall(sp[2]):
                print "Error:wrong command format"
                return -1
            
            elif my_dict.has_key(str_name) == False:
                print "Error:\'c\' or \'r\' specified for a street that does not exist."
                return -1
            
            else:
                my_dict[str_name] = str_num
            
    
    if input == "r" :
        pa = re.compile(r'r +"(.*)" *')
        str_name = pa.search(line).group(1)
    
        if pa.search(line) == None:
            print "Error:wrong command format"
            return -1
        
        elif  my_dict.has_key(str_name) == False:
            print "Error:\'c\' or \'r\' specified for a street that does not exist."
            return -1
        else:
            del my_dict[str_name]

    if input == "g" :
        if len(line) != 1 and line != "g":
            print "Error:wrong command format"
            return -1

#def add_street():

#def change_street():

#def draw_graph():

#def remove_street():




instruction()
while True:
    
    comm = get_command()
    if comm != 0:
        ret = check_command(comm)

    if  command == 'a' :
        continue#add_street()
    elif  command == 'c':
       continue# change_street()
    elif  command == 'r':
       continue# remove_street()
    elif  command == 'g':
       continue# draw_graph()
    
    #time.sleep(100)
        

'''
def check_command(line): 
    sp = re.split(r'\s',line)   
    command1 = sp[0].strip()
    sp = re.split(r'\s"|"\s',line)
   
    if command1 != 'a' and command1 != 'c' and command1 != 'r' and command1 != 'g':
        print ("Error: unknown command \"%s\""%(command1))
        return -1


    elif command1 == 'a' or command1 == 'c':
        if len(sp) != 3:
            print "Error: wrong command format"
        elif command1 == 'a':
            str_name = sp[1].strip()
            nums = sp[2]
            if check_num(nums) == -1:
                return -1

        elif command1 == 'c':
            str_name = sp[1].strip()
            pattern = re.compile(r'\d+')
            num = pattern.findall(sp[2].strip()) 
            if (check_num() == -1):# or (check_street() == -1):
                return -1      
    
    elif command1 == 'r':
        if len(sp) != 2:
            print "Error: wrong command format"
            return -1
        else:
            str_name = sp[1].strip()
    
    elif command1 == 'g':
        if len(sp) != 1:
            print "Error: wrong command format"
            return -1
    
    else:
        return 1

'''

'''
def check_num(nums):
    pattern = re.compile(r'\d+')
    num = pattern.findall(nums.strip())

    pattern1 = re.compile(r'(\(\d+,\d+\))+')

    if len(num) == 0:
        print "Error: wrong command format"
        return -1
    if len(num) != (len(pattern1.findall(nums)) * 2) :
        print "Error: wrong coordinate format"
        return -1
    return 1
'''