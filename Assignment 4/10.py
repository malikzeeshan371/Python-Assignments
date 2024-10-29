# 10. Print each element in a list of lists.
# Example: lst = [[1, 2], [3, 4]] should print 1, 2, 3, 4
list1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in list1:
    for j in i:
        print(j ,end=" ")
