def jumpingNumbers(number):
    y=number
    number=abs(number)
    number_list = []
    flag=1
    if number>=0 and number<=9:
        flag=0
    elif flag==1:
        while int(number)!=0:
            last_number=int(number%10)
            number_list.append(int(last_number))
            number=number/10
        number_list.reverse()
        check_list1=[]
        check_list2=[]
        for item in number_list:
            check_list1.append(item+1)
            check_list2.append(item-1)
        number_list.pop(0)
        check_list2.pop(len(check_list2)-1)
        check_list1.pop(len(check_list1)-1)
        print(number_list)
        print(check_list1)
        print(check_list2)
        f=0
        for i in range(0,len(number_list)):
            temp=number_list[i]
            if(temp!=check_list1[i] and temp!=check_list2[i]):
                f+=1
    if(flag==0 or f==0):
        print("yes")
    else:
        print("no")

#num=int(input(print("enter the numnber for checking")))
num=4343456
jumpingNumbers(num)
