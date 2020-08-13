def func(lst11,lst2):
    lst3=[]
    for i in range(len(lst11)):
        lst3.append(lst11[i])
    for j in range(len(lst2)):
        if (lst2[j] not in lst3):
            lst3.append(lst2[j])
    return len(lst3)


print(func([1,2,3,4,5],[1,2,3,4,5,6,7,8,9]))
