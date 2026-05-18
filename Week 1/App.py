# 1.6 Course Project Wesley Gavitt

from datetime import datetime

print("WESGAV9989 Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called userOption
userOption = input()

print("You selected", userOption, "at", datetime.now())
