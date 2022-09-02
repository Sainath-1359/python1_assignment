
brotherstuple =("abhishek","varun","sai")#created a tuple for brothers
sistersstuple =("mounika","amulya","pranathi")#created a tuple for sisters
sibilingsstuple = brotherstuple + sistersstuple#to have both brothers and sisters tuple in single cell
print(sibilingsstuple)
print("The length of Sibilingsstuple is: ",len(sibilingsstuple))#length used to calculate combined tuple

parents = ('Srinivas','Aruna')
familytuple = sibilingsstuple + parents#adding parents to siblings to have a family tuple
print(familytuple)
