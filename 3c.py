#missing number in an array: 
def missingNumber(array,n):
        # code here
        for i in range(1,n+1):
            if i not in array:
                return i
n=int(input())
array=[1,2,4,5]
print(missingNumber(array,n))
