def listConcat(a_list, b_list):
    c_list = a_list[::2] + b_list[1::2]
    return c_list


lista = [0,1,2,3,4,5,6,7,8,9,10]
listb = [0,1,2,3,4,5,6,7,8,9,10]
print(listConcat(lista,listb))