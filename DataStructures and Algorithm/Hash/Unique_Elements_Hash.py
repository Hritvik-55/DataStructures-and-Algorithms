

def func(arr):
    for i in range(len(arr)):
        if arr.count(arr[i])==1:
            print (arr[i])

lst=[1,1,1,1,2,2,2,3,3,3,4,5,5,5,5,6,6,6,8,8,8]

func(lst)