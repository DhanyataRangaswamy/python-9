class A:
    def __init__(self,a):
        self.a=a 
    def __lt__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob1 is greater than ob2"
        
    def __eq__(self,other):
        if(self.a==other.a):
            return "ob1 and ob2 are equal"
        else:
            return "not equal"
        
ob1=A(2)
ob2=A(4)
print("passed values:",ob1.a,ob2.a)
print(ob1<ob2)

ob3=A(3)
ob4=A(3)
print("Passed values:",ob3.a,ob4.a)
print(ob3==ob4)
