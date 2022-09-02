ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()#to arrange in an ascending order
print(ages)
print("Minimum =",min(ages))#here min is a direct function to find min value
print("Maximum =",max(ages))#here max is a direct function to find max value
ages.append(min(ages))#to add min value to ages I used append
ages.append(max(ages)) #to add max value to ages I used append
ages.sort()
print(ages)
n=len(ages)#to find length of ages I used length
if n % 2 == 0: #the if statement used to check the remainder is zero or not
    median1 = ages[n//2]
    median2 = ages[n//2 - 1]
    median = (median1+ median2)/2#to find median we divide and add 2 medians
print("median =",median)
def Average(ages):#defining a function to find average
    return sum(ages)/len(ages)#calling a function and finding average
average=Average(ages)
print("Average of the list=", round(average , 2))#round function used to get an exact value without
                                                     #decimals
print(max(ages)-min(ages))
