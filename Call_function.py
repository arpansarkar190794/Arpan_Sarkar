a={1,2,3,4}
b={1,2}
def Unin():
    print('a union b is',a|b)
    print('a intersection b is',a&b)
    print('a-b is',a-b)
    print('After discarding 1 from a',a.discard(1),a)
    print(type(a))
    print('Difference of a and b is',a.difference(b))
    print('Updation of a after subtraction',a.difference_update(b),a)
    print('Removing element 4 from a',a.remove(4),a)
Unin()



