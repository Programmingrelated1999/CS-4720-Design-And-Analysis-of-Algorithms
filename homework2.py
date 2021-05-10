#CountInv Algorithm

#page 65 sortandcountInv

def CountInt(array):
    #if n = 0 or n = 1 then return array,0
    if len(array) == 1 or len(array) == 0:
        return array, 0

    mid = len(array)//2

    #leftinversion, rightinversion
    left,leftinversion = CountInt(array[:mid])
    right,rightinversion = CountInt(array[mid:])
    sortedArray, splitinversion = MergeAndCountSplitInv(left,right)

    #return sortedArray, leftInv + rightInv + SplitInversion
    return sortedArray, splitinversion + leftinversion + rightinversion

 
def MergeAndCountSplitInv(left,right):
    #initialize
    Array = []
    i = j = inversion = 0

    #if right is bigger then dont count, if left is bigger then all the elements on the left are in inversion.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            Array.append(left[i])
            i = i + 1
        else:
            Array.append(right[j])
            j = j + 1
            inversion = inversion + (len(left)-i)

    #leftovers from left or right. Fill out.
    while i < len(left):
            Array.append(left[i])
            i = i + 1
            
    while j < len(right):
            Array.append(right[j])
            j = j + 1
            
    return Array, inversion

#main
if __name__=="__main__":
    #open file I use 100000 elements
    file = open("problem3.5.txt", "r")
    array = []

    #initialize array
    for line in file:
        array.append(int(line))

    file.close()

    #call CountInt and print
    sortedArray,inversioncount = CountInt(array)
    print ("There are " + str(inversioncount) + " inversions in the array")
    print("The array is", sortedArray)

####Output
##= RESTART: C:\Users\khmya\Desktop\Spring 2021\Design and Analysis of Algorithms\homework2.py
##There are 2407905288 inversions in the array

