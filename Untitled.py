#!/usr/bin/env python
# coding: utf-8

# # 1.Mailing Address

# In[8]:


name = "Rocky Bhai."
university = "Stanford university."
department = "Computer science."
mail = "abcd@gmail.com "
address = "Hyderabad."
pincode = 500085
country = 'India.'

print(f"My name is {name}")
print(f"My university is {university}")
print(f"My Department is {department}")
print(f"My email id {mail}")
print(f"MY address {address}")
print(f"My pincode is {pincode}")
print(f"My country is {country}")

print()

print("Ben Stephenson")
print("Dapartment of computer science")
print("University of calgary")
print("2500 university drive NW")
print("calgary,Alberta T2N")
print("canada")


# # 2.Hello

# In[13]:


name = input("Enter your name: ")
message = "Welcome to programming world!"

print(f"{name},{message}")
print("Hi {},{}".format(name,message))
print("Hi Rocky,Welcome.")


# # 3. Area of a Room

# In[15]:


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

def area_room():
    area = length * width
    print(area)
    
area_room()
    
print()

area = length * width

print("The area of the room is",area, "square feet")
    


# # 4. Area of a Field

# In[18]:


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

square_feet_acre = 43560

def area_field():
    acres = (length * width) / square_feet_acre
    print(acres)
    
area_field()

print()

acres = (length * width)/square_feet_acre

print("The area of field is",acres, "acre.")


# # 5. Bottle Deposits

# In[1]:


less_deposit = 0.10
more_deposit = 0.25

less = float(input("Containers you have less or 1 litre: "))
more = float(input("Containers have more than 1 litre: "))
refund = less * less_deposit + more * more_deposit

print("Your total refund will be %.2f." % refund)


# In[2]:


20*0.10


# In[4]:


40*0.25


# # 6. Tax and Tip

# In[7]:


tax = 0.05
tip = 0.18
cost_meal = float(input("Enter the cost of meal: "))
tax= cost_meal * tax
tip= tip * cost_meal

total = cost_meal + tax + tip

print("The tax is %.2f and the tip is %.2f, making the total %.2f" %(tax,tip,total))


# # 7. Sum of the first n positive integers.

# In[9]:


n = int(input("Enter a positive integer: "))
sum = n*(n+1)/2
print("The sum of first", n,"positive integers is",sum)


# # 8. Widgets and Gizmos

# In[22]:


print("The online retailer sells two products is widgets and gizmos.")

widget = int(input("Enter the weight of widget: "))
gizmos = int(input("Enter the weight of gizmos: "))

total_weight = widget + gizmos

print("The total weights of widget and gizmos is: " + str(total_weight) + " in grams.")


# # 9. Compound Interest

# In[48]:


principal_amount = int(input("Enter the amount: "))
rate = int(input("Enter the rate of intrest: "))
time = int(input("Enter time in years: "))


amount = principal_amount * (pow((1 + rate/100),time))
CI = amount - principal_amount
print("Compound intrest is: %.2f" % round(CI,2))
end_of_the_year = principal_amount + CI
print("The total amount is end of the year: ", str(end_of_the_year))


amount_1 = principal_amount * (pow((1 + rate/100),2))
C = amount_1 - principal_amount
print("Compound intrest second year is : %.2f"% round(C,2))
second_year = principal_amount + C
print("The total amount at second year: ",str(second_year))


amount_2 = principal_amount * (pow((1 + rate/100),3))
Compound = amount_2 - principal_amount

print("Compound intrest third year is : %.2f"% round(Compound,2))

third_year = principal_amount + Compound
print("The total amount at third year: ",str(third_year))


# # 10. Arithmetic

# In[51]:


from math import log10

a =  int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(a,"+", b, "is", a+b)
print(a,"-", b, "is", a-b)
print(a,"*", b, "is", a*b)
print(a,"/", b, "is", a/b)
print(a,"%", b, "is", a%b)

print("The base 10 logarithm of", a, "is", log10(a))
print(a,"^", b, "is", a**b)


# # 11. Fuel Efficiency

# In[52]:


def convert_mileage(m):
    return (236.5 / m )

if __name__ == '__main__' :
    print ("20 MPG = ",convert_mileage(20)," Liters per 100 kilometers") 


# In[53]:


def convert_mileage2(m):
    return ((3.78/((m*1.6)/100)))

if __name__ == '__main__' :
    print ("20 MPG = ",convert_mileage2(20)," Liters per 100 kilometers") 


# In[5]:


def convert_mileage(miles_per_gallon):
    km_per_gallon = float(input("Enter the gallons: "))  # 3.78544784
    km_per_mile = float(input("Enter the mile: "))  # 1.609344
    liters_per_100 = (100* km_per_gallon)/(km_per_gallon * miles_per_gallon)
    
    print(miles_per_gallon,'miles per gallon are',liters_per_100,'liters per 100 kilometers.')
    
    
convert_mileage(40)


# # 12. Distance between TWO points on earth.

# In[8]:


from math import acos ,sin,cos,radians

print("Input coordinates of the two points.")

t1 = radians(float(input("Enter the latitude value: ")))
g1 = radians(float(input("Enter the longitude value: ")))
t2 = radians(float(input("Enter the latitude value: ")))
g2 = radians(float(input("Enter the logitude value: ")))

distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))

print("The distance is %.2fkm." % distance)


# # 13. Making Change

# In[17]:


cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter =25
cents_per_dimes = 10
cents_per_nickel = 5

cents = int(input("Enter the user cents: "))

print(" ",cents//cents_per_toonie,"toonies")
cents = cents % cents_per_toonie

print(" ",cents//cents_per_loonie,"loonies")
cents = cents % cents_per_loonie

print(" ",cents//cents_per_quarter,"quarter")
cents = cents % cents_per_quarter

print(" ",cents//cents_per_dimes,"dime")
cents = cents % cents_per_dimes

print(" ",cents//cents_per_nickel,"nickel")
cents = cents% cents_per_nickel

print(" ",cents, "pennies")


# In[14]:


400 % 200


# In[20]:


800 // 100


# # 14. Height units

# In[22]:


in_per_feet =12
cm_per_in = 2.54

# print("Enter your height: ")
feet = int(input("Enter your feet: "))
inch = int(input("Enter number of inches: "))
cm = (feet * in_per_feet +inch)*cm_per_in
print("your height in cm: ", cm)


# # 15. Distance units

# In[27]:


feet = int(input("Enter your feet : "))
d_inches = feet * 12
d_yards = feet/3.0
d_miles = feet/5280
print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)


# # 16.Area and Volume

# In[34]:


r = int(input("Enter the radius: "))
pi = 3.142


are_of_circle = pi * r * r
print("The area of the circle is: ",are_of_circle)
volume_of_sphere = 4/3 *pi*r*r*r
print("The area of the volume_of_sphere is :",volume_of_sphere)


# # 17. Volume of a Cylinder

# In[1]:


# pi * r*r*h

pi = 3.142

r = float(input("Enter the radius of cylinder: "))
h = float(input("Enter the heigh of cylinder: "))

volume_of_cylinder =  pi * r * r * h
print("The volume of the cylinder is: ",volume_of_cylinder)


# # 18. Free Fall

# In[3]:


from math import sqrt

gravity = 9.8

d = float(input("Enter the which the object id dropped(in meters): "))

vf = sqrt(2 * gravity * d)

print("It will hit the ground at : ",vf)


# # 19. Area of a Triangle

# In[11]:


base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triagle: "))
area = 0.5*(base * height)
print("The area of the triangle is : ",float(area))


# # 20. Area of a Triangle(Again)

# In[15]:


s1 = float(input("Enter the first side of Triangle: "))
s2 = float(input("Enter the second side of triangle: "))
s3 = float(input("Enter the third side of triangle: "))

# calculating the semi perimeter.
s = (s1 + s2 + s3)/2

area = (s * (s-s1)*(s-s2)*(s-s3))** 0.5
print("Area of the triangle: ",area)


# # 21. Area of a Regular polygon

# In[17]:


from math import tan, pi

s = float(input("Enter the length of the each side of ploygon: "))
n = float(input("Enter the number of sides: "))

area = (n * s ** 2)/(4 * tan(pi/n))
print("The area of the polygon is : ",area)


# # 22. Units of Time

# In[18]:


days = int(input("input days: "))* 3600 *24
hours = int(input("input hours: ")) * 3600
minutes = int(input("input minutes: "))* 60
seconds = int(input("input seconds: "))

duration = days + hours + minutes + seconds 
print("The amount of seconds : ", duration)


# # 23.Units of Time(again)

# In[21]:


7/5


# In[25]:


100 % 86400
100/86400


# In[32]:


seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60
seconds = int(input("Enter the number of seconds: "))

days = seconds / 86400
seconds = seconds%86400

hours = seconds/ 3600
seconds = seconds % 3600

minutes = seconds/ 60
seconds = seconds % 60


print("The equalent duration is: ",(days,hours,minutes,seconds))


# # 24.Current Time

# In[34]:


from datetime import datetime

now= datetime.now()

print(now)
current_date = now.strftime("%H:%M:%S")
print(current_date)


# In[35]:


import time

time_astr = time.asctime()
print(time_astr)


# # 25. Body Mass Index

# In[37]:


weight = int(input("Enter the weight in kg is : "))
height = int(input("Enter the height in meters is : "))

BMI = weight/height ** 2
print("The BMI is: ",BMI)


# # 26.Wind Chill

# In[40]:


# wc = 13.12 + 0.621T - 11.37 V^0.16 + 0.3965 T (V^0.16)


temp = float(input("Enter the temparature in degrees (celsius): "))
speed = float(input("Enter the speed in kilometers per hour : "))

wind_chill = 13.12
wind_chill_1 = 0.621
wind_chill_2 = -11.37
wind_chill_3 = 0.3965 
wind_chill_exponent = 0.16

wci = wind_chill + wind_chill_1 * temp + wind_chill_2 * speed **wind_chill_exponent +         wind_chill_3 * temp * speed** wind_chill_exponent

print("The wind chill index is", round(wci))


# # 27.Celsius to Fahrenheit and Kelvin

# In[43]:


temp = float(input("Enter temparature in degrees: "))
# celsius to fahrenheit f= (c * 9/5)+32
#fahrenheit to celsius c=(f-32)*5/9
# celsius to kelvin k=c+273.15
# kelvin to celsius c=k-273.15

f = (temp * 1.8) +32
print("celsius to fahrenheit is: ",f)

c = (temp-32)*1.8
print("fahrenheit to celsius is: ",c)

k = temp + 273.15
print("celsius to kelvin: ", k)

c1 = k-273.15
print("Kelvin to celsius is: ", c1)


# # 28.Units of pressure

# In[46]:


pressure = float(input("Enter the pressure(in kilopascals): "))
pressure_in_pounds_per_square_inch = pressure/6.895
pressure_in_millimeters_of_mercury = pressure * 7.501
pressure_in_atmosphere = pressure/101.325

print("Pressure in pounds per square inch:", pressure_in_pounds_per_square_inch)
print("Pressure in millimeters of mercury:", pressure_in_millimeters_of_mercury)
print("Pressure in atmospheres:", pressure_in_atmosphere)


# # 29.Sum of the Digits in an integer

# In[5]:


num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)


# # 30. Sort 3 Integers

# In[14]:


a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

mn = min(a,b,c)
mx = max(a,b,c)
mid = a + b + c -mn - mx

print("The numbers are sorted order: ")
print(" ",mn)
print(" ",mid)
print(" ",mx)


# # 31. Day Old Bread

# In[15]:


cost_bread = 3.49
discount_rate = 0.60

num_loaves = int(input("Enter no of loaves: "))

regular_price = num_loaves * cost_bread

discount = discount_rate * regular_price

total = regular_price - discount


print("Regular_price: %.2f" % regular_price)
print("Discount: %.2f" % discount)
print("Total: %.2f" % total)


# In[ ]:




