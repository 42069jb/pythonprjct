class Person:
    def __init__(self,nam):
        self.name=nam
    def talk(self):
        print(self.name+" is talking")



p=Person("arun")
p.talk()
l=Person("nivin")
l.talk()