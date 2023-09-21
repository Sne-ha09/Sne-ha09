number_1 = int(input("Type the first number."))
number_2 = int(input("Type the second number."))
operation = input ("Type 'a' for addtion, 's' for subtraction, 'd' for division, 'e' for exponential multiplication  ")





if operation  == 'a' : 
     print (f"Your answer is", {number_1 + number_2})
    
elif operation  == 's' :
     print (f"Your answer is", {number_1 - number_2})
    
elif operation  == 'd' :
    print(f"Your answer is ", {number_1 / number_2})  
     
elif operation  == 'e' :
    print(f" Your answer is " ,{number_1**number_2}) 


