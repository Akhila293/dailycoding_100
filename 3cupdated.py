#missing number in an array: 
   def missingNumber(array,n):
        sum=(n+1)*n//2
        act=sum(array)
        return sum-array
n=int(input("Enter the length of the array: "))
lst=[1,2,4,5]
print("missing number is: ",missingNumber(lst,n))
