def swap(num):
    result = " "
    
    i=0
    while i<len(num)-1:
        result += num[i+1]+num[i]
        i += 2
        
    if len(num) % 2 != 0:
            result += num[-1]
    
    return result


num = input("enter a string : ")
swapped = swap(num)
print(swapped)
