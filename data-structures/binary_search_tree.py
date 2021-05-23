'''

n is used to represent the number of nodes

Time Complexity:
    - Insertion O(log n)
    - Search O(log n)

    The worse case is O(n) if the tree becomes unbalanced

Space Complexity:

    O(n)

'''

class Node:
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def insert(self, data):

        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def contains(self, data):
        if data == self.data:
            return True
        elif data <= self.data:
            if self.left is None:
                return False

            return self.left.contains(data)
        else:
            if self.right is None:
                return False

            return self.right.contains(data)

    def dfs_inorder(self):
        if self.left is not None:
            self.left.dfs_inorder()

        print(self.data)

        if self.right is not None:
            self.right.dfs_inorder()

    def dfs_preorder(self):
        print(self.data)

        if self.left is not None:
            self.left.dfs_preorder()

        if self.right is not None:
            self.right.dfs_preorder()

    def dfs_postorder(self):
        if self.left is not None:
            self.left.dfs_postorder()

        if self.right is not None:
            self.right.dfs_postorder()

        print(self.data)

    def breadth_first_search(self):
        queue = []

        queue.append(self)

        while len(queue) > 0:

            current = queue.pop(0)
            
            print(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    def height(self, node):       
        if node is None:
            return -1

        return max(self.height(node.left), self.height(node.right)) + 1


tree = Node(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)

'''
       8  
       /\
    3     10
   / \     \
  1   6     14
    / \     /
   4   7   13
'''

tree.breadth_first_search()
print(tree.height(tree))


