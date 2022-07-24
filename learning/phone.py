numbers=[0,1,2,3,4,5,6,7,8,9]
num1=["zero","one","two","three","four","five","six","seven","eight","nine"]
lmt=3
lst2=[]
i=0
nm=int(input("enter the number"))
while(nm!=0):
       mod=nm%10
       nm=int(nm/10)
       i+=1
       k=numbers.index(mod)
       lst2.append(num1[k])
lst2.reverse()
for i in range(0,i):
    print(lst2[i],end=" ")