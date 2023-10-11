import functions
from functions import h

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
        
def run():
    heads = __create_command_heads_tuple()
    
    while True:
        command = input(">")
        command_head ,*args = __parse_command(command)
        args = args[0] #make it flat
        
        if command_head in heads:
            functions.commands[h(command_head)](args)
        else:
            print("command {} doesn't exist!".format(command_head))
        
