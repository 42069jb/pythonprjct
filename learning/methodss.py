import math
weight=input("enter the wight")
ch=input("(K)for kg (P)for pounds")
if ch.upper()=='K':
    weigh=int(weight)/0.45
    print(f"your weight {(weight)}kg  {(weigh)}lbs")
elif ch.upper()=='P':
    weigh=int(weight)*0.45
    print(f"your weight {weight}kg  {weigh}lbs")
else:
    print("wrong command")

