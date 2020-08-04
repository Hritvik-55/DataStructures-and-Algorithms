def func(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                return "Duplicate Item Found"
            else:
                return "All the elements are distinct"
arr=[1,6,5,2]
print(func(arr))