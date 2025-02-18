#Task1
def square(n):
    for i in range(n + 1):
        yield i**2
n = int(input())
print(",".join(map(str, square(n))))


#Task2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i  
n = int(input())
print(",".join(map(str, even_numbers(n))))

#Task3
def d(n):
    for i in range(n + 1):
        if i%3==0 and i%4==0:
            yield i
n = int(input())
print(",".join(map(str, d(n))))


#Task4
def square1(a,b):
    for i in range(a,b+1):
        yield i**2
a = int(input())
b = int(input())
print(",".join(map(str, square1(a,b))))

#Task5
def nums(m):
    for i in range(m,-1,-1):
        yield i
m = int(input())
print(",".join(map(str, nums(m))))




