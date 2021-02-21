
# This is a max heap system
import random
import math
class Node(object):
    def __init__ (self, key, data, priority):
        self.key = key
        self.prio = priority
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def __str__(self):
        return "{" + str(self.key) + " , " + str(self.data) + " , " + str(self.prio)+"}"        

class Treap(object):
    
    def __init__(self):
        self.__root = None
        self.__nElems = 0
    
    # random priority number generator for balancing of Treap    
    def __randPri(self):
        return random.random()    
    
    # left rotation for node   
    def heapRotateLeft(self, node):
        temp  = node.rightChild
        node.rightChild = temp.leftChild
        temp.leftChild  = node
        return temp
    
    
    # right rotation for node
    def heapRotateRight(self, node):
        temp = node.leftChild
        node.leftChild = temp.rightChild
        temp.rightChild = node
        return temp     

    def __insert(self, node, k, d, p):
        
        # if Treap is empty (or the insert part of the recursive method)
        if not node:
            
            # increase number of elements
            self.__nElems += 1
            return Node(k, d, p)
        
        
        # if key is already in Treap
        if k == node.key:
            return node
        
        # if the key is smaller than the key of the current node
        if k < node.key:
            node.leftChild = self.__insert(node.leftChild, k, d, p)
            
            # once inserted, ensure that the priority is smaller than its parent and rotate
            if node.leftChild.prio > node.prio:
                node = self.heapRotateRight(node)  
                
        # if the key is larger than the key of the current node
        if k > node.key:
            node.rightChild = self.__insert(node.rightChild, k, d, p)
            
            # once inserted, ensure that the priority if smaller than its parent and rotate
            if node.rightChild.prio > node.prio:
                node = self.heapRotateLeft(node) 
        return node
    
    # Wrapper method for recursive insert            
    def insert(self, k, d):
        
        temp = self.__nElems
        
        # invoke a random priority for the basis of the balancing aspect of the treap
        p = self.__randPri()
        
        self.__root = self.__insert(self.__root, k, d, p)
        
        # checks if something was in fact inserted
        return temp != self.__nElems
        
    def __find(self, node, k):
        
        # if no node or node is not found in Treap
        if not node:
            return None
        
        if node.key != k:
            
            # if the key is larger than the key of the node it is compared to 
            if node.key < k:
                return self.__find(node.rightChild, k)
            
            # if the key is smaller than the key of the node it is compared to
            if node.key > k:
                return self.__find(node.leftChild, k)
        return node.data
    
    # wrapper method for find
    def find(self, k):
        return self.__find(self.__root, k)
 
    # mine that passes
    def delete(self, k): 
        
        # if the Treap is emptry return None
        if not self.__root:
            return None
        
        # set the current node to the root and keep track of the parent
        prev = None
        cur = self.__root
        
        # find the node with the correct key that needs to be deleted
        # while keeping track of the parent node
        while cur and cur.key != k:
            if cur.key < k:
                prev = cur
                cur = cur.rightChild
            elif cur.key > k:
                prev = cur
                cur = cur.leftChild
                
        # if a node with this key does not exist return False
        if not cur: return False
        
        # scenarios with the node that needs to be deleted being the root
        if cur == self.__root:
            
            # if a node has both a left and right Child
            if cur.leftChild and cur.rightChild:
                
                # must compare the priorities of the children to determine which
                # one becomes the root
                if cur.leftChild.prio <= cur.rightChild.prio:
                    
                    # switch cur and parent
                    prev = self.heapRotateLeft(cur)
                    
                    # change the root to point to parent
                    self.__root = prev 
                else:
                    
                    # if the left priority is larger than the right one
                    prev = self.heapRotateRight(cur)
                    self.__root = prev
                    
            # if there is only a left child
            elif cur.leftChild and not cur.rightChild:
                prev = self.heapRotateRight(cur)
                self.__root = prev
                
                # ensure that the right child of the parent is pointing to cur
                prev.rightChild = cur
            
            # if there is only a right child
            elif cur.rightChild and not cur.leftChild:
                prev = self.heapRotateLeft(cur)
                self.__root = prev
                
                # ensure that the left child of the parent is pointing to cur
                prev.leftChild = cur
            else:
                
                # return the data of the root because that is the only node in the Treap
                # so the root is deleted
                temp = cur.data
                self.__root = None
                return temp        
        
        # same scenarios as before but with cur not as root node
        # rotate until the node becomes a leaf node
        while cur.leftChild or cur.rightChild:
            
            # parent has only left child
            if cur.leftChild and not cur.rightChild:
                
                # check if cur is the parents right or left child and assign
                # the correct side of the parent to the child
                if prev.leftChild == cur:
                    prev.leftChild = self.heapRotateRight(cur)
                    prev = prev.leftChild
                else:
                    prev.rightChild = self.heapRotateRight(cur)
                    prev = prev.rightChild
                    
            # parent only has right child
            elif cur.rightChild and not cur.leftChild:
                
                # check if cur is the parents right or left child and assign
                # the correct side of the parent to the child                
                if prev.rightChild == cur:
                    prev.rightChild = self.heapRotateLeft(cur)
                    prev = prev.rightChild
                else:
                    prev.leftChild = self.heapRotateLeft(cur)
                    prev = prev.leftChild
            
            # if cur has both children
            elif cur.leftChild and cur.rightChild:
                
                    # compare priorities of children to rotate the correct way
                    if cur.leftChild.prio <= cur.rightChild.prio:
                        
                        # check if cur is the parents right or left child and assign
                        # the correct side of the parent to the child                        
                        if prev.rightChild == cur:
                            prev.rightChild = self.heapRotateLeft(cur)
                            prev = prev.rightChild
                        else:
                            prev.leftChild = self.heapRotateLeft(cur)
                            prev = prev.leftChild
                    
                    else:
                        
                        # check if cur is the parents right or left child and assign
                        # the correct side of the parent to the child                        
                        if prev.rightChild == cur:
                            prev.rightChild = self.heapRotateRight(cur)
                            prev = prev.rightChild
                        else:
                            prev.leftChild = self.heapRotateRight(cur)
                            prev = prev.leftChild
        
        # after rotating and the node is a leaf node
        # keep the data
        temp = cur.data
        
        # delete the child by ensuring the parents correct side now points to none
        # instead of to the node being deleted
        if prev.leftChild == cur:
            prev.leftChild = None
        else:
            prev.rightChild = None
        cur = None
        
        # return the data
        return temp    
    
    
    # just returns the priority of the root node
    def getMaxPrio(self):
        cur = self.__root
        return cur.prio
    
    # wrapper method to print the way the tree looks
    def printTreap(self):
        self.pTreap(self.__root, "ROOT:  ", "")
        print()
    
    # method to print the tree    
    def pTreap(self, n, kind, indent):
        print("\n" + indent + kind, end="")
        if n: 
            print(n, end="")
            if n.leftChild:
                self.pTreap(n.leftChild,  "LEFT:   ",  indent + "    ")
            if n.rightChild:
                self.pTreap(n.rightChild, "RIGHT:  ", indent + "    ")  
                
   
    # checks the tree property that all left children are smaller than their parent
    # and all right children are larger than their parents
    def __checkTreeProp(self, cur):
        if cur:
            if cur.rightChild:
                if cur.key >= cur.rightChild.key:
                    return False 
                if cur.key < cur.rightChild.key:
                    return self.__checkTreeProp(cur.rightChild)
            if cur.leftChild:
    
                if cur.key < cur.leftChild.key:
                    return False
                
                if cur.key >= cur.leftChild.key:
                    return self.__checkTreeProp(cur.leftChild)
            
        return True
    
    # wrapper method for tree property
    def checkTreeProp(self):
        return self.__checkTreeProp(self.__root)
    
    
    # check heap property that every priority of the child is smaller than its
    # parents
    def __checkHeapProp(self, cur):
        if cur.rightChild:
            if cur.rightChild.prio <= cur.prio:
                return self.__checkHeapProp(cur.rightChild)
            return False
        if cur.leftChild:
            if cur.leftChild.prio <= cur.prio:
                return self.__checkHeapProp(cur.leftChild)
            return False
        return True
    
    # wrapper method for heap property
    def checkHeapProp(self):
        return self.__checkHeapProp(self.__root)    
                
            
    
        
def __main():
    T = Treap()
    for i in range(1, 10):
        T.insert(i, "lk"* i)
    T.printTreap()
    print(T.find(3))
    for i in range(1, 5):
        T.delete(i)  
    for i in range(1, 10):
        print(T.find(random.randint(1, 10)))
        
    T.printTreap()
if __name__ == '__main__':
    __main()
                  