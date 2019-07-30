from timeit import default_timer as timer
import math


def example1():

    # This is an example of a function that has a Big O notation of O(n). Referred to as linear time.
    nemo = ['nemo']
    everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
    huge_array = ['blep'] * 100000
    huge_array.append('nemo')

    def find_nemo(array):
        start = timer()
        for i in range(0, len(array)):
            if array[i] == 'nemo':
                print("Found nemo")
                break
        end = timer()
        print("The function took {} seconds".format(end-start))
    find_nemo(nemo)
    find_nemo(everyone)
    find_nemo(huge_array)


def example2():

    # This is an example of a function that has a Big O notation of O(1). Referred to as constant time.
    boxes = [1, 2, 3, 4, 5, 6]

    def log_first_two_boxes(array):

        print(array[1])
        print(array[2])

    log_first_two_boxes(boxes)


def challenge1():

    # This function has a Big O of n because of the call to the example2 function
    something = [1, 2, 3]

    def fun_function(foo):
        a = 10      # O(1)
        a = 50 + 3  # O(1)

        for i in range(0, len(foo)):
            example2()      # O(n)
            random = True   # O(1)
            a += 1          # O(1)
        return a            # O(1)

    fun_function(something)


def challenge2():

    # What is the Big O of the below function? (Hint, you may want to go line by line) function anotherFunChallenge
    # (input)
    # Answer = O(n)
    def another_fun_challenge(foo):
        a = 5
        b = 10
        c = 50
        for i in range(0, foo):
            x = i + 1
            y = i + 2
            z = i + 3

        for j in range(0, foo):
            p = j * 2
            q = j * 2

        whoAmI = "I don't know"


def example3():

    # Rule 2 of Big O is to drop constants. This function is technically O(.5n + 100)
    # Doesn't matter that the function only goes through half of the function.
    # This function is O(n + 1) but drop the 1 so it's O(n)
    def print_first_item_then_first_half_then_say_hi_100_times(array):
        print(array[0])
        middle = math.floor(len(array)//2)
        index = 0

        while index < middle:
            print(array[index])

        for i in range(0,100):
            print('Hi')


def example4():

    # Rule 3 of Big O is to use different terms for different inputs
    # The Big O of this function is O(a + b)
    def compress_boxes_twice(boxes, boxes2):
        for box in boxes:
            print(box)

        for box in boxes2:
            print(box)


def example5():

    # This is an O(n^2). This is also known as quadratic time
    nums = [1, 2, 3, 4, 5]

    def log_all_pairs_of_array(array):
        for i in range(0, len(array)):
            for j in range(0, len(array)):
                if i != j:
                    print("{}{}".format(array[i], array[j]))

    log_all_pairs_of_array(nums)


def example6():

    # Rule 4 of Big O is to only keep the dominant term.
    # The technical Big O for this function is O(n + n^2) but the dominant term means that it is O(n^2)
    def print_all_numbers_then_all_pair_sums(numbers):

        print('these are the numbers:')
        for number in numbers:
            print(number)

        print('and these are their sums:')
        for first_number in numbers:
            for second_number in numbers:
                print(first_number + second_number)

    print_all_numbers_then_all_pair_sums([1, 2, 3, 4, 5])


def example7():

    # The space complexity of this function is O(1) because no new space is added other than 'i'
    def boooo(n):
        for i in range(0, len(n)):
            print("booooo!")
    boooo(5)

def example8():

    # The space complexity of this function is O(n) because n new elements are added
    def array_of_hi_n_times(n):
        hi_array = []
        for i in range(0, len(n)):
            hi_array[i] = 'Hi'
        return hi_array

    array_of_hi_n_times(6)

example6()
