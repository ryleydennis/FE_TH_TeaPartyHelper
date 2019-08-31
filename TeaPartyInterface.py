import pandas as ps
import os
import numpy as np


def checkForX(i):
    if i == "exit" or i == "x":
        return True
    else:
        return False

def GuestExists(guest, houses):
    for house in houses.columns:
        for person in houses[house]:
            if str(person).lower() == guest.lower():
                return True
        # if guest in houses[house]:
        #     return True
    return False

def getTeaPath(index):
    if index == 0: return "favoriteTeas"
    if index == 1: return "interestedTopics"
    if index == 2: return "finalComments"
    if index == 3: return "likes"

def getTablesForGuest(guest):
    tables = []
    path = "TeaPartyGuests/"+guest+"/"
    if os.path.exists(path):
        for i in range(4):
            if os.path.exists(path + getTeaPath(i) + ".csv"):
                tables.append(ps.read_csv(path + getTeaPath(i) + ".csv", header=0))
    return tables

def clearScreen():
    if  os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printFull(table):
    ps.set_option('display.max_rows', len(table))
    ps.option_context('display.colheader_justify','left')
    print(table)
    ps.reset_option('display.max_rows')

def main():
    
    clearScreen()
    i = ""
    while i.lower() != "exit" or i.lower() != "x":
        
        houses = ps.read_csv("TeaPartyGuests.csv", header=0)
        houses.replace(np.NaN, "-", inplace=True)
        print(houses)

        i = input("Type in a Guests name, or type exit or x to quit\nGuest: ") 
        if checkForX(i): break
        
        if GuestExists(i, houses):
            guest = i
            tables = getTablesForGuest(guest)

            for index in range(len(tables)):
                tables[index].replace(np.nan, '-', inplace=True)
                print("\n..." + getTeaPath(index) + "...")
                printFull(tables[index])
            i = input("\n press any key to continue (or exit (x) to quit\n")
            if checkForX(i): break

        else:
            print("Not a guest\n\n")
        clearScreen()

if __name__ == "__main__":
    main()