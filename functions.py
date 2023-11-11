import json
import os.path
from functools import reduce
from sys import exit

class Functions:
    data = ""
    ssn  = 10

    @staticmethod
    def _check_args(args,n,com_name):
        if len(args) != n:
            print("{} doesn't take {} arguments!".format(com_name,n))
            return False
        return True

    @staticmethod
    def _open(args):
        '''takes 1 argument and tries to open json file.'''
        if __class__._check_args(args,1,"open"):
            if os.path.isfile(args[0]):
                path = args[0].replace('\\\\', '\\')
                try:
                    with open(path,"r") as f:
                        __class__.data = json.load(f)
                except ValueError as e:
                    print("can not open {} file!".format(args[0]))
            else:
                print("{} doesn't exist or not regular file!".format(args[0]))

    @staticmethod
    def _save(args):
        '''write down created/changed json file'''
        if __class__._check_args(args,1,"save"):
            if __class__.data != "":
                with open(args[0],"w") as f:
                    json.dump(__class__.data,f)
            else:
                print("can not save json file! it was not opened at all!")

    @staticmethod
    def __chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]


    @staticmethod
    def _showk(args):
        '''showk - shows keys with 10 elements on 1 line by default'''
        if __class__._check_args(args,0,"showk") and __class__.data != "":
            keys = list(__class__.data.keys())
            keys = __class__.__chunks(keys,__class__.ssn)
            for k in keys:
                line = reduce(lambda a,b:"{} {} ".format(a,b),k)
                print(line)
                input()
                
    key_exists = lambda n: n in (list(__class__.data.keys()))
    def _addk(args):
        '''adds new key'''
        if __class__._check_args(args,1,"addk") and __class__.data != "":
            if not __class__.key_exists(args[0]):
                __class__.data[args[0]] = ""
            else:
                print("{} key already exists!".format(args[0]))
                
    def _showv(args):
        '''shows value of the key'''
        if _check_args(args,1,"showv") and __class__.data != "":
            if __class__.key_exists(args[0]):
                print(__class__.data[args[0]])
                
    def _init(args):
        '''creates empty json file, replacing opened/created file'''
        if __class__._check_args(args,0,"init"):
            __class__.data = {}
            
    def _change_ssn(args):
        '''change the number of printed keys on 1 line'''
        if __class__._check_args(args,1,"change_ssn"):
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
        if __class__._check_args(args,2,"change_val") and  __class__.data != "":
            if __class__.key_exists(args[0]):
                __class__.data[args[0]] = args[1]
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
       
commands = {
    ("exit","e"):        lambda args: exit(0),
    ("help","h"):        Functions._help,
    ("change_ssn","cn"): Functions._change_ssn,
    ("open","o"):        Functions._open,
    ("showk","sk"):      Functions._showk,
    ("save","s"):        Functions._save,
    ("addk","ak"):       Functions._addk,
    ("showv","sv"):      Functions._showv,
    ("init","i"):        Functions._init,
    ("change_val","cv"): Functions._change_val
    }

def h(head):
    for _h in commands.keys():
        fst,snd = _h
        if fst == head or snd == head:
            return _h
