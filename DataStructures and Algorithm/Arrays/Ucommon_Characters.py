maxchar=26
def func(str1,str2):
    str2.lower()
    str1.lower()
    arr=[0]*maxchar
    for i in range(maxchar):
        arr[i]=0
    for i in range(0,len(str1)):
        arr[ord(str1[i])-ord('a')]=1
    for i in range(len(str2)):
        if (arr[ord(str2[i])-ord('a')]==1 or arr[ord(str2[i])-ord('a')]==-1):
            arr[ord(str2[i])-ord('a')]=-1
        else:
            arr[ord(str2[i])-ord('a')]=2
    for i in range(len(arr)):
        if(arr[i]==1 or arr[i]==2):
            print(chr(i+ord('a')),end="")

func("characters","alphabets")