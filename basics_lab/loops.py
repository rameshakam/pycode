import sys


while __name__=="__main__":
    #args = input("calculator")
    #print(sys._base_executable,sys.api_version,sys.argv,sys.base_exec_prefix,sys.base_prefix)
    fns = dir(sys)
    print(fns)
    break


for fn in dir(sys):

    module_dict={}
    module_dict.update(type(fn)=fn)
    print (module_dict)
    #if type(fn) == "func"
    #print(fn)
