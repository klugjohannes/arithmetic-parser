import unittest

from tree import Tree


class TreeOrderTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(1)
        self.tree.left = Tree(2)
        self.tree.right = Tree(3)
        self.tree.right.left = Tree(4)
        self.tree.right.right = Tree(5)

    def test_preorder_tree(self):
        self.assertEqual(list(self.tree.preorder()), [1, 2, 3, 4, 5])

    def test_postorder_tree(self):
        self.assertEqual(list(self.tree.postorder()), [2, 4, 5, 3, 1])

    def test_inorder_tree(self):
        self.assertEqual(list(self.tree.inorder()), [2, 1, 4, 3, 5])


if __name__ == '__main__':
    unittest.main()
