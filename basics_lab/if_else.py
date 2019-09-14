from sys import platform as platform


#platform= platform.capitalize()
print(type(platform))

x =123.45

y= lambda x,y:x+x+y
#print (y(2,3))

def func_name(func_pos_arg=10,*tup,**kwargs):
    return [func_pos_arg,tup,kwargs]




if(__name__ == "__main__"):


    #1 " ".format(var)
    print("platform of the script{}".format(platform))

    #2 Template version
    print(f"printing func result:{func_name(func_pos_arg=6,platform,fun=platform[0:2],Bool=True)}")
