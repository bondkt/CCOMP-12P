# *===============================================
# * DESCRIPTION
# *===============================================
# File Name: Linear_Data_Structures_P2.py
# W3
# CCOMP-12P
# Spring 2021
# *===============================================

# *===============================================
# * LIBS
# *===============================================


# *===============================================

# *===============================================
# * LICENSE_INFO
# *===============================================

# If I had license info, it would go here...

# *===============================================

# *===============================================
# * VARIABLE DECLARATION
# *===============================================
## Variables: Application
appName = "Linear Data Structures P2"
appVersion = "1.0.0"
appArch = "x86&x64"
appLang = "EN"
appScriptVersion = "1.0.0"
appScriptDate = "2021.02.06"
appScriptAuthor = "Kyle Teuton"

# *===============================================
## Misc. Variables
# *===============================================

# *===============================================

# NOTE: Lots of code taken from the below URLs:
# LINK https://www.youtube.com/watch?v=JlMyYuY1aXU
# LINK https://repl.it/@JoeManlove/LinkedList#main.py

# ANCHOR node Class
# Class to create nodes


class node:
    '''
    Node
    Allows for creation of nodes.

    __init__(self, contents, next_node=None): creates a node, sets the next node equal to none.

    __repr__(self): returns the node representation in string format
    '''
    # default node constructor function
    # used to create a node
    # takes self, contents (aka data) and takes a next and sets it to none
    def __init__(self, data=None, next=None):
        # set the data of the node to equal the data being passed in
        self.data = data
        # set the next node to equal the variable being passed in - none
        self.next = next

    # default node constructor function
    # learned from: https://www.journaldev.com/22460/python-str-repr-functions
    def __repr__(self):
        # returns the content ofn the object being passed as a string.
        return f"This node contains {self.data}."

# ANCHOR LinkedList Class
# Class to create a linkedlist
class linked_list:
    '''
    LinkedList

    __init__(self, data=[]): default constructor to create a linked list

    append_right(self, data): adds a new node to right of the current head node

    append_left(self, data): adds a new node to left of the current head node

    pop_left(self): pops the node to the left of the current head

    pop_right(self): pops the node to the right of the current head

    contains(self, data): searches the linkedlist for similar data

    display_ll(self): prints the linked list
    '''

    # default constructor to create a linked list
    # takes self and data as input. if data isn't supplied, will proceed with an empty list.
    def __init__(self, data=[]):
        # set the head equal to None
        self.head = None

    # Append right function. Appends data to the right of the linked list.
    # takes self and data as input
    def append_right(self, data):
        # create a new node, passing the data that was passed from in
        new_node = node(data)
        # if the head is equal to none
        if self.head == None:
            # set the head to equal the newly created node
            self.head = new_node
        # else...
        else:
            # set the current node to be the head
            cur = self.head
            # while the current nodes next value is not equal to none
            while cur.next != None:
                # advanced the current node to the node
                cur = cur.next
            # once out of the while loop, set the current node to be the newly created node
            cur.next = new_node

    # Append left function. Appends data to the left of the linked list.
    # takes self and data as input
    def append_left(self, data):
        # create a new node, and ensure it has a head property
        new_node = node(data, self.head)
        # set the newly created node as the head
        self.head = new_node

    # pop left function. pops the left node in the linked list
    # takes self input
    def pop_left(self):
        # set the current node to the head
        cur = self.head
        # sets the head to the next node in the list
        self.head = cur.next

    # pop right function. pops the right node in the linked list
    # takes self input
    def pop_right(self):
        # set the previous node equal to none
        prev_node = None
        # set the current node to the head, to start at the begining of the linked list
        cur_node = self.head
        # while the current nodes next value is not equal to none
        while cur_node.next != None:
            # set the previous node to the current node (for tracking)
            prev_node = cur_node
            # advanced to the next node
            cur_node = cur_node.next
        # if the current node is ever equal to none, we have reached the end of the list
        if cur_node.next == None:
            # set the previous node equal to none, the new tail.
            prev_node.next = None

    # contains function. searches the linked list.
    # takes self and data as input
    def contains(self, data):
        # set the head as the current node
        cur_node = self.head
        # if the head is none, the list isd empty
        if self.head == None:
            # let the user know the list is empty
            print("Linked List is empty.")
            # return
            return
        # while the current node is not equal to none
        while cur_node != None:
            # if the data matches the data in the current node, we have a match
            if data == cur_node.data:
                # let the user know the list contains what they are looking for
                print(f"The Linked List contains: {data}")
                # break out of the while loop
                break
            # else...
            else:
                # advanced the curerent node to the next node in the linked list
                cur_node = cur_node.next
        # if the current not is not one (tail)
        if cur_node == None:
            # let the user know the linked list doesn't have a match to what they are looking for
            print(f"The Linked List does not contain: {data}")
    
    # display_ll function. prints the linked list.
    # takes self as input
    def display_ll(self):
        # if the head is none, the list isd empty
        if self.head == None:
            # let the user know the list is empty
            print("Linked List is empty.")
            # return
            return
        # crete an empty list
        elems_list = []
        # set the head of the linked list as the current node
        cur_node = self.head
        # advance through the linked list
        while cur_node != None:
            # appends the data in each node to the list
            elems_list.append(cur_node.data)
            # advances the current node to the next node
            cur_node = cur_node.next
        # prints out the linked list
        print(elems_list)


# ANCHOR Main
# determine if this script is being called by itself or imported. Only execute if it is not being imported.
# learned from: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    # create an empty empty list
    test_list = linked_list()
    # add data to the list by appending right
    print("Creating linked list (append right):")
    # add data to the list
    test_list.append_right(1)
    # add data to the list
    test_list.append_right(2)
    # add data to the list
    test_list.append_right(3)
    # add data to the list
    test_list.append_right(4)
    # add data to the list
    test_list.append_right(5)
    # display the linked list
    test_list.display_ll()
    print("Append left:")
    test_list.append_left(0)
    # display the linked list
    test_list.display_ll()
    # pop the left node in the list
    print("Popping left:")
    test_list.pop_left()
    # display the linked list
    test_list.display_ll()
    # pop the right node in the list
    print("Popping right:")
    test_list.pop_right()
    # display the linked list
    test_list.display_ll()
    # search the linked list for 7 and 3
    print("Searching for numbers...")
    test_list.contains(7)
    test_list.contains(3)

