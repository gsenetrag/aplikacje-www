list = [1,2,3,4,5,6,7,8,9,10]
list2 = list[5:10]
list = list[0:5]

print(list)
print(list2)

list3 = [0]+list+list2
list4 = list3

print(list4[::-1])