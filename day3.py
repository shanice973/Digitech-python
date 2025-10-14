my_dict ={"name":"shanice","age":20,"tribe":"kisii"}
print(my_dict)

#my_dict.clear()
#print(my_dict)

backup = my_dict.copy()
print(backup)

keys =["name","age","city"]
values ="unknown" 
default =dict.fromkeys(keys,values)
print(default)

getting =backup.get("age")
print(getting)

key1 = backup.keys()
print(key1)

values1 = my_dict.values()
print(values1)

all_item = backup.items()
print(all_item)

popping =backup.pop("names")
print(popping)
print(my_dict)

popitem = my_dict.popitem()
print(popitem)
print(my_dict)

new_dict =  {"name":"Lennox","country","kenya"}
setdefaulting = new_dict.setdefault("name","luo")
print(setdefaulting)

updating = my_dict.update(new_dict)
print(my_dict)

new_keys =["school","gender","class"]
new_values =["Barani","Female",8]
complete_dict =dict(zip(new_keys,new_values))
print(complete_dict)
