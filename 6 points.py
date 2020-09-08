x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

x=int(input())
y=int(input())

a=y*(x2-x1)-y1*(x2-x1)-x*(y2-y1)+x1*(y2-y1)
if a>0:
    print("Up")
if a<0:
    print("High")
    
