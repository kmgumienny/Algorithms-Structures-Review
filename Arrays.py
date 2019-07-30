

def example1():

    def simple_array():
        # This uses up 16 bytes of storage because 4 items x 4 bytes each
        # They are stores sequentially
        strings = ['a', 'b', 'c', 'd']

        # static arrays are defined upon initialization
        # in C++ it would be defined as int array[20]
        print(strings[2])

        # Push operation
        strings.append('e')     # O(1)
        # Pop operation
        strings.pop(4)          # O(1)
        # Add to the beginning
        strings.insert(0, '1')  # O(n) because everything has to shift over
        # Delete from the end
        strings.remove('1')     # O(n) because everything has to shift back over

        print(strings)

    simple_array()

def example2():

    class my_array:

        def __init__(self):
            self.length = 0
            self.data = {}

        def get(self, index):
            return self.data[index]

        def push(self, item):
            self.data[self.length] = item
            self.length += 1

        def pop(self):
            last_item = self.data[self.length - 1]
            self.data.popitem()
            self.length -= 1
            return last_item

        def delete(self, index):
            item = self.data[index]
            self.shift_items(index)

        def shift_items(self, index):
            for i in range(index, self.length-1):
                self.data[i] = self.data[i+1]
            self.data.popitem()
            self.length -= 1

    new_array = my_array()
    new_array.push("hi")
    new_array.push("you")
    new_array.push('!')
    # new_array.pop()
    # new_array.pop()
    new_array.delete(0)
    new_array.delete(1)
    new_array.push("are")
    new_array.push("nice")
    print(new_array.data)


def example3():

    def reverse_string(string):
        if len(string) < 2 or isinstance(string, str):
            return "Not a string"
        reverse = []
        for letter in string[::-1]:
            reverse.append(letter)
        return reverse

    print(reverse_string("Hi my name is Kamil"))

example3()