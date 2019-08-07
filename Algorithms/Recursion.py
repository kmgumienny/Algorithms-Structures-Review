# Use a debugger with this example to better understand what's happening
def example1():
    counter = 0

    def inception(value):
        if value > 3:
            return 'Done!'
        else:
            value += 1
            return inception(value)

    print(inception(counter))


def example2():

    def recursive_factorial(value):
        if value == 1:
            return 1
        else:
            return value * recursive_factorial(value - 1)

    def iterative_factorial(value):
        total = 1
        for i in range(value, 0, -1):
            total = total * i
        return total

    print(recursive_factorial(5))
    print(iterative_factorial(5))


def example3():

    # This is O(n)
    def fibonacci_recursive(n):
        if n < 2:
            return n
        else:
            return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

    # This is O(2^n). Yikes!
    def fibonacci_iterative(n):
        arr = [0, 1]
        for i in range(2, n + 1):
            arr.append(arr[i-1] + arr[i-2])
        return arr[len(arr) - 1]

    # Should get 21
    print(fibonacci_recursive(8))
    print(fibonacci_iterative(8))


# example1()
# example2()
example3()
