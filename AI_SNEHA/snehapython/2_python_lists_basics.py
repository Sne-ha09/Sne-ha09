#list_basics (by sir)

#list is a datatype/ data structre which stores multiple information in a sequence separated by commas
#enclosed in []
#empty list is []
#names= list() or name=[]
name=["Sneha","Gitan","Aniska","Suja"]
print(len(name)) #----- for length
#indexing -  to get the address of element of the list
print(name[2]) #- to find the third element of the list
print(name[3][2]) #- to find the 2nd letter of the 3rd element (**can be used only for strings**)

#can be used to create matrices
#list of lists
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
#double indexing taking matrices as an example
print(matrix[2][1]) #ith row and jth column
#for square matrix
#condition
if len(matrix)== len(matrix[0]):
     print ("It is a square matrix")
else:
     print("It is not a square matrix")     

#negative indexing - print(name[-1]) ---- for element's address from backward

# slicing a list ---- (start:end) [end isn't included]
# #middle= ages[2:5] ---- for element 2,3 & 4
#print(middle) 
#first_four = ages[:3] ---- for elements from the beginning to 3rd element
#print(first_four)
#last_four = ages[3:] ---- for 4th element to the last element
#negative addressing 
#negative= ages[-2:-5] ---- for elements from -3 to -5
#membership opertor -> using word 'in'
print('Suja' in name) #---- will show true if its there & false if its not in the list

your_name= input("enter your name")
if your_name in name:
      print('She is an AI student')
else:
      print('The student has not opt for AI')     
#OR
your_name= input("enter your name")
if your_name not in name:
       print('The student has not opt for AI')     
else:
       print('She is an AI student')

#iterating over a list using 'for' loop
#for elements in ages: ---- elements is just a name given to 
      #print (elements)



#add elements in a list at the last
# age.append(50)      
# print ( ages)

#del(age[2])
#print(ages)

#ages.pop() ---- removes last element
#print(ages)

#add in between
#ages[2]=20
#print(ages)

#to add without deleting
#ages.insert(2,12) --- first agrument= where you want to insert & second = what you want to insert
     
#LISTS
# [] is for lists
# [:] id for range in lists
#example of list 
fam=["sneha","aniska","gitan","suja","ivan sir","atl"] #any type can be included
print(fam)
print(fam[2])
print(fam[-2])
#- means counting from backwards
#example of list of lists
fam2= [["sneha","gitan","ivan sir"],["suja","aniska","atl"]]
# use commas between lists and between the elements within lists
# index (location of elements) starts with 0
print(fam[1:3]) #the starting element is included whereas the last element is excluded
print(fam[:3]) #elements from 0 to 3 are included
print(fam[3:]) #every element after the 3rd element


#LISTS MANIPULATION 
#changing elements in lists
fam[5]="ATL Lab"
fam
print(fam)
#changing several elements together
fam[0:3] = [] #add the corrected values inside [""] with , in between elements
fam 
print(fam)
#adding elements to lists
fam+["Python","Java",1995]
fam
print(fam)
#deleting elements from lists
del(fam[2])
fam
print(fam)
#copying elements from lists
x=["a","b","c"]
y=x
print(y) #changing the lists name from x to y
#and
u=["s","n","e"]
v=list(u)
#or
v=u[:]
print(u)
print(v) #u and v are different lists with same elements


