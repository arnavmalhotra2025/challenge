#activity 1
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x/ y
print("Value of (v+w) * x/ y is ", z)

name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello welcome")
else:
    print("goodbye")

#activity 2
print("enter a number (Numerator):")
numn = int(input())
print("enter a number (denominator):")
numd = int(input())

if numn % numd == 0:
    print("\n" +str(numn)+" is divisible by "+str(numd))
else:
    print("\n" +str(numn)+" is not divisible by "+str(numd))

#activity 3
mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40
#sum of 40 numbers
sum = mean1*total_number
print("the sum of 40 number:",sum)

#correct sum of these numbers
sum2 = sum- wrong_number + correct_number
print("sum-((wrong_number) - (correct_number)):" , sum2)

#the correct mean
mean2 = sum2/total_number
print(mean2)

#activity 4

a = int(input("enter a value :"))
b = int(input("enter a value 2 :"))
c = int(input("enter a value 3:"))

avg = (a+b+c)/3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg,a,b,c))
elif avg > a and avg > b:
    print("avrage is greater than a and b")
elif avg > a and avg > c:
    print("avrage is greater than a and c")
elif avg > b and avg> c:
    print("avrage is greater than band c")
elif avg > a:
    print("avrage is greater than a ")
elif avg > b:
    print("avrage is greater than b")
elif avg >c:
    print("avrage is greater than c")
else:
    print("invalid input")
    
    

    