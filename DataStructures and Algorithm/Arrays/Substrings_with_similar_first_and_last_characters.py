def func(s):
    n=len(s)
    result=0
    for i in range(n):
        for j in range(i,n):
            if s[i]==s[j]:
                result+=1
    return result

s="abcab"
print(func(s))