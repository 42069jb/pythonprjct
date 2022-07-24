#greaetst in list
'''numbers=[1,3,45,6,2,5,8]
max=0
for item in numbers:
    if max<item:
        max=item
    else:
        max=max
print(max)'''

#reading a list from the user
'''numbers=[]
lmt=int(input("enter the limit"))
for i in range(0,lmt):
    nm=int(input("enter the number"))
    numbers.append(nm)

print(numbers)'''

#removing the duplicate from a list alg 1
'''lst=[2,4,5,6,3,5,4,7,8,2,5]
lst1=[]
lst.sort()
print(lst)
length=len(lst)
print(length)
lst1.append(lst[0])
for i in range(0,length-1):
    temp=lst[i]
    if lst[i]!=lst[i+1]:
        lst1.append(lst[i+1])
print(lst1)'''

##removing the duplicate from a list alg 2 simple

lst1=[9,10,7,4,3,2,2,3,5,6,4,3,5,7,9]
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)

lst2.sort()
print(lst2)
lst2.reverse()
print(lst2)