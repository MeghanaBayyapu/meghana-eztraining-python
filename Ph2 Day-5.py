#!/usr/bin/env python
# coding: utf-8

# # TREES

# In[6]:


#Types:
#Binary Tree: A node can have maximum two children

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        
node1=BinaryTreeNode(10)
node2=BinaryTreeNode(21)
node3=BinaryTreeNode(33)
node4=BinaryTreeNode(41)
node5=BinaryTreeNode(56)
node6=BinaryTreeNode(68)
node7=BinaryTreeNode(71)

node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7

print("Root node is:")
print(node1.data)

print("left child of the node is:")
print(node1.leftChild.data)

print("right child of the node is:")
print(node1.rightChild.data)

print("Root node is:")
print(node2.data)

print("left child of the node is:")
print(node2.leftChild.data)

print("right child of the node is:")
print(node2.rightChild.data)

print("Root node is:")
print(node3.data)

print("left child of the node is:")
print(node3.leftChild.data)

print("right child of the node is:")
print(node3.rightChild.data)


# # Binary Tree Traversal

# In[7]:


#Types:
#1.InOrder   -> left-root-right -LDR(root=data=D)
#2.PreOrder  -> root-left-right  -DLR
#3.PostOrder -> left-right-root -lRD


# In[1]:


#Pre,Post,Inorder of bst(Binary Search Tree)
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        #first recur on left child
        printInorder(root.left)
        #then print data of node
        print(root.val,end="")
        #now recur on right child
        printInorder(root.right)
def printPostorder(root):
     if root:
        #first recur on left child
        printPostorder(root.left)
        #now recur on right child
        printPostorder(root.right)
        #then print data of node
        print(root.val,end="")
def printPreorder(root):
    if root:
        #then print data of node
        print(root.val,end="")
        #first recur on left child
        printPreorder(root.left)
        #now recur on right child
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("PRE-ORDER")
printPreorder(root)
print()
print("POST-ORDER")
printPostorder(root)
print()
print("IN-ORDER")
printInorder(root)
print()


# In[4]:


# Implementation,insertion or creating of bst
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
# a new node with the given key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
#Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
r=insert(r, 30)
r=insert(r, 20)
r=insert(r, 40)
r=insert(r, 70)
r=insert(r, 60)
r=insert(r, 80)
inorder(r)


# In[11]:


#deletion in binary search tree

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    elif key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minValueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=deleteNode(root.left,key)
    elif key>root.key:
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root, 50)
root=insert(root, 30)
root=insert(root, 70)
root=insert(root, 20)
root=insert(root, 40)
root=insert(root, 80)
root=insert(root, 90)
print("InOrder traversal of the given tree")
inorder(root)
print("\nDelete 30")
root=deleteNode(root,30)
print("InOrder traversal of the modified tree")
inorder(root)
print("\nDelete 20")
root=deleteNode(root,20)
print("InOrder traversal of the modified tree")
inorder(root)
print("\nDelete 50")
root=deleteNode(root,50)
print("InOrder traversal of the modified tree")
inorder(root)

















# In[ ]:




