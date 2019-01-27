"""
File:tree.py
    Author: Aayush Ghimire, Date:05/2/2018, 
    Purpose: To construct a class Genome data to make a tree
    object for each organism.
    It is exported to main file phylo.py
"""
"""
This is the helper file that has the tree class. It is exported
to the phylo file.
"""
class Tree:
    """
    This class creates a instant of tree object.It initialize the
    attribute of the tree and have specific setter and getter

    PARAMETER: NONE

    RETURN: getter method has their specific return

    PRE-CONDITION: class is consructed with its attribute

    POST-CONDITION: it creates a tree object
    """
    def __init__(self):
        #initialize the atrtribute
        self._id = None
        self._left = None
        self._right = None
        self._list = None

    #stes the id
    def set_id(self,ids):
        self._id = ids

    #sets the left node of tree
    def set_left(self,ids):
        self._id = Tree(ids)

    #sets the right node of tree
    def set_right(self,ids):
        self._id = Tree(ids)

    #getter to get left node
    def get_left(self):
        return self._left

    #getter to get the right node
    def get_right(self):
        return self._right

    #joins the list after combining tree
    def join_list(self,l1,l2):
         self._list = l1 + l2

    #getter for id
    def get_id(self):
        return self._id

    #add  a list also a setter
    def add_list(self,ids):
        self._list= [ids]

    #returns a list
    def get_list(self):
        return self._list

    #checks if its leaf or not
    def is_leaf(self):
        if self._left == None and self._right == None:
            return True
        else:
            return False

    #str method of tree which prints the tree
    #this gives the output in console
    def __str__ (self):
        if self.is_leaf():
            return self.get_id()
        else:
            return ("({}, {})".format(str(self.get_left()),
                                      str(self.get_right())))
