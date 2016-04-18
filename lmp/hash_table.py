class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return "Person {self.name}{self.address}".format(self=self)


class HashTable:
    def __init__(self, size=100):
        self.size = self.closest_prime(size)
        self.hash = lambda key: key % self.size
        self.table = [[] for _ in range(self.size)]

    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num // 2):
            if not num % i:
                return False
        return True

    @staticmethod
    def closest_prime(num):
        while True:
            if HashTable.is_prime(num):
                return num
            else:
                num += 1

    def __setitem__(self, key, value):
        self.table[self.hash(key)].append(value)

    def __getitem__(self, key):
        value = self.table[self.hash(key)]
        if not len(value):
            raise KeyError(key)
        elif len(value) == 1:
            return value[0]
        return value

if __name__ == '__main__':
    h = HashTable()
    h[12412] = Person('Fedor', 'VF 138')
    print(h[12412])
