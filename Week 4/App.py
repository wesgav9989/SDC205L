# 4.3 Course Project * Wesley Gavitt

from datetime import datetime

filePath = "ZooData.csv"

# This function converts pounds to kilograms
def convertData(value):
    return value / 2.205

# This function inserts one line of data into the csv file
def insertData(path, data):
    try:
        file = open(path, "a")
        file.write(data + "\n")
        file.close()
    except:
        print("Error: data could not be saved")

# This function displays the contents of the csv file
def viewData(path):
    try:
        file = open(path, "r")
        print("The file", path)
        print(file.read())
        file.close()
    except:
        print("Error: data could not be read")

# This function gets user input and saves converted data to the csv file
def getInput():
    entries = int(input("How many entries are you inputting?\n"))

    for count in range(entries):
        date = input("Enter a date:\n\n")
        pounds = float(input("Enter the weight in pounds for the inputted date:\n"))

        # The next line calls the convertData function, passes in pounds, and returns the weight converted to kilograms
        kilograms = convertData(pounds)

        data = date + "," + str(pounds) + "," + str(kilograms)

        insertData(filePath, data)

        print("The following data was saved at", datetime.now())
        print(data)

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
elif userOption == "2":
    print("You selected", userOption, "at", datetime.now())
    viewData(filePath)
else:
    print("Error: The chosen functionality is not implemented yet")
