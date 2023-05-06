import pyfiglet
import math  # We import an external library to use its functions


def to_color(string, color):
    color_code = {'blue': '\033[34m',
                    'yellow': '\033[33m',
                    'green': '\033[32m',
                    'red': '\033[31m'
                    }
    return color_code[color] + str(string) + '\033[0m'

text = pyfiglet.figlet_format(text = "__Calculator__", font = 'Slant')
print(to_color(text,'blue'))


active = True  # This is our on/off switch for the program. True is on and False is off.

while active:  # We make a while loop. So while active(True) - keep repeating everything inside
    print ("1) Add")  # This is our menu and list options for the user - It's inside a while loop so that the entire program doesn't run once and then exit.
    print ("2) Subtract")
    print ("3) Divide")
    print ("4) Multiply")
    print ("5) Exponential")
    print ("6) Square Root")
    print ("7) Exit")
    print

    try:  # This is a try statement used to handle errors
        answer = int(input("Option: "))  # This is a variable which stores the value a user enters
                                    # The input function makes the program wait for user input
                                    # Input returns integers, so letters and special characters cause errors
        print  # These blank print statements are for neatness

        # Note We Do Not Need To Use If-Else Statements Here But For Simplicities Sake We Are

        if answer == 1:  # Basic if statement - if user entered 1 then do what's next
           a = int(input("Enter the number: "))

           ask ="Y"

           while (ask == "Y"):
               b = int(input("Enter the number: "))
               a = sum([a,b])
               ask = input("Do you want to add more numbers(Y/N): ")
           else:
               print("Answer is:", a)
               if (ask == "N"):
                   break
               print

        elif answer == 2:   # Basic if statement - if user entered 2 then do what's next
            a = int(input("Enter the number: "))  # Enter the first number

            ask = "Y"

            while (ask == "Y"):  # Inserting looop because if user want to add more numbers
                b = int(input("Enter the number: "))
                a = a - b
                ask = input("Do you want to subtract more numbers(Y/N): ")
            else:
                print("Answer is:", a)
                if (ask == "N"): # Closing the loop
                    break
                print

  
        elif answer == 3:    # Basic if statement - if user entered 3 then do what's next
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            Division = first / second
            print ("Answer is:", first, "/", second, "=", Division)
            print

        elif answer == 4:    # Basic if statement - if user entered 4 then do what's next
            a = int(input("Enter the number: "))

            ask = "Y"

            while(ask == "Y"):
                b = int(input("Enetr the Number: "))
                a = a * b
                ask = input("Do you want to multiply more numbers(Y/N): ")
            else:
                print("Answer is:", a)
                if (ask == "N"):
                    break
            print

        elif answer == 5:    # Basic if statement - if user entered 5 then do what's next
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            Exponential = first ** first
            print ("Answer is:", first, "**", second, "=", Exponential)
            
        elif answer == 6:     # Basic if statement - if user entered 6 then do what's next
            first = float(input("First Number: "))
            Squared_root = math.sqrt(first)  # Here we use an external function from the Math module which is sqrt ( Square Root )
            print ("Answer is:", Squared_root)
            print

        elif answer == 7:  # This is how we exit the program. We make active go from True to False.
                           # This has to do with how we designed the while loop. Since it's dependant on the active variable to run
            active = False
        else:  # This is for if the user enters any number that's not on the list
            print
            print ("Please select a valid option number")
            print
    except NameError:  # This is part of the try statement. This is how we handle the errors
                       # If it's a NameError - Do this and so on
                       # NameError means we entered letters or rather variable names that are not defined in the code.
        print
        print ("NameError: Please Use Numbers Only")
        print
    except SyntaxError:  # SyntaxError means we typed letters or special characters i.e !@#$%^&*( or if we tried to run python code
        print
        print ("SyntaxError: Please Use Numbers Only")
        print
    except TypeError:  # TypeError is if we entered letters and special characters or tried to run python code
        print
        print ("TypeError: Please Use Numbers Only")
        print
    except AttributeError:  # AttributeError handles rare occurances in the code where numbers not on the list are handled outside of the if statement
        print
        print ("AttributeError: Please Use Numbers Only")
        print