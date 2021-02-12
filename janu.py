def task():
    a=int(input("enter the a value"))
    b=int(input("enter the b value"))
    c=int(input("enter the value"))
    if("a==b==c"):
       print("zero")

    elif(a==b and b!=c):
       print(c)
    elif(b==c and c!=a):
       print(a)
    elif(a==c and c!=b):
       print(b)
    else:
       print(a+b+c)
task()


            
            
