# ==============================================================
# Payroll Program - Group Project
# Group Name: The Loop Troop
# Members: Kaleb Whybrew, [Teammate 2], [Teammate 3], [Teammate 4]
#
# This program enters employee information, looks up the pay
# rate from our employee database using the employee ID,
# calculates gross pay (with overtime), takes out state and
# federal taxes, shows a paycheck, and saves all the results
# to a spreadsheet file called payroll_results.csv
# ==============================================================

# ----- constants (so we never use magic numbers) -----
STATE_TAX_RATE = 0.056     # state tax is 5.6%
FED_TAX_RATE = 0.079       # federal tax is 7.9%
OVERTIME_RATE = 1.5        # time and a half for overtime
REGULAR_HOURS = 40         # a normal work week
MAX_HOURS = 80             # more than this is not allowed
WARNING_HOURS = 60         # more than this is unusual, so we double check
MAX_DEPENDENTS = 10        # most dependents we allow

# ----- our pay rate "database" -----
# The employee ID is the primary key and the hourly rate is the value.
# (In Module 8 this will be replaced with a real database look-up.)
payRateDB = {
    101: 15.00,
    102: 18.50,
    103: 22.00,
    104: 12.75,
    105: 19.25,
    106: 16.50,
    107: 25.00,
    108: 14.00,
    109: 20.50,
    110: 17.75
}


# ==============================================================
# MODULE 1 - INPUT AND SECURITY CHECKS   (written by Kaleb)
# Every input is checked so bad data can not get in.
# ==============================================================

def getEmployeeID():
    # keeps asking until we get a real employee ID (0 means quit)
    while True:
        answer = input("Enter employee ID (0 to quit): ")
        if answer.isdigit():
            empID = int(answer)
            if empID == 0:
                return 0
            if empID in payRateDB:
                return empID
            else:
                print("  SECURITY CHECK: ID", empID, "is not in the database. Try again.")
        else:
            print("  SECURITY CHECK: the ID must be a number. Try again.")


def getName(prompt):
    # keeps asking until the name is not blank and is only letters
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print("  SECURITY CHECK: a name can not be blank and must be letters only. Try again.")


def getDependents():
    # keeps asking until dependents is a whole number from 0 to 10
    while True:
        answer = input("Enter number of dependents (0-10): ")
        if answer.isdigit():
            dependents = int(answer)
            if dependents <= MAX_DEPENDENTS:
                return dependents
            else:
                print("  SECURITY CHECK: dependents must be 0 to 10. Try again.")
        else:
            print("  SECURITY CHECK: dependents must be a whole number. Try again.")


def getHours():
    # keeps asking until the hours are a number between 0 and 80
    # anything over 60 is unusual, so we ask the user to confirm it
    while True:
        answer = input("Enter hours worked: ")
        try:
            hours = float(answer)
        except ValueError:
            print("  SECURITY CHECK: hours must be a number. Try again.")
            continue
        if hours <= 0:
            print("  SECURITY CHECK: hours must be more than 0. Try again.")
        elif hours > MAX_HOURS:
            print("  SECURITY CHECK: hours can not be more than", MAX_HOURS, ". Try again.")
        elif hours > WARNING_HOURS:
            check = input("  WARNING: " + answer + " hours is unusual. Is that correct? (y/n): ")
            if check == "y":
                return hours
            else:
                print("  OK, let's re-enter the hours.")
        else:
            return hours


# ==============================================================
# MODULE 2 - CALCULATIONS   (written by [Teammate 2])
# Gross pay with overtime, then the two taxes.
# ==============================================================

def calcGrossPay(rate, hours):
    # regular pay for the first 40 hours, time and a half after that
    if hours <= REGULAR_HOURS:
        gross = rate * hours
    else:
        overtimeHours = hours - REGULAR_HOURS
        gross = (rate * REGULAR_HOURS) + (rate * OVERTIME_RATE * overtimeHours)
    return round(gross, 2)


def calcStateTax(preTaxAmount):
    # state tax is 5.6% of the pre-tax amount
    return round(preTaxAmount * STATE_TAX_RATE, 2)


def calcFedTax(preTaxAmount):
    # federal tax is 7.9% of the pre-tax amount
    return round(preTaxAmount * FED_TAX_RATE, 2)


# ==============================================================
# MODULE 3 - OUTPUT AND SPREADSHEET   (written by [Teammate 3])
# Shows the paycheck on screen and saves everything to a file.
# ==============================================================

def printPaycheck(firstName, lastName, empID, dependents, hours, rate,
                  preTax, stateTax, fedTax, postTax):
    print("  --------- PAYCHECK ---------")
    print("  Employee:  " + firstName + " " + lastName + "  (ID " + str(empID) + ")")
    print("  Dependents:", dependents)
    print("  Hours worked:", hours, " Rate: $" + format(rate, ".2f"))
    print("  Gross pay (pre-tax):  $" + format(preTax, ".2f"))
    print("  State tax (5.6%):     $" + format(stateTax, ".2f"))
    print("  Federal tax (7.9%):   $" + format(fedTax, ".2f"))
    print("  Net pay (post-tax):   $" + format(postTax, ".2f"))
    print("  ----------------------------")


def saveToSpreadsheet(allRows):
    # writes every paycheck to a csv file that opens in Excel
    outFile = open("payroll_results.csv", "w")
    outFile.write("ID,First Name,Last Name,Dependents,Hours,Rate,")
    outFile.write("Gross Pay (Pre-Tax),State Tax,Federal Tax,Net Pay (Post-Tax)\n")
    for row in allRows:
        outFile.write(row + "\n")
    outFile.close()
    print("Results were saved to payroll_results.csv")


# ==============================================================
# MAIN PROGRAM  (put together by the whole team)
# ==============================================================

print("========================================")
print("   The Loop Troop Payroll Program")
print("========================================")

allRows = []            # every finished paycheck goes in this list
employeeCount = 0

while True:
    print()
    empID = getEmployeeID()
    if empID == 0:
        break           # the user is done entering employees

    firstName = getName("Enter first name: ")
    lastName = getName("Enter last name: ")
    dependents = getDependents()
    hours = getHours()

    # the pay rate comes from the database using the ID as the key
    rate = payRateDB[empID]

    # do all the calculations
    grossPay = calcGrossPay(rate, hours)
    preTax = grossPay                      # taxes come out of the pre-tax amount
    stateTax = calcStateTax(preTax)
    fedTax = calcFedTax(preTax)
    postTax = round(preTax - stateTax - fedTax, 2)

    # show the paycheck and remember it for the spreadsheet
    printPaycheck(firstName, lastName, empID, dependents, hours, rate,
                  preTax, stateTax, fedTax, postTax)
    row = (str(empID) + "," + firstName + "," + lastName + "," + str(dependents)
           + "," + str(hours) + "," + str(rate) + "," + str(preTax) + ","
           + str(stateTax) + "," + str(fedTax) + "," + str(postTax))
    allRows.append(row)
    employeeCount = employeeCount + 1

print()
print("Payroll finished for", employeeCount, "employees.")
saveToSpreadsheet(allRows)
