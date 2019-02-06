#  Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
# For example, given the following preorder traversal:
# [a, b, d, e, c, f, g]
# And the following inorder traversal:
# [d, b, e, a, f, c, g]
# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
class BinTree():
  def __init__(self,value = None):
    self.value = value
    self.left = None
    self.right= None

  def height(self):
    if self.right is not None and self.left is not None :
      return 1 + max(self.right.height(),self.left.height()) 
    if self.right is None:
      if self.left is None:
        return 1
      return 1 + self.left.height()
    return 1 + self.right.height()
  
  def pre_order(self):
    print(self.value, end = ' ')
    if self.left:
      self.left.pre_order()
    if self.right:
      self.right.pre_order()
      
  def in_order(self):
    if self.left:
      self.left.in_order()
    print(self.value, end = ' ')
    if self.right:
      self.right.in_order()

def rcreate(pre,ino,root=None):
  root = BinTree(pre[0])
  if len(ino) is 1: 
    return root   
  newroot = pre[0]
  root.left = rcreate(pre[1:len(ino[:ino.index(newroot)+1])],ino[:ino.index(newroot)])
  root.right = rcreate (pre[len(ino[:ino.index(newroot)+1]):],ino[ino.index(newroot)+1:])
  return root

pre = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
ino = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

mytree = rcreate(pre,ino)

print ('\nPre Order:')
mytree.pre_order()
print ('\nIn order')
mytree.in_order()
print ('\nHeight: ',mytree.height())

# Output
# Pre Order:
# a b d e c f g 
# In order
# d b e a f c g 
# Height:  3