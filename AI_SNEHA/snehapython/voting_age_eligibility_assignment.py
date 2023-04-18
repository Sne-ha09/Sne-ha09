age=99
age =int (input ("Enter your age."))
while age>3:
    print(f"You entered your age as {age}.")
    
    if age>17 and age<60: #if age>=18 #if int(age)>17
       print("You're eligible to cast your vote.")

    elif age>59:
      print("You're eligible to cast your vote and will be provided with refreshments too")

    else:
      print(f"Sorry, you can come after {18-age} years.")
    break 
print("Exited the program.")
    

