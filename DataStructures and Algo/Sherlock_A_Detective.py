n=int(input())
arr=[int(ele) for ele in input().split(" ")]
for i in range(1,n+1):
    if i not in arr:
        print(i,end=" ")
print(" ")



