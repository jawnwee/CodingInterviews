from Tree import Tree
from Stack import Stack

stck = Stack()
paths = []

def find_sum_path(current_path, current_sum, goal, currentDepth=0):
  if stck.isEmpty():
    return 'Complete'
  top = stck.pop()
  if len(current_path) > currentDepth:
    current_path[currentDepth] = top.data
    current_path = current_path[:currentDepth+1]
    current_sum = 0
    for i in current_path:
      current_sum += i
  else:
    current_path.append(top.data)
    current_sum += top.data
  if current_sum == goal:
    print current_path
  currentDepth += 1
  if top.left != None:
    stck.push(top.left)
    find_sum_path(current_path, current_sum, goal, currentDepth)
  if top.right != None:
    stck.push(top.right)
    find_sum_path(current_path, current_sum, goal, currentDepth)

def path_to_sum(root):
  if root == None:
    return 'Cannot pass in empty tree'
  stck.push(root)
  result_list = find_sum_path([], 0, 12)

one = Tree(1)
three = Tree(3)
four = Tree(4)
five = Tree(5)
six = Tree(6)
seven = Tree(7)
eight = Tree(8)

five.left = three
five.right = seven

three.right = four
three.left = one

seven.left = six
seven.right = eight

