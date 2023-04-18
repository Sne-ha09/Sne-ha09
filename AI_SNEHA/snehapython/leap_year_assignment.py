print("Please enter the year to know if it's a leap year or not")
year= int(input("Enter the year here  "))
while True:
     if year%4!=0 :
          print("It is a common year.")
          break
     else :
          print("It is a leap year.")     
          break