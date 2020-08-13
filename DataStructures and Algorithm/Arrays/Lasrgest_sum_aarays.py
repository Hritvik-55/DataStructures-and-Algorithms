def func(lst):
    max=0
    max_so_far=0
    for i in range(len(lst)):
        max=max+lst[i]
        if (max_so_far<max):
            max_so_far=max
        if max<0:
            max=0
    return max_so_far

arr=[-2,-3,4,-4,-5,-6]
print(func(arr))