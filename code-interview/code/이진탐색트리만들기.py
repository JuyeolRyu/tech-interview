'''
이진탐색트리 만들기
'''
class Node():
  def __init__(self,n):
    self.val = n
    self.left = None
    self.right = None

def makeTree(l,r):
  m = (l+r)//2
  if l == r:
    return;
  newNode = Node(arr[m])
  leftChild = makeTree(l,m)
  rightChild = makeTree(m+1,r)
  newNode.left = leftChild
  newNode.right = rightChild
  return newNode
arr = [1,2,3,4,5,6,7,8,9]
mid = len(arr)//2
tree = makeTree(0,len(arr))
print(tree.right.left.val)