# while True:

#     password = input("please input your password here: ")

#     result = []

#     # for checking the length of password 

#     if len(password) >= 7:
#         result.append(True)
#     else:
#         result.append(False)

#     # for checking if there is any dighit is in the password or not:

#     digits = False
#     for i in password:
#         if i.isdigit():
#             digits = True

#     result.append(digits)

#     # for cheching if there exists a uppercase letter in the password

#     uppercase = False
#     for i in password:
#         if i.isupper():
#             uppercase = True

#     result.append(uppercase)  

#     if all(result):
#         print("strong password")
#     else:
#         print("No! This isn't a strong pass")    




password = input("please enter you passwprd: ")

def strength(password):
    result = {}
    if len(password) >=8:
        result["length"] = True
    else:
        reult["length"] = False
        
    digit = False
    uppercase = False
    
    for i in password:
        if i.isdigit():
            digit = True
            
        if i.isupper():
            uppercase = True
            
    result["digits"] = digit
    result["upper-case"] = uppercase
    
    if all(result.values()):
        return"Strong Password"
        
    else:
        return"Weak Password"
      

recommendation = (strength(password))
print(recommendation)

    
