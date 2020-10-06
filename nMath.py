#!/usr/bin/env python

'This module introduces a number of mathematical functions'

#Sorry, this might recreate functions from the math module, I never went through the documentation

from math import pi
from random import randint

from nType import xdict

def calcGrade(percentageGrade):
    'Takes a percentage grade and converts it to letter; returns result'
    
    #percentageGrade defines grade to be converted
    
    percent = float(percentageGrade)
    grade = None
    
    if percent < 60:
        grade = 'F'
    elif percent < 70:
        grade = 'D'
    elif percent < 80:
        grade = 'C'
    elif percent < 90:
        grade = 'B'
    else:
        grade = 'A'

    return(grade)

def centDiv(cents):
    'Divides a number of cents into as little U.S. coins as possible'

    numCents = int(cents)
    
    if numCents >= 100:
        raise ValueError('centDiv() expected cents to be < 100; got %s' % (cents))
    else:
        #calculates quarters
        quarters = str(numCents // 25)
        remainder = numCents % 25

        #calculates dimes
        dimes = str(remainder // 10)
        remainder %= 10

        #calculates nickels
        nickels = str(remainder // 5)
        remainder %= 5

        #calculates pennies
        pennies = str(remainder)
        remainder = 0 #for consistency
        
        print(quarters + " quarters, " + dimes + " dimes, " + nickels + " nickels, and " + pennies + " pennies.")
        
#These are from excersises learning Python        
def circleArea(radius):
    area = math.pi * (radius**2)
    return(area)

def isdivisible(dividend, divisor, /): #get rid of / parameter if your Python version is earlier than 3.8
    'finds if dividend is divisible by divisor'
    if dividend % divisor == 0:
        return(True)
    else:
        return(False)

def f2c(farenheit):
    'converts farenheit to celsius'
    celsius = (farenheit - 32) * (5/9)
    return celsius
    
def c2f(celsius):
    'converts celsius to farenheit'
    farenheit = (celsius / (5/9)) + 32
    return farenheit

def minToHours(minutes):
    'converts minutes to hours and minutes'
    return xdict(('hours', 'minutes'), divmod(minutes, 60))
