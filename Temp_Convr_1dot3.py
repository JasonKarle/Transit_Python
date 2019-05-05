#!/usr/bin/python
"""

Program: Temperature Conversion (C to F, or F to C)
Date:    05 May 2019
Version: 1.2
Author:  Jason P. Karle

Remark:  This program was inspired by a Python exercise that
asks you to create a program that will convert one Celsius value to Fahrenheit;
so a program that can be executed with three lines of code.

However, I wanted to make something that would allow the user to
convert to and from either C of F, and do so multiple times, until the user
decides to end the program. This was also an exercise for me to
advance not only my code skills, but how I structure a program.

version history:
    1.0 Initial draft
    1.1 Correction of runtime; posted to StackExchange for feedback
    1.2 Re-coded based on feedback; trying to improve flow control
"""


def read_selection():
    selection = input('''Welcome to the temperature conversion program!

Please make a selection:

    c to convert from Celcius to Fahrenheit;
    f to convert from Fahrenheit to Celsius; or
    q to quit the program.
    
Enter your selection: ''').lower()
    return selection


def value_input(selection):
    value = input('''\nPlease enter the temperature you
want to convert: ''')
    try:
        value = float(value)
    except ValueError:
        print('That is not a number!\n')
    else:
        if selection == 'c':
            convert_c2f(value)
        else:
            convert_f2c(value)
            # return value


def convert_c2f(value):
    print(f'The answer is: {(value * (9/5)) + 32}°F\n')
    return


def convert_f2c(value):
    print(f'The answer is: {(value-32) * (5/9)}°C\n')
    return


def main():
    while True:
        selection = read_selection()
        if selection == 'q':
            return
        elif selection == 'c' or selection == 'f':
            value_input(selection)
            '''convert_c2f()
        elif selection == 'f':
            convert_f2C()'''
        else:
            print('Invalid selction. Try again.\n')
 

if __name__ == '__main__':
    main()