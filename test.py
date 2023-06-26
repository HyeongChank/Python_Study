dict1 = {'a':1, 'b':2,'c':3}
keys = dict1.keys()
print(list(keys))

values = dict1.values()
print(list(values))

items = dict1.items()
print(list(items))

for key, value in dict1.items():
    print(key)

aa = dict1.get('a')
print(aa)

searchkey = [key for key, value in dict1.items() if value==2]
print(searchkey)