def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Basic Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
choice=int(input("Enter your choice:"))
if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
else:
    print("Enter a valid choice.")