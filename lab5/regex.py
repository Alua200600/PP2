import re  
with open("r.txt") as f:
    data = f.read().strip() 

#Task1
matches = re.fullmatch(r"^ab*$", data)
print(matches) 

#Task2
strings = ["a","ab","abb","abbb","abbbb"]
for string in strings:
    if re.fullmatch(r"ab{2,3}", string):
        print(string,end=" ")

#Task3
strings = ["last_name","name_","name","student_of"]
for string in strings:
    if re.findall(r'\b[a-z]+_[a-z]+\b' ,string):
        print(string,end=" ")


# 4
text = input()
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)

# 5
text = input()
if re.fullmatch(r'a.*b', text):
    print("Yes")
else:
    print("No")

# 6
text = input()
modified_text = re.sub(r'[ ,.]', ':', text)
print(modified_text)

# 7
snake_case = input()
camel_case = ''.join(word.capitalize() for word in snake_case.split('_'))
print(camel_case)

# 8
text = input()
split_text = re.split(r'(?=[A-Z])', text)
print(split_text)

# 9
text = input()
modified_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print(modified_text)

# 10
camel_case = input()
snake_case = re.sub(r'([A-Z])', r'_\1', camel_case).lower().lstrip('_')
print(snake_case)

