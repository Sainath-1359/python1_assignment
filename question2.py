dog = {} # created an empty dictionary
dog['name'] = 'goli'#the keys and values are shown here
dog['color']= 'black'
dog['breed'] = 'german shephard'
dog['legs'] = 4
dog['age'] = 5
print(dog)


#creating a student dictionary and having keys and values in it
student={'first_name':'Sainath Reddy', 'last_name':'Kollu','gender':'Male','age':22,'Marital Status':'Single','Skills':'oops','Country':'India','City':'Overland park','Address':'hunters pointe'}

print(student)

print(len(student))

x= list(student)
print(student.get('skills'),type(x))#to get the value of skills and to find the data type


student['skills'] = 'C'#modifing the skills to have add other skills
print(student)

print(list(student.keys()))#to get the list of only keys

print(list(student.values()))#to get the list of only value
