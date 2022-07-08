'''Python file I/O program. Emulates basic file reading operation.'''
import argparse
import os

# message for -h command to run program
MSG = "run command -->eg: python utility.py -l file"
# Initialize parser
parser = argparse.ArgumentParser(description= MSG)
# adding arguments
parser.add_argument("-l", "--lines", help = "Count number of lines")
parser.add_argument("-c", "--characters", help = "Count number of characters")
parser.add_argument("-w", "--words", help = "Count number of words")
parser.add_argument("-n", "--numerics", help = "Show only numeric data")
parser.add_argument("-a", "--alphabets", help = "Show only alphabets")

def fileapplications(arg):
    '''
    Reads the text file and returns integer or string based on input command
    :param args: arguments consists of input command data given by user
    :return : integer or string based on command input
    '''
    try:
        #-c: no. of character present in a file
        if arg.characters:
            file_content = open(os.path.abspath(str(arg.characters)),encoding="utf-8")
            character = sum(1 for character in file_content.read() if character.rstrip())
            return character
        #-l: should display no. of lines present in a file
        elif arg.lines:
            with open(os.path.abspath(str(arg.lines)),encoding="utf-8") as lines:
                lines = sum(1 for line in lines if line.rstrip())
                return lines
        # -w: no. of words in a file
        elif arg.words:
            file_content = open(os.path.abspath(str(arg.words)),encoding="utf-8")
            return len(file_content.read().split())
        #-n: should display only numeric numbers in input file
        elif arg.numerics:
            return numeric_data(arg)
        #-a: should display only alphabets in input file
        elif arg.alphabets:
            return alpha_data(arg)
    except Exception as exception:
        raise exception

def numeric_data(arg):
    '''
    Reads the text file and returns string numerics based on input command
    :param args: arguments consists of input command data given by user
    :return : string
    '''
    flag=0
    file_content = open(os.path.abspath(str(arg.numerics)),encoding="utf-8")
    characters =""
    for character in file_content.read():
        if character.isdigit() is True or character == " ":
            if character==" " and flag:
                flag=0
                characters = characters+character
            elif character!=" ":
                characters = characters+character
                flag=1
    return characters.strip()

def alpha_data(arg):
    '''
    Reads the text file and returns string alphabets based on input command
    :param args: arguments consists of input command data given by user
    :return : string
    '''
    file_content = open(os.path.abspath(str(arg.alphabets)),encoding="utf-8")
    characters =""
    for character in file_content.read():
        if character.isalpha() is True or character==" ":
            characters = characters+character
    return characters.strip()

args =parser.parse_args()
data = fileapplications(args)
print(data)
