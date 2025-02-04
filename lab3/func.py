#Task1
g = int(input())
def func1(g):
    return g* 28.3495231
print("unc: "+str(func1(g)))


#Task2
f = int(input())
def temp(f):
    return (5/9)*(f-32)
print("C: "+str(temp(f)))


#Task3
heads = int(input())
legs = int(input())
def solve(heads,legs):
    rabbit = (legs-2*heads)//2
    chicken = heads - rabbit
    return "rabbits : " + str(rabbit) + "  chicken : " + str(chicken)
print(solve(heads,legs))


#Task4
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
arr = map(int,input().split())
arr1 = []
for i in arr:
    if prime(i):
        arr1.append(i)
print(arr1)


#Task5
s = input()
def permutation(s):
    from itertools import permutations
    perm = set(permutations(s))
    return perm
print(permutation(s))


#Task6
def reverse(a):
    b = ""  
    for i in range(len(a)-1, -1, -1):
        b += a[i]
    return b
a = input()
print(reverse(a))


#Task7
def has_33(arr):
    arr = list(arr)
    for i in range(len(arr)-1):
        if arr[i]==3 and arr[i+1]==3:
            return True
    return False
arr = map(int,input().split())
print(has_33(arr))


#Task8
def spy_game(arr):
    arr = list(arr)
    for i in range(len(arr)-1):
        if arr[i]==0 and arr[i+1]==0 and arr[i+2]==7:
            return True
    return False
arr = map(int,input().split())
print(spy_game(arr))


#Task9
import math
def v(r):
    return (4/3)*math.pi *(r**3)
r = int(input())
print(v(r))


#Task10
def u(arr):
    arr = sorted(arr)  
    arr1 = []  
    for i in range(len(arr)):  
        if i == 0 or arr[i] != arr[i - 1]:  
            arr1.append(arr[i])
    return arr1
arr = map(int, input().split())  
print(u(arr))


#Task11
def palindrome(s):
    if s==s[::-1]:
        return True
    return False
s = input()
print(palindrome(s))


#Task12
def histogram(arr):
    arr = list(arr) 
    for i in arr:  
        print("*" * i)  
arr = map(int, input().split())  
histogram(arr)  


#Task13
import random
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess")
def num(name):
    a = random.randint(1,20)
    attempts = 0 
    while True:
        g = int(input())  # Пользователь вводит число
        attempts += 1
        if a>g:
            print("Your guess is too low.")
        elif a<g:
            print("Your guess is too high.")
        else :
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
print(num(name))









    
    




