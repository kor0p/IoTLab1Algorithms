from time import time

class Ship:
    def __init__(self, tonnage=0, name="NoName", numOfPassengers=0):
        self.tonnage = int(tonnage)
        self.name = name
        self.numOfPassengers = int(numOfPassengers)

with open("input.txt") as file:
    ships = [Ship(*line.split(',')) for line in file.readlines()]
A = [s.tonnage for s in ships]
i = 0
permutations = 0
comparings = 0
start_time = time()
while i < len(A):
    j = i
    comparings += 1
    while j > 0 and A[j-1] > A[j]:
        A[j], A[j-1] = A[j-1], A[j]
        j = j - 1
        permutations += 1
        comparings += 1
    i += 1
print(f"Insertion sort\ntime: {time()-start_time},\npermutations: {permutations},\ncomparings: {comparings},\nres:{A}.\n\n")
def mergeSort(alist, p=0, c=0):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        p, c = mergeSort(lefthalf, p, c)
        p, c = mergeSort(righthalf, p, c)

        # merging
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            c += 1
            p += 1
            if lefthalf[i] >= righthalf[j]:
                alist[k]=lefthalf[i]
                i += 1
            else:
                alist[k]=righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            p += 1
            alist[k]=lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            p += 1
            alist[k]=righthalf[j]
            j += 1
            k += 1
    return p, c
A = [s.numOfPassengers for s in ships]
start_time = time()
permutations, comparings = mergeSort(A)
print(f"Merge sort\ntime: {time()-start_time},\npermutations: {permutations},\ncomparings: {comparings},\nres:{A}.\n")
