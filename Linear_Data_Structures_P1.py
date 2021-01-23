# *===============================================
# * DESCRIPTION
# *===============================================
# File Name: Linear_Data_Structures_P1.py
# W2
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
# Variables: Application
appName = "Linear Data Structures "
appVersion = "1.0.0"
appArch = "x86&x64"
appLang = "EN"
appScriptVersion = "1.0.0"
appScriptDate = "2021.01.21"
appScriptAuthor = "KTeuton"

# *===============================================
# Misc. Variables
# *===============================================


# *===============================================

# class to create a stack
class Stacker():

    '''
    Stacker
        Allows for appending, popping and searching items to a stack. Takes the stack as input.

        AppendStack(self): Appends random numbers to a stack.

        PopStack(self): Pops items in a stack.

        ContainsStack(self): Searches items in a stack.
    '''

    # function to append items to the stack
    def AppendStack(self):
        # print the current stack
        print(f"Current Stack: {self}")
        # append to stack
        Stack.append("Testing Stack's")
        # append to stack
        Stack.append("12345")
        # append to stack
        Stack.append("6789")
        # print the appended stack
        print(f"Appended Stack: {self}")

    # function to pop items in the stack
    def PopStack(self):
        print(f"Current Stack: {self}")
        Stack.pop()
        print(f"Popped Stack: {self}")

    # function to search items in the stack
    def ContainsStack(self):
        print(f"Current Stack: {self}")
        if self in Stack:
            print(f"The Stack contains {self}.")
        else:
            print(f"The Stack does not contain {self}.")

# the stack (list)
Stack = []

# call the function to to append to the stack
Stacker.AppendStack(Stack)
# call the function to to pop the stack
Stacker.PopStack(Stack)
# call the function to search the stack
Stacker.ContainsStack("12345")

print("*********************************************")

class Queuer():

    '''
    Queuer
        Allows for appending, popping and searching items to a stack. Takes the Queue as input.

        AppendQueue(self): Appends random numbers to a Queue.

        PopQueue(self): Pops items in a Queue.

        ContainsQueue(self): Searches items in a Queue.
    '''

    # function to append items to the queue
    def AppendQueue(self):
        # print the current queue
        print(f"Current Queue: {self}")
        # append items to the queue
        Queue.append("Testing Queue's")
        # append items to the queue
        Queue.append("10111213")
        # append items to the queue
        Queue.append("141516")
        # print the current queue
        print(f"Appended Queue: {self}")

    # function to pop items in the Queue
    def PopQueue(self):
        # print the current queue
        print(f"Current Queue: {self}")
        # pop items in the queue
        Queue.pop(0)
        # print the current queue
        print(f"Popped Queue: {self}")

    # function to search items in the Queue
    def ContainsQueue(self):
        # print the current queue
        print(f"Current Queue: {self}")
        # if the queue contains the string, print that it does
        # else, print that it doesn't
        if self in Queue:
            # print the current queue
            print(f"The Queue contains {self}.")
        # else, print that it doesn't
        else:
            # print the current queue
            print(f"The Queue does not contain {self}.")

# create the queue (list)
Queue = []
# function to append items to queue 
Queuer.AppendQueue(Queue)
# function to pop items in the queue 
Queuer.PopQueue(Queue)
# function to search items to queue 
Queuer.ContainsQueue("141516")
