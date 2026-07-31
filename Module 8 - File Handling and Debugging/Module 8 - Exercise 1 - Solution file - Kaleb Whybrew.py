# ==============================================================
# Module 8 - Exercise 1 - Solution file
# Author: Kaleb Whybrew
#
# Geraldine's Landscaping and Gerard's Landscaping merged their
# businesses. This program merges their two customer files (each
# already sorted by customer number) into ONE file that is still
# in customer number order. It uses the standard merge algorithm
# with a HIGH_VALUE sentinel, the same logic shown in the flowchart
# and pseudocode. (Assumes there are no identical customer numbers.)
# ==============================================================

HIGH_VALUE = 999999   # sentinel: larger than any real customer number


def readFile(filename):
    # reads one customer file into a list of records (each record is a
    # dictionary with the four fields)
    records = []
    dataFile = open(filename, "r")
    for line in dataFile:
        line = line.strip()
        if line == "":
            continue                      # skip blank lines
        field = line.split(",")
        record = {
            "custNum": int(field[0]),
            "lastName": field[1].strip(),
            "address": field[2].strip(),
            "area": int(field[3])
        }
        records.append(record)
    dataFile.close()
    return records


def getRecord(records, index):
    # returns the record at index, or a sentinel record when we run out
    if index < len(records):
        return records[index]
    else:
        return {"custNum": HIGH_VALUE, "lastName": "", "address": "", "area": 0}


def mergeFiles(geraldine, gerard, outName):
    outFile = open(outName, "w")
    outFile.write("CustomerNumber,LastName,Address,PropertyAreaSqFt\n")

    aIndex = 0                            # position in Geraldine's list
    bIndex = 0                            # position in Gerard's list
    a = getRecord(geraldine, aIndex)
    b = getRecord(gerard, bIndex)
    count = 0

    # keep going until BOTH files are finished (both at the sentinel)
    while a["custNum"] != HIGH_VALUE or b["custNum"] != HIGH_VALUE:
        if a["custNum"] < b["custNum"]:   # Geraldine's is smaller -> write it first
            record = a
            source = "Geraldine"
            aIndex = aIndex + 1
            a = getRecord(geraldine, aIndex)
        else:                             # Gerard's is smaller -> write it first
            record = b
            source = "Gerard"
            bIndex = bIndex + 1
            b = getRecord(gerard, bIndex)

        line = (str(record["custNum"]) + "," + record["lastName"] + "," +
                record["address"] + "," + str(record["area"]))
        outFile.write(line + "\n")
        print(format(record["custNum"], "<6"), format(record["lastName"], "<12"),
              format(record["address"], "<16"), record["area"], " (from " + source + ")")
        count = count + 1

    outFile.close()
    print("Merged", count, "customer records into:", outName)


# ----- main program -----
print("=== Merging Geraldine's and Gerard's customer files ===")
print(format("Cust#", "<6"), format("Last Name", "<12"), format("Address", "<16"), "Area")
print("-" * 55)
geraldineCustomers = readFile("Geraldines Businesses.csv")
gerardCustomers = readFile("Geralds Businesses.csv")
mergeFiles(geraldineCustomers, gerardCustomers, "Merged Customers - Kaleb Whybrew.csv")
