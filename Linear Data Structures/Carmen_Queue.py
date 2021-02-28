# *===============================================
# * DESCRIPTION
# *===============================================
# File Name: Carmen_Queue.py
# CCOMP-12P
# Spring 2021
# *===============================================

# *===============================================
# * LIBS
# *===============================================

# from time import perf_counter (nanoseconds)
from time import perf_counter_ns

# from random import random
from random import choice

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
appName = "Carmen Queue"
appVersion = "1.0.0"
appArch = "x86&x64"
appLang = "EN"
appScriptVersion = "1.0.0"
appScriptDate = "2021.02.27"
appScriptAuthor = "KTeuton"

# *===============================================
## Misc. Variables
# *===============================================

# lists for testing
list_1 = [1, 2, 3, "Carmen Sandiego", 5]
list_2 = [1, 2, 3, 4, 5]
list_3 = [1, 2, "Carmen Sandiego", "Carmen Sandiego", 5, "Carmen Sandiego"]

# create a list of the lists to be selectable
# learned from: https://stackoverflow.com/questions/43647640/pick-random-value-from-multiple-lists-with-equal-probability
# also learned from: https://stackoverflow.com/questions/47372712/how-to-import-random-so-i-can-use-random-choice-in-my-function
lists = choice([list_1, list_2, list_3])

# *===============================================

class Queuer():

    '''
    Queuer
        Allows for appending, popping and searching items to a stack. Takes the Queue as input.

        AppendQueue(self): Appends random numbers to a Queue.

        PopQueue(self): Pops items in a Queue.

        ContainsQueue(self): Searches items in a Queue.
    '''

    def __init__(self, datain=[]):
        # set the data of the node to equal the data being passed in
        self.data = datain

    # function to append items to the queue
    def AppendQueue(self, datain):
        self.data.append(datain)

    # function to pop items in the Queue
    def PopQueue(self):
        self.data.pop(0)

    def __contains__(self, datain):
        return datain in self.data

    def __iter__(self):
        return self.data.__iter__()
        #return self

    def __repr__(self):
        return self.data.__repr__()

# Carueue class
# takes a queue as input

    '''
    Carueue
        searches for words that are passed to it in any queue, 

        finder(self): searches the queue for words being passed in
    '''
class Carueue(Queuer):
    def __init__(self, queuein):
        super().__init__(queuein)

    # finds words in the queue
    # takes self and the word in as arguments
    def finder(self, searchword):
        # for each element in the queue...
        for index, element in enumerate(self.data):
            # see if the element matches the search word
            if (element == searchword):
                # if it matches the search word, print that it exists in the queue
                # learned from: https://www.techiedelight.com/find-all-occurrences-item-python-list/
                print(f"Carmen was found in index: {index}")
                # the code below works but not if there are multiples of the search word (the index doesn't advance correctly)
                #print(f"Carmen was found in index: {self.data.index(element)}")


# ANCHOR Main
# determine if this script is being called by itself or imported. Only execute if it is not being imported.
# learned from: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    # create the queue (list)
    Q1 = Queuer([1, 2, 3, "Carmen Sandiego", 5])

    # function to append items to queue
    Q1.AppendQueue(6)

    # print the current queue
    print(f"Creating Queue: {Q1}")

    # function to pop items in the queue
    Q1.PopQueue()

    # print the current queue
    print(f"Popped Queue: {Q1}")

    # function to search items to queue
    print("Is 3 in the Queue?")
    print(3 in Q1)
    
    # create the list to be passed
    CarFinder = Carueue(lists)
    
    # Start the counter 
    t1_start = perf_counter_ns() 

    # call the finder function to search for carmen
    CarFinder.finder("Carmen Sandiego")

    # Stop the counter 
    t1_stop = perf_counter_ns() 

    # timer function learned from: https://www.geeksforgeeks.org/time-perf_counter-function-in-python/
    print("Elapsed time (nanoseconds):", t1_stop-t1_start) 

    # debug
    #for element in Q1:
    #    print(element)
