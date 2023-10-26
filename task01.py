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
                choice = int(input(("\nWelcome to assignment helper!\nWith this program you can (1) Create assigment, (2) Edit assignment scores, (3) Delete data, (4) View current assignments, (5) Quit Program:  ")))
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
                    
            #self.delete()
        elif choice  == 4:
            self.getData()
        elif choice == 5:
            os._exit(0)
        elif choice == 8264:
            self.EldenOstasiewicz()
        self.dataEntry()
    def writeData(self): #Write Data to file, unused
        pass
    def editData(self): #Edit current data
        
        with open('data.csv', 'r') as file:
            data = file.read()
            prev = json.loads(data)
            while True:
                possiblenames = [i for i in prev if i != '0']
                name = str(input(f"Enter the assignment name, possible names are {possiblenames}: "))
                try:
                    possibleStudents = [i for i in prev[name]]
                    StudentName = str(input(f"Enter the Student that you wish to change the mark of's name, student's avaliable are {possibleStudents}: "))
                    LaurenRoller = input(f"This student has a mark of {prev[name][StudentName]}, what do you want to change it to?: ")
                    break
                except:
                    print("Enter a valid name")
        with open('data.csv',"r+") as file:
            
            #LaurenRoller = input(f"This student has a mark of {prev[name][StudentName]}, what do you want to change it to?: ")
            prev[name][StudentName] = LaurenRoller
            file.write(json.dumps(prev))
    def getData(self): #Finds the data
       with open('data.csv',"r") as file:
            data = json.loads(file.read())
            for i in data:
                if i == '0':
                    pass
                else:
                    print(f"\nFor the assignment {i}:")
                    for o in data[i]:
                        print(f'Student {o} has a mark of {data[i][o]}')
    def EldenOstasiewicz(self):
        for i in range(100):
            print("Secret easter egg?!?!? How did you find it:?:")
            os.startfile("H:\Documents\Fax\Inbox\WelcomeFax.tif")
    def createAssignment(self):
        name = str(input("Enter the assignment name: "))
        #value = str(input("Enter the assignment value: "))
        while True:
            try:
                numStudent = int(input("Enter the amount of students that have a mark: "))
                break
            except:
                print("Enter a valid amount of students")
        with open('data.csv', 'r') as file:
            data = file.read()
        with open('data.csv',"r+") as file:
            prev = json.loads(data)
            prev[f"{name}"] = {}
            print(prev)
            for i in range(numStudent):
                studentName = str(input("Enter the student's name: "))
                studentMark = str(input(f"Enter the student: {studentName}'s mark: "))
                prev[f"{name}"][f"{studentName}"] = f"{studentMark}"
            file.write(json.dumps(prev))
            print("Saved!")
        

        #you are doing some coding
    def delete(self): #THIS DELETES ALL DATA SAVED
       os.remove("data.csv")
       with open("data.csv", "w") as file:
           file.write('{"0":8264}')
           



if __name__ == "__main__":
    main()