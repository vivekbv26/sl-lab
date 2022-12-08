class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def getdata(self):
        print("enter the details \n  enter the name")
        self.name= str(input())
        print("enter the age")
        self.age = int(input())
        print("enter the marks in 3 subjects")
        for i in range (0,3):
            self.marks.append(int(input()))
            
    def display(self):
        print("name=\n",self.name,"age is \n",self.age)
        print("marks in 3 sub is ",self.marks)

s= student("",0,[])
s.getdata()
s.display()



        