def func(arr,k):
    mydict=dict()
    for i in range(len(arr)):
        if (arr[i] in mydict.keys()):
            mydict[arr[i]]+=1
        else:
            mydict[arr[i]]=1
        i+=1
    for i in range(len(arr)):
        if (mydict[arr[i]]==k):
            return arr[i]
        i+=1

    return -1


arr=[1,7,4,3,4,8,7]
print(func(arr,5))