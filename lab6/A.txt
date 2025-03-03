#Task1
import math
nums = list(map(int,input().split()))
res = math.prod(nums)
print(res)

#Task2
def count_letters(s):
    upper_count = sum(1 for char in s if char.isupper())  
    lower_count = sum(1 for char in s if char.islower())  
    return upper_count, lower_count
text = input()
upper, lower = count_letters(text)
print("upper :", upper)
print("lower :", lower)

#Task3
def palindrom(text):
    text1 = text[::-1]
    if text==text1:
        return True
    else:
        return False
text = input()
print(palindrom(text))

#Task4
import time
num = int(input())
mseconds = int(input())
time.sleep(mseconds / 1000) 
k = math.sqrt(num)
print(f"Square root of {num} after {mseconds} miliseconds is {k}")

#Task5
my_tuple = (True, 1, "hello", 3.14)  
result = all(my_tuple)
print(result)
