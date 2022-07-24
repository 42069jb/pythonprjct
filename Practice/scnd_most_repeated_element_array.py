repetition_list = []
charecter_list = []

def secFrequent(arr,n):

    for item in arr:
        if item not in charecter_list:
            charecter_list.append(item)
    print("character list= ",charecter_list)
    length=len(charecter_list)
    k=0
    add=0

    for k in range(0,length):
        for i in range(0,n):
           item=charecter_list[k]
           if arr[i]==item:
                add+=1
        repetition_list.append(add)
        k+=1
        add=0
    print("repetitions list= ",repetition_list)
    str=finding_element(charecter_list,repetition_list)
    return str

def finding_element(list1,list2):
    f=s=min(list2)
    for item in list2:
        if item>f:
            s=f
            f=item
        elif item>s and item!=f:
            s=item
    v=list2.index(s)
    return list1[v]

arr=["aaa","bbb","aaa","bbb","bbb","aaa","ccc","ccc","ccc","bbb","bbb","ccc"]
ls2=[]
n=len(arr)
st=secFrequent(arr,n)
print(st)



