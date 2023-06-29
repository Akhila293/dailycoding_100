# Number of sockpairs in the list. 
def sockMerchant(n, ar):
    # Write your code here
    temp=[]
    dic={}
    c=0
    for i in ar:
        if i not in temp:
            temp.append(i)
    for i in temp:
        count=0
        for j in ar:
            if i==j:
                count+=1
        dic[i]=count
    for key,val in dic.items():
        p=val//2
        c=c+p
    return c
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)
