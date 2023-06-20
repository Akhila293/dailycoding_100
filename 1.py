# 20-06-2023 print the numbers that are unique in the list.
lst=[3,4,5,2,3,5,1,6,7,2,7]
print("lst: ",lst)
temp=[]
di={}
for i in lst:
    if i not in temp:
        temp.append(i)
print("After removing duplicates: ",temp)        
for i in temp:
    count=0
    for j in lst:
        if i==j:
            count=count+1
    di[i]=count
print(di)
re=[]
for key,val in di.items():
    if val==1:
        re.append(key)
print("These are the values which are unique in the lst",re)
        
    
