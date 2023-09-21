#popular loops for-loop and while-loop

# while loop = when we are not sure of th number of times the loop iterates(keep on acceptin no. from the user until he presses the valid outcome)
# for loop = we nkow '   '   (accept 10 times from user)                 


for n in range(5):
    input(f"type something for {n+1} time")


sum =0   
for n in range(10):
    number = (input(f"enter the number:"))
    sum = sum + int(number)

ch= input("do you want to print the sum")    
if ch=="y":
      print(sum)
else:
  print("OKAY") 

