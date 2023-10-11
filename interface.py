import functions
from functions import h
from sys import argv
from functools import reduce

def __create_command_heads_tuple():
    heads = []
    for head in functions.commands:
        fst,snd = head
        heads.append(fst)
        heads.append(snd)
    return tuple(heads)
    
def __parse_command(com):
    splitted = com.split(" ")
    return (splitted[0],splitted[1:])

def __run_command(command,heads):
    command_head ,*args = __parse_command(command)
    args = args[0] #make it flat
    if command_head in heads:
        functions.commands[h(command_head)](args)
    else:
        print("command {} doesn't exist!".format(command_head))
def run():
    heads = __create_command_heads_tuple()

    if len(argv) == 1:
        while True:
            command = input(">")
            __run_command(command,heads)
    else:
        s = reduce(lambda a,b:a+" "+b,argv[1:]) + ";"
        commands = list(filter(lambda n: n != "", s.split(";")))

        if len(commands) == 2 and commands[1] == '':
            print("error: every command should be finished with ';'")
            exit(-1)
        for c in commands:
            if c[0] == ' ':
                c = c[1:]
            __run_command(c,heads)
        
            
        
