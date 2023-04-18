actual_pwd="1234"
entered_pwd=""
count = 0
while True:
    entered_pwd=input("Please enter the password :)   ")
    if entered_pwd == actual_pwd :
       print("You're logged in :D Enjoy") 
       break
    else:
        count+=1
        print(f"That's not the correct password :( You have {4-count} more attempts left ") 
        if 4-count == 0 :
           print("Oops! Already too many incorrect attempts, your account has been blocked for 24 hours")
           break 

