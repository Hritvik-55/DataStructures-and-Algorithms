def func(lst,k):
    newlst=[]
    for i in range(len(lst)-k,len(lst)):
        newlst.append(lst[i])
    for i in range(0,len(lst)-k):
        newlst.append(lst[i])
    return newlst
arr=[1,2,3,4,45,6,74]
print(func(arr,3))
