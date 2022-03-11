import sys
# getting the user's weight
weight = input("Enter weight in pounds: ")
weight = int(weight)
# getting the user's Height
height = input("Enter your height in inches: ")
height = int(height)
# Metric conversions
weight = weight * .45
height = height * .025
# Calculating BMI
height = height * height
BMI = weight / height
if(BMI < 18.5):
    print("Your BMI is: ", BMI, " you are Underweight.")
elif(18.5 <= BMI <= 24.9):
    print("Your BMI is: ", BMI, " you are Normal weight.")
elif(25 <= BMI <= 29.9):
    print("Your BMI is: ", BMI, " you are Overweight.")
else:
    print("Your BMI is: ", BMI, " you are Obese.")




