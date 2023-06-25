#count the triplets in the given list:
def subarray(arr):
    for i in arr:
        for j in lst:
            if i!=j:
                sum=i+j
                if sum in arr:
                    print(i,"+",j," = ",sum)
    return "Task completed"
lst=[1, 5, 3, 2]
print(subarray(lst))

'''
But the output is:

1 + 2  =  3
3 + 2  =  5
2 + 1  =  3
2 + 3  =  5
Task completed
'''
