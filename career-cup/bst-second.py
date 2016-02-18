# Second largest element in BST

class BST(object):

    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def put(self, key, val=None):
        self = self._put(key, val, self)
        return self

    def _put(self, key, val, x):
        if x is None:
            return BST(key, val)
        if key < x.key:
            x.left = self._put(key, val, x.left)
        elif key > x.key:
            x.right = self._put(key, val, x.right)
        else:
            x.val = val
        return x

    def get(self, key):
        x = self._get(key, self)
        if x is None:
            return None
        else:
            return x.val

    def _get(self, key, x):
        if x is None:
            return None
        if key < x.key:
            return self._get(key, val, x.left)
        elif key > x.key:
            return self._get(key, val, x.right)
        else:
            return val

# reverse in-order trasversal
def bst_second_largest(root, count=0):
    if root is not None:
        count = bst_second_largest(root.right, count)
        count += 1
        if count == 2:
            print(root.key)
            return count
        count = bst_second_largest(root.left, count)
    return count

if __name__ == "__main__":
    root = BST(8)
    root.put(9)
    root.put(1)
    root.put(4)
    root.put(22)
    root.put(3)
    root.put(2)
    root.put(12)
    root.put(42)
    root.put(8)
    root.put(7)
    root.put(15)
    root.put(21)
    bst_second_largest(root)

    
