import time

#partition function
def partition(array, l, r):
    p = array[l]
    i = l+1
    for j in range(l+1, r):
        if array[j] < p:
            swap(array, j, i)
            i = i + 1
    swap(array, l, i-1)
    return i - 1

#swapping function 
def swap(array, firstindex, secondindex):
    temp = array[firstindex]
    array[firstindex] = array[secondindex]
    array[secondindex] = temp

#quicksort
def quicksort(array, l, r):
    if l >= r:
        return array[0]
    i = choosepivot(array, l, r)
    swap(array, l, i)
    j = partition(array, l, r)
    #recursive
    quicksort(array, l, j-1)
    quicksort(array, j+1, r)

#choose the first element as pivot
def choosepivot(array, l, r):
    return l

#main function
if __name__=="__main__":
    file = open("problem5.6test1.txt", "r")
    array1 = list()

    #initialize array
    start = time.time()
    for line in file:
        array1.append(int(line))

    file.close()

    file = open("problem5.6test2.txt", "r")
    array2 = list()

    #initialize array
    for line in file:
        array2.append(int(line))

    file.close()

    file = open("problem5.6test3.txt", "r")
    array3 = list()

    #initialize array
    for line in file:
        array3.append(int(line))

    file.close()

    print("FIRST TEST")
    n = len(array1)
    start = time.time()
    quicksort(array1, 0, n)
    end = time.time()
    print(array1)
    print("array1 took " + str((end-start)) + " seconds.")

    
    print("\n\nSECOND TEST")
    n = len(array2)
    start = time.time()
    quicksort(array2, 0, n)
    end = time.time()
    print(array2)
    print("array2 took " + str((end-start)) + " seconds.")

    
    print("\n\nTHIRD TEST")
    n = len(array3)
    start = time.time()
    quicksort(array3, 0, n)
    end = time.time()
    print(array3)
    print("array2 took " + str((end-start)) + " seconds.")
    


