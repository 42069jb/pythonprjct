def add_dots(string):
    length=len(string)
    i=0
    string1=""
    for i in range(length):
        if(i%2==0):
            string1 += string[i]
            string1 += "."
        else:
            string1 += string[i]
            string1 += "."
    l=list(string1)
    l1=list(string)
    length=len(string1)
    del (l[length-1])
    string1 = "".join(l)
    print(string1)

s=add_dots("abcd")

