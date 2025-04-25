names = input("Enter a name seperated by spaces : ")
names=names.split()

letter = [name[0].upper() for name in names]
print(letter)