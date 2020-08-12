def func(str):
    lst=str.split(" ")
    maxlen=-1
    for i in lst:
        if len(i)>maxlen:
            maxlen=len(i)
            result=i
    return result    

a="hey how are you bfhvhfvhfdy bhbfhbvhbhgbvhjgfbvhgfbhg"
print(func(a))