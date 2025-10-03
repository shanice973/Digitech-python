#list
my_list=[1,2,11,3,4,5]
print(my_list)
#append adds an item to the end of the list,
my_list.append(6)
print(my_list)

#extend appends all items from an iterable to the end of the list
my_list.extend([7,8,9])
print(my_list)

#indexing starts counting from "0"
#insert inserts an item "x" at a specific position in the list
my_list.insert(3,8)
print(my_list)

#removes remove the first occurence of item "x" from the list
my_list.remove(8)
print(my_list)

#popping removes and returns the item at the default
popping = my_list.pop(8)
print(my_list,"removed elemnt is :", popping)

#count returns the number of iccurence of the item "x" in the list
counting =my_list.count(4)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

length = len(my_list)
print(my_list)

maximum = min(my_list)
print(maximum)

checking = 3 in my_list
print(checking)


my_list.clear()
print(my_list)
