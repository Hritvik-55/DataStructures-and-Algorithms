b=["Quora","Amazon","Amazon","Google","Microsoft","Quora","Google","Microsoft"] 
def func(lst):
    mydict=dict()
    for i in b:
        if i not in mydict:
            mydict[i]=0
        else:
            mydict[i]+=1
    for j in mydict.values():
        if mydict[j]==1:
            print(mydict.keys())


func(b)
