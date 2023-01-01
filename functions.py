import json
import os.path
from functools import reduce


def __check_args(args,n,com_name):
    if len(args) != n:
        print("{} doesn't take {} arguments!".format(com_name,n))
        return False
    return True

def __open(args):
    if __check_args(args,1,"open"):
        if os.path.isfile(args[0]):
            try:
                with open(args[0],"r") as f:
                    __state["data"] = json.load(f)
            except ValueError as e:
                print("can not open {} file!".format(args[0]))
        else:
            print("{} doesn't exist or not regular file!".format(args[0]))

def __save(args):
    if __check_args(args,1,"save"):
        if __state["data"] != "":
            with open(args[0],"w") as f:
                json.dump(__state["data"],f)
        else:
            print("can not save json file! it was not opened at all!")

def __chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

data_exists = lambda :__state["data"] != ""
def __showk(args):
    if __check_args(args,0,"showk") and data_exists:
        keys = list(__state["data"].keys())
        keys = __chunks(keys,__state["ssn"])
        for k in keys:
            line = reduce(lambda a,b:"{} {} ".format(a,b),k)
            print(line)
            input()
key_exists = lambda n: n in (list(__state["data"].keys()))
def __addk(args):
    if __check_args(args,1,"addk") and data_exists():
        if not key_exists(args[0]):
            __state["data"][args[0]] = ""
        else:
            print("{} key already exists!".format(args[0]))
def __showv(args):
    if __check_args(args,1,"showv") and data_exists():
        if key_exists(args[0]):
            print(__state["data"][args[0]])
            
def __change_ssn(args):
    if __check_args(args,1,"change_ssn"):
        val = args[0]
        if val.isnumeric():
            __state["ssn"] = int(val)
        else:
            print("incorrect argument type or value!")
            
__state = {
    "data":"",  #containts json file
    "ssn":10 #showing string number represents how many strings will be printed with show command
}
commands = {
    "exit": lambda args: exit(0),
    "change_ssn": lambda args: __change_ssn(args),
    "open": lambda args: __open(args),
    "showk": lambda args: __showk(args),
    "save": lambda args: __save(args),
    "addk": lambda args: __addk(args),
    "showv": lambda args:__showv(args)
    }
