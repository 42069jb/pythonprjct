array1 = [1, 2, 4, 5, 7]
array2 = [5, 6, 3, 4, 8]
array1.sort()
array2.sort()
pair=9
length1=len(array1)
length2=len(array2)


def find_pair(array1,array2,pair,length1,length2):
    list1=[]
    for item in array1:
        difference=pair-item
        k=array2.count(difference)
        if k>=1:
            while(k>0):
                list1.append((item,difference))
                k-=1
    return(list1)


print(find_pair(array1,array2,pair,length1,length2))