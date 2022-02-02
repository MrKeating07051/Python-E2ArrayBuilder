fileNotValid = True
print("KUKA's E2 Array Translator!\n")

while fileNotValid:
    # Get a file name.
    try:
        rawText = input("Enter text filepath to translate: ")
    except ValueError:
        print("Invalid Value.\nEnter text file name to translate: ")
    try:
        openedFile = open(rawText, "r")
    except FileNotFoundError:
        print("File \""+rawText+"\" does not exist.")
    else:
        fileNotValid = False  # Break the file check-loop
        contents = openedFile.readlines()  # Retrieve contents of host file
        noOfLines = len(contents)  # Count number of lines of host file
        fileName = rawText.replace(".txt", "")  # Delete the .txt extension.

        # insert appropriate formatting for each content item.
        for line in range(noOfLines-1):
            if line < noOfLines-2:  # for each line besides the last
                contents[line] = "\"" + contents[line].strip() + "\",\n"
            else: # for the last line
                contents[line] = "\"" + contents[line].strip() + "\"\n"
        openedFile.close()
        print("File " + rawText + " has " + str(noOfLines) + " lines.")

# Confirmation prompting
if openedFile:
    confirmCheck = input("Write file? y/n ")
    if confirmCheck == "y":
        pass
    else:
        exit()

# Copy the file with formatting.
with open(fileName + "_E2Array.txt", "w") as nf:
    nf.write("insertArrayNameHere = array(\n")
    for line in range(noOfLines-1):
        nf.write("     "+contents[line])
    nf.write(")")
    print("\nCreated " + fileName + "_E2Array.txt\n")
    nf.close()

input("Press Enter to continue...")
