#generatin random numbers
'''import random
   for i in range(0,5):
    print(random.randint(1,100))'''


#printing random from a list
'''import random
ls=["arun","nivin","sreerag","akshay","achu","chembu"]
print(random.choice(ls))'''

import random
class Dice:
    def __init__(self,ls):
        self.lis=ls
    def roll(self):
        print(random.choice(self.lis))


ls=["(1,1)","(1,2)","(1,3)","(1,4)","(2,1)","(2,2)","(2,3)","(3,5)","(5,2)"]
d=Dice(ls)
d.roll()