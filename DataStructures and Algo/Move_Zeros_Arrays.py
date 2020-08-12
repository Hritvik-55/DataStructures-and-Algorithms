def func(lst):
    count=0
    for i in range(len(lst)):
        if lst[i]!=0:
            lst[count]=lst[i]
            count+=1
    while count<len(lst):
        lst[count]=0
        count+=1

arr=[0,1,0,3,12]
func(arr)
print(arr)
