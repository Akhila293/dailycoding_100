# Number of sockpairs in the list(updated). 
def sockMerchant(n, ar):
    dic={num:0 for num in ar}
    for i in ar:
        dic[i]+=1
    pairs_total = 0
    for v in dic.values():
        pairs_total += v//2        
    return pairs_total
   
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)
