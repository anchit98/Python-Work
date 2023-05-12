#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

name = input("Enter your name: ")

weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in m: "))

BMI = (weight) / (height**2)

print(BMI)

if BMI > 0:
    if(BMI<18.5):
        print(name +", You are underweight")
    elif(BMI<=25):
        print(name +", You are normal weight")
    elif(BMI<30):
        print(name +", You are overweight")
    elif(BMI<35):
        print(name +", You are obese")
    elif(BMI<40):
        print(name +", You are severely obese")
    else:
        print("Your are morbidly obese")
else:
    print("Enter valid input")
