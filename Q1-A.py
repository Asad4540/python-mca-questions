my_dict ={
    "name":"asad",
    "age":23,
    "city":"pune",
    "country":"india"
}

#Display all the dictionary
print(my_dict)

print("---------------------------------")
#Display the value of key "name"
print(my_dict.keys())

print("--------------------------------")
#Display the value of key "age"
print(my_dict.values())

print("--------------------------------")
#Adding a new key-value pair to the dictionary
my_dict["is_student"]="true"
print(my_dict)

print("--------------------------------")
#delete the key-value pair with key 
del my_dict["age"]
print(my_dict)

print("--------------------------------")
#modify a key value pair in the dictionary
my_dict["name"]="Asad Chaudhary"
print(my_dict)



