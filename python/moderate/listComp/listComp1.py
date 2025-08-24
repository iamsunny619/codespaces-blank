""" marks = [10,20,30,40]
newMarks = []
for mark in marks:
    newMarks.append(mark + 10)

print(newMarks) """

marks=[10,20,30,40,50]
newMarks = [x+10 for x in marks]
print(newMarks)