#!/bin/python3

import sys
from collections import defaultdict

p = 0


# build BST
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        self.print_node(self.root)
        return super().__repr__()

    def get_root(self):
        return self.root

    def insert_node(self, v1, v2):
        if self.root is None:
            if v1 == 1:
                self.root = Node(v1)
            elif v2 == 1:
                self.root = Node(v2)
        inserted = self._insert(self.root, v1, v2)
        if not inserted:
            print("insert val", v1, v2, "failed")

    def _insert(self, node, v1, v2):
        if node.v == v1:
            if node.l is None:
                # print("add left node", v2)
                node.l = Node(v2)
                return True
            elif node.r is None:
                # print("add right node", v2)
                node.r = Node(v2)
                return True
            else:
                print("Node with val %d is full!" % node.v)
                return False
        else:   # DFS?
            # print("milk node v", node.v, v1, v2)
            inserted = False
            if node.l is not None:
                inserted = self._insert(node.l, v1, v2)
                if not inserted:
                    if node.r is not None:
                        inserted = self._insert(node.r, v1, v2)
            return inserted

    # def bfs_and_count(self, node, c):
    #     if node is not None:
    #         if node.l is not None


    def print_node(self, node):
        if node is not None:
            # print("node", node.v)
            if node.l:
                print("node", node.v, "has left node", node.l.v)
            if node.r:
                print("node", node.v, "has right node", node.r.v)
            self.print_node(node.l)
            self.print_node(node.r)


    def compute_prob_factor(bst, e):   # by BFS
        x = 0
        p_factor = 1
        queue = [bst[1]]
        while queue:
            x += p_factor * len(queue)
            path = queue.pop(0)
            if path in bst:
                queue =


        x += p_factor * len(root_lvl)
        for v in root_lvl:
            if v in bst:
                p_factor += 1




if __name__ == "__main__":
    # bst = BST()
    bst = defaultdict(list)

    n = int(input().strip())
    e = n - 1
    for a0 in range(n-1):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        bst[x].append(y)

        # bst.insert_node(int(x), int(y))


    print(bst)
