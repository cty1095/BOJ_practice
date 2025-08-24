import sys
input = sys.stdin.readline



def preorder_traversal(root):
    if root == '.':
        return
    print(root, end='')
    left, right = tree[root]
    preorder_traversal(left)
    preorder_traversal(right)
    

def inorder_traversal(root):
    if root == '.':
        return
    left, right = tree[root]
    inorder_traversal(left)
    print(root, end='')
    inorder_traversal(right)

def postorder_traversal(root):
    if root == '.':
        return
    left, right = tree[root]
    postorder_traversal(left)
    postorder_traversal(right)
    print(root, end='')




N = int(input())
tree = {}
for _ in range(N):
    parrent, left, right = input().split()
    tree[parrent] = (left,right)

preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')
