class op():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
c1=op("raja",21)
c2=op("raju",90)
c3=op("rajo",98)
l=[c1,c2,c3]

for i in l:
    print(i.name,i.age)

       