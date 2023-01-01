import functions

def __exists(commands, head):
    return head in commands.keys()
def __parse_command(com):
    splitted = com.split(" ")
    return (splitted[0],splitted[1:])
        
def run():
    while True:
        command = input(">")
        parsed = __parse_command(command)
        if __exists(functions.commands,parsed[0]):
            functions.commands[parsed[0]](parsed[1])
        else:
            print("command {} doesn't exist!".format(parsed[0]))
        
