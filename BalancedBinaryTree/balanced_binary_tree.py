"""
Kevin Ellis
Braden Harrelson
"""

import random
import string

class BalancedSearch(object):
    def __init__(self,size=16):
        self.tree = [-1 for x in range(size)]
        self.size = size
        self.root = 1
        self.items = 0
    
    """
    @Name: insert
    @Description:
        Receives an integer and inserts it into the binary tree.
    @Params:
        values (val) - a value to enter into the list
    @Returns: 
        None
    """
    def insert(self,val):
        # If list (tree) is empty, put value at root
        if self.tree[self.root] == -1:
            self.tree[self.root] = val
        # loop until you find the location to insert
        # even if you have to extend this list
        else:
            i = self.root
            loop = True
            while loop:
                if val > self.tree[i]:
                    i = self.rightChild(i)
                else:
                    i = self.leftChild(i)
                
                if i >= self.size:
                    #print(".")
                    self.extend()
                
                if self.tree[i] == -1:
                    self.tree[i] = val
                    self.items += 1
                    loop = False
                    
    """
    @Name: insertList
    @Description:
        Receives a list of unordered integers and inserts them into the binary tree in such a manner that the resulting tree is balanced.
    @Params:
        values (List) - unorderd list of integers
    @Returns: 
        None
    """
    def insertList(self,list, start, end):
        list.sort()
        #print(list)
        if len(list) % 2 == 0:
            midpos = (len(list) // 2) -1
        else:
            midpos = (len(list) // 2)
        midnum = list[midpos]
        #print(midnum)
        self.insert(midnum)
        newlistL = []
        newlistL = list[start:(midpos)]
        #print(newlistL)
        for x in range(len(newlistL)):
            self.insert(x)
        newlistR = []
        newlistR = list[midpos + 1:end + 1]
        #print(newlistR)
        for x in range(len(newlistR)):
            self.insert(x)
           
        
        
            
        
    """
    @Name: extend
    @Description:
        increases the size of the tree
    @Params: 
        None
    @Returns: 
        None
    """  
    def extend(self):
        temp = [-1 for x in range(self.size)]
        self.tree.extend(temp)
        self.size *= 2
        #print(self.items)

    """
    @Name: find
    @Description:
        searches the tree for a value
    @Params:
        values (key) - value to be searched for
    @Returns: 
        wether or not the key is in the tree
    """ 
    def find(self,key):
    
        self.comparisons = 1

        if key == self.tree[self.root]:
            return True
        else:
            i = self.root
            while True:
                if key < self.tree[i]:
                    i = self.leftChild(i)
                else:
                    i = self.rightChild(i)
                    
                if i >= self.size:
                    return False
                
                if self.tree[i] == -1:
                    return False   
                    
                if self.tree[i] == key:
                    return True
                    
                self.comparisons += 1
                
    """
    @Name: leftChild
    @Description:
        used to handle the case of a left child
    @Params:
        values (i) - index
    @Returns: 
        the new index of the child
    """           
    def leftChild(self,i):
        return 2 * i

    """
    @Name: rightChild
    @Description:
        used to handle the case of a right child
    @Params:
        values (i) - index
    @Returns: 
        the new index of the child
    """    
    def rightChild(self,i):
        return 2 * i + 1
        
random.seed(342345)
v = int(input("Please enter the amount of values to be inserted. We could only get 1-50 to work because it's not effecient. "))
bs = BalancedSearch(v)
#for x in range(1000):
    #bs.insert(random.randint(0,10))
#Create a list to hold unique integers
unique = []
#loop v times
for x in range(v):
    #get a random number
    r = random.randint(0,99999)
    #if it's not already in the list, enter it.
    if r not in unique:
        unique.append(r)
end  = len(unique) - 1 
start = 0;
bs.insertList(unique, start , end)
print("A balanced but not full tree has been created!")
