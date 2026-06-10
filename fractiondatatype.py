class fraction():
    def __init__(self,a,b):
        if b == 0:
           raise ValueError("Denominator cannot be zero")
        self.num=a
        self.denum=b
    def __str__(self):
        if self.denum==1:
            return f"{self.num}"
        return f"{self.num}/{self.denum}"
    def __simplify(self,tempnum,tempdenum):
        common=1
        for a in range(2, min(abs(tempnum), abs(tempdenum)) + 1):
            if tempnum%a==0 and tempdenum%a==0:
                common = a
        return fraction(tempnum//common,tempdenum//common)

    # or {}/{}.format(self.num,self.denum)
    def __add__(self, other):
        tempnum=self.num*other.denum+self.denum*other.num
        tempdenum=self.denum*other.denum
        return self.__simplify(tempnum,tempdenum)
    def __sub__(self, other):
        tempnum = self.num * other.denum - self.denum * other.num
        tempdenum = self.denum * other.denum
        return self.__simplify(tempnum,tempdenum)
    def __mul__(self, other):
        tempnum=self.num*other.num
        tempdenum=self.denum*other.denum
        return self.__simplify(tempnum,tempdenum)
    def __truediv__(self, other):
        if other.num == 0:
           raise ZeroDivisionError("Cannot divide by zero fraction")
        tempnum=self.num * other.denum
        tempdenum= self.denum * other.num
        return self.__simplify(tempnum,tempdenum)
    def __eq__(self, other):
        return self.num * other.denum == self.denum * other.num
    def __lt__(self, other):
        return self.num * other.denum < self.denum * other.num
        # less than
    def __gt__(self, other):
        return self.num * other.denum > self.denum * other.num
    # greater than 
    def __neg__(self):
        return fraction(-self.num, self.denum)
    def __pow__(self,c):
        if c>0:
           tempnum= self.num**c
           tempdenum= self.denum**c
           return self.__simplify(tempnum,tempdenum)
        elif c==0:
            return fraction(1,1)
        else:
            tempnum= self.denum**(-c)
            tempdenum= self.num**(-c)
            return self.__simplify(tempnum,tempdenum)


        


    
x=fraction(6,6)
y=fraction(3,6)
print(x-y)
print(x+y)
print(x*y)
print(x/y)
print(y**2)
z = fraction(2,3)
print(z ** 2)     # 4/9
print(z ** 0)     # 1
print(z ** -1)    # 3/2
print(z ** -2)    # 9/4
print(-z)         # -2/3
print(z == fraction(4,6))  # True
print(z < fraction(3,4))   # True   
