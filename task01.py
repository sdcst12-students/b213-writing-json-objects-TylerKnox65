#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""

import json
from types import DynamicClassAttribute
import os


class main():
    def __init__(self) -> None:
       self.dataEntry()
    
    def dataEntry(self): #Enter selection mode
        while True:
            try:
                choice = int(input(("Welcome to assignment helper!\nWith this program you can (1) Create assigment, (2) Edit assignment scores, (3) Delete data, (4) View current assignments:  ")))
                break
            except:
                print("Enter a valid integer.")
        if choice == 1:
            self.createAssignment()#tyler is a goofy name (Also the prreson)

        elif choice == 2:
            self.editData()
        elif choice == 3:
            try:
                sure = str(input("Are you sure? Enter YES to confirm: "))
                if sure != "YES":
                    raise ValueError('A very specific bad thing happened.')
                else:
                    self.delete()
            except:
                self.dataEntry()
                    
            self.delete()
    def writeData(self): #Write Data to file
        pass
    def editData(self): #Edit current data
        pass
    def getData(self): #Finds the data
        pass
    def createAssignment(self):
        name = str(input("Enter the assignment name: "))
        value = str(input("Enter the assignment value: "))
        with open('data.csv') as file:
            pass
        
    def delete(self): #THIS DELETES ALL DATA SAVED
       os.remove("data.csv")
       with open("data.csv", "w") as file:
           file.write("{0:0}")



if __name__ == "__main__":
    main()