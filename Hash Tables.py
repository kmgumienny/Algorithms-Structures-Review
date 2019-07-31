def example1():
    user = {
        'age' : 54,
        'name': 'Kylie',
        'magic': True,
        'scream': "Ahhhhhhhhhhh"
    }

    print(user['age'])      # O(1)
    user['name'] = False    # O(1)
    user.pop('magic')       # O(1)
    user['spells'] = True   # O(1)
    print(user)


def example2():

    class HashTable:
        def __init__(self, size):
            self.data = [None] * size

        def hash(self, key):
            a_hash = 0
            for i in range(0, len(key)):
                a_hash = (a_hash + ord(key[i]) * i) % len(self.data)

            return a_hash

        def set(self, key, value):
            address = self.hash(key)
            if self.data[address] is None:
                self.data[address] = []
                self.data[address].append((key, value))
            return self.data

        def get(self, key):
            address = self.hash(key)
            value = self.data[address]
            return value[0][1]

        def keys(self):
            keys_array = []
            for data in self.data:
                if data is not None:
                    keys_array.append(data[0][0])
            return keys_array

    my_hash_table = HashTable(50)
    # print(my_hash_table.hash('grapes'))
    my_hash_table.set('grapes', 100000)
    my_hash_table.set('apples', 54)
    my_hash_table.set('oranges', 2)
    print(my_hash_table.get('grapes'))
    print(my_hash_table.keys())

def example3():

    def recurring_character(array):
        num_dict = dict()
        for num in array:
            if num in num_dict:
                return num
                break
            else:
                num_dict[num] = True
        return None

    # Should return 2, 1, and None respectively 
    print(recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]))
    print(recurring_character([2, 1, 1, 2, 3, 5, 1, 2, 4]))
    print(recurring_character([2, 3, 4, 5]))


example3()
