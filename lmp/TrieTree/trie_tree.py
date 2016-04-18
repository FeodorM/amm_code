class TrieTree:
    """
    Trie tree. Also called digital, radix or prefix tree.
    To create new tree just use default constructor: TrieTree()
    """

    def __init__(self, parent=None):
        """Creating new empty tree."""
        self.children = {}
        self.end = False
        self.parent = parent
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.end = True
        self._value = value

    @value.deleter
    def value(self):
        self.end = False
        self._value = None

    def __child(self, key):
        """
        Return child with given key or None if key is not in the tree

        """
        current = self
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def __setitem__(self, key, value):
        """Set self[key] to value."""
        current = self
        for char in key:
            if char not in current.children:
                current.children[char] = TrieTree(current)
            current = current.children[char]

        current.value = value

    def __getitem__(self, key):
        """Return self[key]"""
        child = self.__child(key)

        if child is None or not child.end:
            raise KeyError(key)

        return child.value

    def __delitem__(self, key):
        """Delete self[key]."""
        child = self.__child(key)

        if child is None:
            raise KeyError(key)
        del child.value

        parent = child.parent
        for char in reversed(key):
            if (not parent.children[char].children and
                    not parent.children[char].end):

                del parent.children[char]
                parent = parent.parent
            else:
                break

    def get(self, key, default=None):
        """
        T.get(key[,default]) -> T[key] if key in T, else default.
        :param default: defaults to None.

        """
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        """True if Tree has a key k, else False."""
        child = self.__child(key)
        return child.end if child is not None else False

    def anagrams(self, letters, key=''):
        result = []

        if self.end:
            result.append(key)

        for letter, child in self.children.items():
            if letter in letters:
                result.extend(
                    child.anagrams(
                        letters,
                        key + letter
                    )
                )
        return result

    def print(self, indent='...'):
        return "({})".format(self.value) + ''.join(
            '\n{indent}{name} {rest}'.format(
                indent=indent,
                name=name,
                rest=child.print(indent + '...')
            ) for name, child in self.children.items()
        )


# It's something like main function.
# This will run only if you run this module, not import it.

if __name__ == '__main__':
    # Let's create a tree!
    t = TrieTree()

    # This code reads keys from file
    with open('source.txt') as file:
        for line in file:
            t[line.strip()] = None

    # You can add new keys
    t['just_a key'] = 42
    t['spam'] = [1, 2, 3, 4]
    t['another key'] = 'spam'

    # You can get keys
    print('value with key "spam":', t['spam'])
    print("with key 'ham':", t.get('ham'), end='\n\n')

    # You can delete keys
    del t['another key']

    # You can print entire tree
    print(t.print())

    # print(t.anagrams(input('Enter something: ')))

    # uncomment line below if you wanna more help
    # help(TrieTree)

    input('Press Enter to quit...')
