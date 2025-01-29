a=int(input("enter thenumber a:"))
b=int(input("enter the number b:"))
if(a%4==0 & a%100==0|b%4==0 & b%100==0):
    print("leap year")
else:
    print("not a leap year")
