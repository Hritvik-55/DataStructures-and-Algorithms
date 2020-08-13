def func(lst,num):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==num:
                print("Indices of the numbers are : ",i,j)
           
lst=[7,2,11,13]
func(lst,20)
