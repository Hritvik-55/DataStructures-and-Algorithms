def func(str):
    str=str.lower()
    mydict=dict()
    for i in str:
        if (i in mydict):
            return i
        else:
            mydict[i]=1
str="GeeksForGeeks"
print(func(str))

