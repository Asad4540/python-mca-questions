n = int(input("How many elements do you want to enter? "))
user_set= set()

print("enter each element one by one")
for _ in range(n):
    ch = input("enter element : ")
    if len(ch) == 1:
        user_set.add(ch)
    else:
        print("only single character is allowed")
        
print("user set is : ", user_set)

print("length of user set is ",len(user_set))

digitCount = 0 
lowerCount = 0
upperCount = 0

for ch in user_set:
    if ch.isdigit():
        digitCount +=1 
    elif ch.islower():
        lowerCount +=1
    elif ch.isupper():
        upperCount +=1
    
print("digit count is : ", digitCount)
print("lower count is : ", lowerCount)
print("upper count is : ", upperCount)