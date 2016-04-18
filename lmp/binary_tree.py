class BinaryTree:
    class Node:
        """Binary tree node"""
        def __init__(self, key):
            self.key = key
            self.left = self.right = None

        def __str__(self):
            res = []
            if self.left is not None:
                res.append(str(self.left))
            res.append(str(self.key))
            if self.right is not None:
                res.append(str(self.right))
            return ' '.join(res)

    def __init__(self):
        """Creating new empty tree"""
        self.root = None

    def __current_and_parent(self, key):
        """
        Return node with given :param key: and its parent
        :return: (current, parent)
        """
        parent = None
        current = self.root
        while current is not None and current.key != key:
            parent = current
            if current.key > key:
                current = current.left
            else:
                current = current.right

        return current, parent

    def insert(self, key):
        """
        Add an element to a tree.

        This has no effect if the element is already present.

        """
        current, parent = self.__current_and_parent(key)

        if current is not None:
            return

        if parent is None:
            self.root = self.Node(key)
            return

        if parent.key > key:
            parent.left = self.Node(key)
        else:
            parent.right = self.Node(key)

    def remove(self, key):
        """
        Remove an key from a tree; it must be in the tree.

        If the key is not in the tree, raise a KeyError.

        """
        current, parent = self.__current_and_parent(key)

        if current is None:
            raise KeyError(key)

        if current.left is None or current.right is None:
            if current.left is None:
                current = current.right
            else:
                current = current.left

            if parent is None:
                self.root = current
            elif parent.key > key:
                parent.left = current
            else:
                parent.right = current
        else:
            for_del = current.right
            while for_del.left is not None:
                for_del = for_del.left
            new_key = for_del.key
            self.remove(new_key)
            current.key = new_key

    def __str__(self):
        return str(self.root)

    def __contains__(self, key):
        return self.__current_and_parent(key)[0] is not None

    def __iter__(self):
        return iter(str(self).split())


def test():
    from random import randint
    from tqdm import tqdm
    for test_num in tqdm(range(10000)):
        a = BinaryTree()
        for i in range(50):
            a.insert(randint(0, 100))
        r = randint(0, 100)
        try:
            a.remove(r)
        except KeyError:
            pass
        finally:
            assert r not in a, test_num

        str_a = str(a)
        list_a = [int(x) for x in str(a).split()]
        list_a.sort()
        assert str_a == ' '.join([str(x) for x in list_a]), test_num
    print('passed')

if __name__ == '__main__':
    test()
