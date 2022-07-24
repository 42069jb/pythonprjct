def singleNumber(nums):
    first_list=nums
    second_list=[]
    repetition_list=[]
    for item in first_list:
        if item not in second_list:
            second_list.append(item)
    print("single list= ",second_list)
    for item in second_list:
        repetition=first_list.count(item)
        repetition_list.append(repetition)
    print("repeating list=",repetition_list)
    minimum=min(repetition_list)
    print("minimum repeating value=",minimum)
    main_list=[]
    for i in range(0,2):

        k=repetition_list.index(minimum)
        main_list.append(second_list[k+i])
        repetition_list.remove(minimum)
    print(main_list,"is the once occuring values")


numbers=[1,2,3,2,1,4]
print("first list= ",numbers)
singleNumber(numbers)