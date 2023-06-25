#sub array with the given sum
def subarray(arr,s):
    c=0
    for i in range(0,len(arr)-1):
           sum=arr[i]
           for j in range(i+1,len(arr)):
               sum=sum+arr[j]
               if sum==s:
                   return [i+1,j+1]
                   
    return [-1]

lst=[1,2,3,4,5,6,7,8,9,10]
s=int(input())
print(subarray(lst,s))
