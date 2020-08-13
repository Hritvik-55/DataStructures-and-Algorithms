def func(s):
    s=s.lower()
    length=len(s)
    haspmap=[0]*26
    for i in range(length):
        haspmap[ord(s[i])-ord('a')]+=1
        if (haspmap[ord(s[i])-ord('a')]>1):
            return False
    return True

string="Mam"
print(func(string))