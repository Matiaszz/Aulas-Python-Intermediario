def add_clients(item, list=None):
    if list == None:
        list = []
    list.append(item)
    return list


l1 = []
c1 = add_clients('Allan', l1)
c1.append('João')

c2 = add_clients('Maria')
c2.append('Matheus')

c3 = add_clients('Jose')
c3.append('Fernando')

c4 = add_clients('Jose')
c4.append('Fernando')
print(c1)
print(c2)
print(c3)
print(c4)
