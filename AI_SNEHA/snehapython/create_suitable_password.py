print ("Please create a strong password using both alphabets and numbers. Make sure your password contains atleast 8 characters.")
password =input("Type your password here.")
print(f"You entered your password as {password}.")

while True: 
     if (len(password)<8)  :
          print ("Insufficient length. Please make sure to have atleast 8 characters in your password.")
          password =input("Type your password here.")
     elif (password .isalpha()) or (password .isnumeric()) :
         print("Please add both alphabets and numbers in your password.")
         password =input("Type your password here.")
     else :
       print("You can proceed.")
       break
    
 
