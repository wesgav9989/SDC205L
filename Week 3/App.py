# 3.4 Course Project * Wesley Gavitt

from datetime import datetime

def convertData(value):
    return value / 2.205

def getInput():
    entries = int(input("How many entries are you inputting?\n"))

    for count in range(entries):
        date = input("Enter a date:\n\n")
        pounds = float(input("Enter the weight in pounds for the inputted date:\n"))

        # The next line calls the convertData function, passes in pounds, and returns the weight converted to kilograms
        kilograms = convertData(pounds)

        print("The following was saved at", datetime.now(), ":")
        print(date + "," + str(pounds) + "," + str(kilograms))

print("WESGAV9989 Spreadsheet Automation Menu")
print("Choose a number from the following options")

menuOptions = [
    "Input Data",
    "View Current Data",
    "Generate Report"
]

for index, option in enumerate(menuOptions, start=1):
    print(index, option)

# The next line retrieves the inputted option and stores into the variable called userOption
userOption = input()

if userOption == "1":
    print("You selected", userOption, "at", datetime.now())
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")
