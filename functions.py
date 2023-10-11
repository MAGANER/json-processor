import json
import os.path
from functools import reduce
from sys import exit

def __check_args(args,n,com_name):
    if len(args) != n:
        print("{} doesn't take {} arguments!".format(com_name,n))
        return False
    return True

def _open(args):
    '''takes 1 argument and tries to open json file.'''
    if __check_args(args,1,"open"):
        if os.path.isfile(args[0]):
            try:
                with open(args[0],"r") as f:
                    __state["data"] = json.load(f)
            except ValueError as e:
                print("can not open {} file!".format(args[0]))
        else:
            print("{} doesn't exist or not regular file!".format(args[0]))

def _save(args):
    '''write down created/changed json file'''
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
def _showk(args):
    '''showk - shows keys with 10 elements on 1 line by default'''
    if __check_args(args,0,"showk") and data_exists:
        keys = list(__state["data"].keys())
        keys = __chunks(keys,__state["ssn"])
        for k in keys:
            line = reduce(lambda a,b:"{} {} ".format(a,b),k)
            print(line)
            input()
key_exists = lambda n: n in (list(__state["data"].keys()))
def _addk(args):
    '''adds new key'''
    if __check_args(args,1,"addk") and data_exists():
        if not key_exists(args[0]):
            __state["data"][args[0]] = ""
        else:
            print("{} key already exists!".format(args[0]))
def _showv(args):
    '''shows value of the key'''
    if __check_args(args,1,"showv") and data_exists():
        if key_exists(args[0]):
            print(__state["data"][args[0]])
def _init(args):
    '''creates empty json file, replacing opened/created file'''
    if __check_args(args,0,"init"):
        __state["data"] = {}
def _change_ssn(args):
    '''change the number of printed keys on 1 line'''
    if __check_args(args,1,"change_ssn"):
        val = args[0]
        if val.isnumeric():
            __state["ssn"] = int(val)
        else:
            print("incorrect argument type or value!")

def __convert_val_to_real_type(val):
    #TODO:process another data types
    if val.isdigit():
        return int(val)
    else:
        return val
def _change_val(args):
    '''change value of key'''
    if __check_args(args,2,"change_val") and data_exists():
        if key_exists(args[0]):
            __state["data"][args[0]] = args[1]
        else:
            print("{} key doesn't exist!".format(args[0]))

def _help(args):
    '''print help message'''
    for key in commands.keys():
        fst, snd = key
        if fst != "exit":
            val = commands[key]
            print("{}|{} -".format(fst,snd)+ val.__doc__)

    print("exit, e - quit the program")
            
__state = {
    "data":"",  #contains json file
    "ssn":10 #showing string number represents how many strings will be printed with show command
}
commands = {
    ("exit","e"):        lambda args: exit(0),
    ("help","h"):        _help,
    ("change_ssn","cn"): _change_ssn,
    ("open","o"):        _open,
    ("showk","sk"):      _showk,
    ("save","s"):        _save,
    ("addk","ak"):       _addk,
    ("showv","sv"):      _showv,
    ("init","i"):        _init,
    ("change_val","cv"): _change_val
    }

def h(head):
    for _h in commands.keys():
        fst,snd = _h
        if fst == head or snd == head:
            return _h
