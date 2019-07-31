#!/usr/bin/python3

import sys

#start with infinite loop
while True:
    try:
        z = "successful job"
        print("Let's divide x by y")
        x = int(input("What is the int value of x?"))
        y = int(input("What is the int value of y?"))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling of a runtime error:", zerr)
        z = "Error div by 0"
    except ValueError as err:
        z = "Value Error detected via user input"
    except Exception as err:
        print("We didn't code for this error yet.", err)
        print(sys.exc_info()[0])
        z = sys.exc_info()[0] + "| "+ err
        raise
    finally:
        with open("try02.log", "a") as log:
            log.write(z+"\n")
        break

