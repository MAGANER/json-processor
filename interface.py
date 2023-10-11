import functions

def __exists(commands, head):
    return head in commands.keys()
def __parse_command(com):
    splitted = com.split(" ")
    return (splitted[0],splitted[1:])
        
def run():
    while True:
        command = input(">")
        command_head ,*args = __parse_command(command)
        args = args[0] #make it flat
        
        if __exists(functions.commands,command_head):
            functions.commands[command_head](args)
        else:
            print("command {} doesn't exist!".format(command_head))
        
