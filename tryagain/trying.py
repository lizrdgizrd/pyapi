#!/usr/bin/python3

while True:
    #pull info from user and create file
    try:
        name = input('Enter file name: ')
        with open(name, 'w') as myfile:
            myfile.write('Well done\n')
    except:
        print("Error in file creation. Try again.\n")
    else:
        print("File created successfully")
        break
