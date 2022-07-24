def consecuive_zeros(string1):
    list1=string1.split("1")
    largest=0
    k=max(list1)
    print(len(k))
    for item in list1:
        length=len(item)
        if length>largest:
            largest=length
    print(largest)

consecuive_zeros("1001101000110")