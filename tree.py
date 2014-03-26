class Tree(object):
    """ a simple iterable binary tree implementation """

    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def inorder(self):
        if self.left is not None:
            for tree in self.left.inorder():
                yield tree

        yield self.value

        if self.right is not None:
            for tree in self.right.inorder():
                yield tree

    def preorder(self):
        yield self.value

        if self.left is not None:
            for i in self.left.preorder():
                yield i

        if self.right is not None:
            for i in self.right.preorder():
                yield i

    def postorder(self):
        if self.left is not None:
            for tree in self.left.postorder():
                yield tree

        if self.right is not None:
            for tree in self.right.postorder():
                yield tree

        yield self.value
