N = int(input())
tree = {} # 트리 생성

for _ in range(N): # 부모, 왼쪽자식, 오른쪽자식 저장
    root, left, right, = input().split()
    tree[root] = (left, right)

def preorder(node):
    if node == '.': # 자식이 없으면 종료
        return
    print(node, end = '') # 루트
    preorder(tree[node][0]) # 왼쪽 자식
    preorder(tree[node][1]) # 오른쪽 자식

def inorder(node):
    if node == '.':
        return
    
    inorder(tree[node][0])
    print(node, end = '')
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
