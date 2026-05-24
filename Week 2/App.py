# 2.4 Course Project * Wesley Gavitt

from datetime import datetime

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

if userOption == "1" or userOption == "2" or userOption == "3":
    print("You selected", userOption, "at", datetime.now())
else:
    print("Error: invalid choice selected")
