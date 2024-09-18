# ================ lab 1 ================

#principal amount
principal_amount = int(input(' Enter the principal amount:  '))

#rate of interest
rate_of_interest = int(input(' Enter the rate of interest '))

#time period
time_period = int(input(' Enter the time period: '))

#simple_interest calculations
simple_interest = ((principal_amount*rate_of_interest*time_period)/100)

#final calculations
print (f" the simple interest is: {simple_interest} ")



# ================ lab 2 ================

#weight number
weight = float(input(' enter your weight:  '))

#height number
height = float(input('enter your height:  '))

#calculations for the bmi

bmi = ((weight) / (height))
if((weight) / (height) < 50):
    print (' you are in the healthy range ')
else:
    ((weight) / (height) > 50 )
    print (' you are not in the healthy range ')

#final calculations
print (f" your BMI is: {bmi} ")

# ================ lab 3 ================

celsius = int(input(' enter the celsius tempature:   '))

# calculations

final_calculations = (((celsius)*9/5)+32)

#final stuff
print (f" the tempature converted to farenheit is: {final_calculations} ")

