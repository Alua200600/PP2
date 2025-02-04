#Task1
class Console:
    def __init__(word):
        word.text = ""
    def getstring(word):
        word.text = input()
    def printstring(word):
        print(word.text.upper())
obj = Console()
obj.getstring()
obj.printstring()

#Task2
class Shape:
    def area(self):
        print("area: 0")  
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print("area : ", self.length ** 2) 
shape = Shape()
shape.area()  
length = int(input("lenght of square: ")) 
square = Square(length)  
square.area()  

#Task3
class Shape:
    def area(self):
        print("area: 0")  
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  
        self.width = width    
    def area(self):
        print("area:", self.length * self.width)  
shape = Shape()
shape.area()  
length = int(input("length: "))
width = int(input("width: "))
rectangle = Rectangle(length, width)
rectangle.area()  

#Task4
import math
class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"pont1 : {self.x}, {self.y}")
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
        print(f"new point : {self.x}, {self.y}")
    def dist(self,other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance
point1 = Points(1,2)
point1.show()
point2 = Points(2,3)
point2.move(1,2)
print("dist : " +str(point1.dist(point2)))

#Task5
class account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,plus_money):
        self.balance+=plus_money
        print(f"balance : {self.balance}")
    def withdraw(self,minus_money):
        if minus_money>self.balance:
            print("You don't have enough money")
        else :
            self.balance-=minus_money
            print(f"balance : {self.balance}")
owner = input()
BankAccount = account(owner,0)
plus_money = int(input())
BankAccount.deposit(plus_money)
minus_money = int(input())
BankAccount.withdraw(minus_money)

#Task6
is_prime = lambda x: x>1 and all(x%i!=0 for i in range(2,x))
numbers = map(int,input().split())
prime_numbers = list(filter(is_prime,numbers))
print(prime_numbers)
