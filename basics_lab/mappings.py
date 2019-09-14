import os.path

dict_sample ={}

list = type(dir(os.path))

for k in dir(os.path):
    for k in k:
        print(type(k))




#print(list)
#print(list.count(dict_sample))

#dict_sample = list.__module__
#print(dict_sample)