array1=[1,2,3,7,5]
n=5
def subarray_with_sum(array1,n):
    sub = []
    for i in range(len(array1)):
        sub.append(array1[i])
        while(sum(sub)>n):
            sub.pop(0)
        if(sum(sub)==n):
            return sub
    return []

print(subarray_with_sum(array1,5))