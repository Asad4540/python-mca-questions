# string = input("enter a string")
# print(string[::-1])

def stringRev():
    userInput = input("enter a string : ")
    words = userInput.split()
    revWords = [word[::-1] for word in words]
    result=' '.join(revWords)
    return result

str = stringRev()
print("Output : ",str)
    
    
    
    


