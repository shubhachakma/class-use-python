class Max3Num:
    def __init__(self,a,b,c):
        if a>b and a>c:
            print("A is maximum",a)
        elif b>c:
            print("B is maximum",b)
        else:
            print("C is maximum", c)

#a = int(input("A="))
#b = int(input("B="))
#c = int(input("C="))
#max3Num = Max3Num(a, b, c)



import math
class Trianglearea:
    def __init__(self, a, b, c):
        import math
        if (a+b)>c and (b+c)>a and (a+c)>b:
            s=(a+b+c)/2
            area=math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Triangle Area",area)
        else:
            print("Triangle is not possible")
a = float(input("Enter first Arm="))
b = float(input("Enter second Arm="))
c = float(input("Enter third Arm="))
tarea = Trianglearea(a,b,c)


#Enter first Arm=4
#Enter first Arm=3
#Enter first Arm=2