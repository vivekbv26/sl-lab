list1 = []
list2 = []

def c_to_f(cel):
    cel_con= float((cel*9/5)+32)
    print("temp in farenheight is",cel_con)
    tup=(cel,cel_con)
    list1.append(tup)

def f_to_c(far):
    far_con = float((far-32)*5/9)
    print("temp in celsius=",far_con)
    tup=(far,far_con)
    list2.append(tup)

while(1):
    print("1.c to f \n 2. f to c \n 3.exit \n 4.display \n 5.display2 \n enter yout choice")
    choice = int(input())
    if(choice == 1):
        print("enter the temp in celcius")
        cel= int(input())
        c_to_f(cel)
    elif(choice==2):
        print("enter the temp in fareheight:")
        far = float(input())
        f_to_c(far)
        
    elif(choice ==3):
        SystemExit.exit()

    elif(choice==4):
        print(list1)
    elif(choice ==5):
        print(list2)


