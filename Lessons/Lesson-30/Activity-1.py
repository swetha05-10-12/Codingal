class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return "Object 1 is less than Object 2"       
        else:
            return "Object 2 is less than Object 1" 
        
    def __eq__(self, other):
        if (self.a==other.a):
            return "Object 3 is equal to Object 4"
        else:
            return "Object 3 is not equal to Object 4"
        

ob1=A(2)
ob2=A(3)
print("Passed Values:",ob1,ob2)
print("Obj1<Obj2")

ob3=A(4)
ob4=A(4)
print("Passed Values:",ob3,ob4)
print("Ob3==Obj4")
