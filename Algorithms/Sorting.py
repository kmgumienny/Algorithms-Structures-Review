def example1():

    def python_sort():
        int_array = [2, 42, 54, 23, 3, 6, 7, 8]
        char_array = ['a', 'c', 'b', 'z', 'd', 's']

        int_array.sort()
        char_array.sort()

        for val in int_array:
            print(val, end=', ')

        print()

        for val in char_array:
            print(val, end=', ')

    python_sort()


def example2(arr):

    def bubble_sort(input1):
        if len(input1) == 1:
            return

        length = len(input1)

        for k in range(0, length):
            for i in range(0, length - 1):
                if input1[i] > input1[i + 1]:
                    temp = input1[i + 1]
                    input1[i + 1] = input1[i]
                    input1[i] = temp

    bubble_sort(arr)

    for val in arr:
        print(val, end=' ')
    print()


def example3(arr):

    def selection_sort(input2):
        if len(input2) == 1:
            return input2

        length = len(input2)

        for outer_index in range(0, length):
            smallest = outer_index
            for inner_index in range(outer_index, length):
                if input2[smallest] > input2[inner_index]:
                    smallest = inner_index
            temp = input2[outer_index]
            input2[outer_index] = input2[smallest]
            input2[smallest] = temp

    selection_sort(arr)
    for val in arr:
        print(val, end=' ')
    print()


def example4(arr):

    def insertion_sort(input3):

        for i in range(1, len(input3)):
            key = input3[i]
            j = i - 1

            while j >= 0 and key < input3[j]:
                input3[j + 1] = input3[j]
                j -= 1

            input3[j + 1] = key

    insertion_sort(arr)
    for val in arr:
        print(val, end=' ')
    print()


# Obtained from https://www.geeksforgeeks.org/python-program-for-merge-sort/
def example5(arr):

    def merge(input4, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = input4[l + i]

        for j in range(0, n2):
            R[j] = input4[m + 1 + j]

            # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                input4[k] = L[i]
                i += 1
            else:
                input4[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            input4[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            input4[k] = R[j]
            j += 1
            k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted
    def merge_sort(input4, l, r):
        if l < r:
            # Same as (l+r)/2, but avoids overflow for
            # large l and h
            m = (l + (r - 1)) // 2

            # Sort first and second halves
            merge_sort(input4, l, m)
            merge_sort(input4, m + 1, r)
            merge(input4, l, m, r)

    merge_sort(arr, 0, len(arr) - 1)
    for val in arr:
        print(val, end=' ')
    print()


# Got from https://www.geeksforgeeks.org/python-program-for-quicksort/
def example6(arr):
    # This function takes last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    # of pivot
    def partition(input5, low, high):
        i = (low - 1)  # index of smaller element
        pivot = input5[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if input5[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                input5[i], input5[j] = input5[j], input5[i]

        input5[i + 1], input5[high] = input5[high], input5[i + 1]
        return i + 1

        # The main function that implements QuickSort

    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort
    def quick_sort(input5, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(input5, low, high)

            # Separately sort elements before
            # partition and after partition
            quick_sort(input5, low, pi - 1)
            quick_sort(input5, pi + 1, high)

    quick_sort(arr, 0, len(arr) - 1)
    for val in arr:
        print(val, end=' ')
    print()


values = [33, 61, 4, 7, 35, 25, 2, 6, 5, 76, 12]
print("Bubble Sort:")
example2(values)
values = [33, 61, 4, 7, 35, 25, 2, 6, 5, 76, 12]
print("Selection Sort:")
example3(values)
values = [33, 61, 4, 7, 35, 25, 2, 6, 5, 76, 12]
print("Insertion Sort:")
example4(values)
values = [33, 61, 4, 7, 35, 25, 2, 6, 5, 76, 12]
print("Merge Sort:")
example5(values)
values = [33, 61, 4, 7, 35, 25, 2, 6, 5, 76, 12]
print("Quick Sort:")
example6(values)
