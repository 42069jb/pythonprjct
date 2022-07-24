def saveIronman(s):
    s=s.upper()
    s=s.replace(" ","")
    print(s)
    rem_space = s.replace(" ", "")
    reversed= rem_space[::-1] #extended slicing [start:end:step_value]

    print(rem_space)
    if s==rem_space:
        k=True
    else:
        k=False
    return k







s="I am :IronnorI Ma, i"
p=saveIronman(s)
if p==True:
    print("yes")
else:
    print("no")