myList = [5, 6, 9, 8, 7, 8, 5, 54, 56, 66, 6, 6, 6, 5, 5, 4, 1, 2]
occurences = []
for item in myList:
    count = 0
    for x in myList:
        if x == item:
            count += 1
    occurences.append(count)
duplicates = set()
index = 0
while index < len(myList):
    if occurences[index] != 1:
        duplicates.add(myList[index])
    index += 1
print(duplicates)
