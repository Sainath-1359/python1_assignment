it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Complete length of this is: ",len(it_companies))
it_companies.add('Twitter')#adding twitter to present items by add function
print("The full set is:",it_companies)
l = ('TCS', 'Accenture', 'wipro','Infosys')
it_companies.add(l)#adding multiple companies by taking a single variable by add function
print(it_companies)
it_companies.remove('Facebook')#to remove a company we use remove function
print(it_companies)

x = A.union(B)#to find union in two sets  i used this thing
print(x)
print(A.intersection(B))#to find intersection
print(A.issubset(B))#to check if it is subset or not
print(A.isdisjoint(B))#to check if it is a disjoint set
x = A.union(B)
print(x)
y = A.symmetric_difference(B)#to find the symmetric difference used this function
print("The symmetric difference between two sets is: ",y)
A.clear()#to remove the set I used the clear function
B.clear()
print(A)
print(B)
len_age = len(age)
age_set = set(age)
len_age_set = len(age_set)
diff_age = len_age - len_age_set
print(diff_age)
