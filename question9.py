conversionrate = 0.45 #the value obtained when we want to convert lbs to kg
x = int(input('Enter the number of students'))# the input function used to enter the value by user
List=[]
for i in range(x):#for loop used to excute this List
    List.append(int(input('Enter the weight in lbs:')))#append function used to add something

y = [conversionrate*i for i in List]
print("The list in Kilogram is:",y)
