password =input("Password: " )
num1 = num2 = num3 = num4 = num5 = 0  
for x in password:
      if x.isspace():
        num5 += 1
      if x.isupper():
       num1 += 1
      if x.islower():
       num2 += 1
      if not x.isalnum() and not x.isspace():
        num3 += 1
      if x.isdigit():
        num4 += 1
if num5 != 0 or len(password) < 8:
  print("INVALID Password can't have spaces or more than 8 characters")
else:
 if num1 != 0 and num2 != 0 and num3 != 0 and num4 != 0 :
  print("strong")
 elif num1*num2*num3 !=0 or num2*num3*num4 != 0 or num3*num4*num1 != 0 or num1*num3*num4!= 0 or num1*num2*num4!= 0:
  print("good")
 else:
  print("weak")
       
        
