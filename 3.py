
class rectangle:               #defining a class
    def __init__(self,l,w):    #initialising constructor
        self.length = l
        self.width = w

    def area(self):             #area function
        return self.length*self.width

n = int(input("enter the side"))
m = int(input("ente"))
newrectangle = rectangle(n,m) #creating object of class
print("The area of rectangle is:")
print(newrectangle.area())      #calling area function