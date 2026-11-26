class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def level_order(self, rt):
        if rt is None:
            print("bst is empty")
            return

        arr = [rt]
        cnt = 0
        level = 0

        while cnt < len(arr):
            node_count = len(arr) - cnt
            print(f"\nlevel no : {level} --> ", end="")
            for _ in range(node_count):
                temp = arr[cnt]
                cnt += 1
                print(temp.data, end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level += 1

    def countleaf(self, rt):
        if rt is None:
            return
        self.countleaf(rt.left)
        if rt.left is None and rt.right is None:
            self.count += 1
        print(rt.data, end=" ")
        self.countleaf(rt.right)

    def countnleaf(self, rt):
        if rt is None:
            return
        self.countnleaf(rt.left)
        if rt.left is not None or rt.right is not None:
            self.count += 1
        print(rt.data, end=" ")
        self.countnleaf(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    def findminmax(self, rt):
        if rt is None:
            return
        temp = rt
        while temp.left:
            temp = temp.left
        print("\nMin :", temp.data)

        temp = rt
        while temp.right:
            temp = temp.right
        print("\nMax :", temp.data)

    def deletenode(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.deletenode(rt.left, val)
        elif val > rt.data:
            rt.right = self.deletenode(rt.right, val)
        else:
            # Case 1 & 2: 0 or 1 child
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left

            # Case 3: 2 children -> replace with inorder successor
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.deletenode(rt.right, succ.data)

        return rt

    def get_successor(self, temp):
        temp = temp.right
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp

    def search(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False


b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))

print("Inorder : ")
b1.inorder(b1.root)

print("\nPreorder : ")
b1.preorder(b1.root)

print("\nPostorder : ")
b1.postorder(b1.root)

b1.findminmax(b1.root)

b1.root = b1.deletenode(b1.root, 4)
print("\nInorder after delete : ")
b1.inorder(b1.root)

b1.root = b1.deletenode(b1.root, 65)
print("\nInorder after delete : ")
b1.inorder(b1.root)

b1.root = b1.deletenode(b1.root, 450)
print("\nInorder after delete : ")
b1.inorder(b1.root)

b1.count = 0
b1.countleaf(b1.root)
print("\ntotal number of leaf nodes :", b1.count)

b1.count = 0
b1.countnleaf(b1.root)
print("\ntotal number of non leaf nodes :", b1.count)

if b1.search(50):
    print("\nfound the node")
else:
    print("\nnot found")

print("\nLevel order :")
b1.level_order(b1.root)