def func(str):
    str.lower()
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if (str[i]==str[j]):
                return str[i]



str="hello"
print(func(str))