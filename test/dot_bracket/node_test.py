import unittest
from rnastructure import dot_bracket as dbp


class NodeTest(unittest.TestCase):

    def test_empty_loop(self):
        node = dbp.Node()
        node.append(dbp.Node())
        ans = tuple()
        val = node.loop()
        self.assertEqual(val, ans)

    def test_simple_loop(self):
        node = dbp.Node()
        node.append(('.', 1))
        node.append(('.', 2))
        ans = tuple([[1, 2]])
        val = node.loop()
        self.assertEqual(val, ans)

    def test_internal_loop(self):
        node = dbp.Node()
        node.append(dbp.Node())
        node.append(('.', 1))
        node.append(('.', 2))
        node.append(dbp.Node())
        node.append(dbp.Node())
        node.append(('.', 3))
        ans = tuple([[1, 2], [3]])
        val = node.loop()
        self.assertEqual(val, ans)

    def test_outer_loop(self):
        node = dbp.Node()
        node.append(('.', 1))
        node.append(('.', 2))
        node.append(dbp.Node())
        node.append(('.', 3))
        ans = tuple([[1, 2], [3]])
        val = node.loop()
        self.assertEqual(val, ans)

    def test_junction_loop(self):
        node = dbp.Node()
        node.append(dbp.Node())
        node.append(('.', 1))
        node.append(('.', 2))
        node.append(dbp.Node())
        node.append(dbp.Node())
        node.append(('.', 3))
        node.append(('.', 4))
        node.append(('.', 5))
        node.append(dbp.Node())
        node.append(dbp.Node())
        node.append(('.', 6))
        node.append(('.', 7))
        ans = tuple([[1, 2], [3, 4, 5], [6, 7]])
        val = node.loop()
        self.assertEqual(val, ans)

    # def test_get_pseudo(self):
    #     node = dbp.Node()
    #     node.append(dbp.Node())
    #     node.append(('{', 1))
    #     node.append(('{', 2))
    #     node.append(('{', 3))
    #     node.append(dbp.Node())
    #     node.append(('}', 4))
    #     node.append(('}', 5))
    #     node.append(('}', 6))
    #     ans = tuple([[1, 2, 3], [4, 5, 6]])
    #     val = node.get_pseudoknot()
    #     self.assertEqual(val, ans)
