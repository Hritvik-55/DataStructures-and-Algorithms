def func(lst,n):
    mydict=dict()
    min=-1
    for i in range(n-1,-1,-1):
        if lst[i] in mydict.keys():
            min=i
        else:
            mydict[lst[i]]=1
    if (min!=-1):
        print("First Element to recurr is : ",lst[min])
    else:
        print("No elements repeat")

arr=[10,5,3,4,3,6]
n=len(arr)
func(arr,n)