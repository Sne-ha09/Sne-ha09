students = ["Sneha",
         "Aniska",
         "Suja",
         "Gitanjali",
         "Pema", 
         "Rangeeta", 
         "Hrishu" ,
         "Diya",
         "Karma",
         "Anusha",]
score = []
# a = int((input("Enter marks for Sneha")))
# b = int((input("Enter marks for Aniska")))
# c = int((input("Enter marks for Suja")))
# d = int((input("Enter marks for Gitanjali")))
# e = int((input("Enter marks for Pema")))
# f = int((input("Enter marks for Rangeeta")))
# g = int((input("Enter marks for Hrishu")))
# h = int((input("Enter marks for Diya")))
# i = int((input("Enter marks for Karma")))
# j= int((input("Enter marks for Anusha")))

for name in students :
    print ("Enter marks for" , name)
    scores = input()
    score.append(score)
#marks = [a ,b,c,d,e,f,g,h,i,j]

# grades = [[students[0],marks[0]],
#           [students[1],marks[1]],
#           [students[2],marks[2]],
#           [students[3],marks[3]],
#           [students[4],marks[4]],
#           [students[5],marks[5]],
#           [students[6],marks[6]],
#           [students[-3],marks[7]],
#           [students[8],marks[8]],
#           [students[9],marks[9]]]
# print (grades)

for i in range (9):
    print (students[i], score [i])

# print (f"The highest marks is" , {max(marks)})

# z = a + b + c + d + e +f +g + h + i + j
# print (f"The average marks is" , { z / 10})



