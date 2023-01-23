print("Enter the starting number")
a=int(input())
print("Enter the last number")
b=int(input())
for x in range(a,b):
    if x%3==0 and x%5!=0:
        print(x," hello")
    elif x%5==0 and x%3!=0:
        print(x," world")
    elif x%5==0 and x%3==0:
        print(x," Hellow world")

 