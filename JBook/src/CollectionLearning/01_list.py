# print only if a data set is sum >= 10
nested_lists = [[1, 2], [4, 5, 2], [10, 0], [3],[5,5],[2,2,2,2,2]]

for lists in nested_lists:
    total = 0
    for list in lists:
        total = total + list
    
    if(total>9):
        print(lists)

