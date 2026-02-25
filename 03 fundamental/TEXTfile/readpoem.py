# jabber=open("Jabberwocky.txt","r")

# for line in jabber:
#     print(line.rstrip(),end="")
#  #   print(len(line))
# jabber.close()


# with open("Jabberwocky.txt","r") as jabber:
#     for line in jabber:
#         print(line.rstrip())

# compare_simple.py
file2 = "listOfMerchand.txt"
file1 = "D7RepoReport.txt"


# Read second file into a list
with open(file2, "r") as f:
    file2_lines = [line.strip() for line in f]

print("Files present in", file1, "but NOT in", file2)
print("-" * 50)

# Loop through first file and check in second file
with open(file1, "r") as f:
    for line in f:
        filename = line.strip()
        if filename and filename not in file2_lines:
            print(filename)
