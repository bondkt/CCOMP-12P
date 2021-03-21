# *===============================================
# * DESCRIPTION
# *===============================================
# File Name: midterm.py
# CCOMP-12P
# Spring 2021
# *===============================================

# *===============================================
# * LIBS
# *===============================================

# from random import the randint function
import random
#from random import randint

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
appName = "midterm"
appVersion = "1.0.0"
appArch = "x86&x64"
appLang = "EN"
appScriptVersion = "1.0.0"
appScriptDate = "2021.03.07"
appScriptAuthor = "Kyle Teuton"

# *===============================================
## Misc. Variables
# *===============================================

# sign cycle time (in seconds)
sign_show_duration = 20

# student read sign start time
# minimum read time a student has to read the signs
stud_read_start_time = 55

# student read sign end time
# minimum read time a student has to read the signs
stud_read_end_time = 65

# number of signs being shown
num_signs = 20

# days per week that all students attend school
days_per_week = 4

# # of students attending class that week
num_students = 5

# list of  all students
students_roster = []

# *===============================================

# NOTE: Lots of code taken from the below URLs:
# LINK https://www.youtube.com/watch?v=JlMyYuY1aXU
# LINK https://repl.it/@JoeManlove/LinkedList#main.py
# LINK https://www.javatpoint.com/python-program-to-create-and-display-a-circular-linked-list

# ANCHOR create_student
# Class to create a student
class create_student:
    '''
    create_student
    Allows for creation of students.

    __init__(self, sign_show_duration): creates a student object with various properties.

    ssigns_seen(self, sign): adds the passed in signs to the students seen list
    '''
    # default student constructor function
    # creates students
    def __init__(self, sign_show_duration):
        # set the students signs seen to none
        self.student_signs_seen = []

        # set the start time list to none
        self.start_time_list = []

        # assign a student name by count up +1 per student
        stud_name = "Student " + str(sign_show_duration)
        # set the name to the student name previous generated
        self.name = stud_name
        # set the students read duration to a random amount depending on the variables stud_read_start_time and stud_read_end_time
        self.read_duration = random.randint(stud_read_start_time, stud_read_end_time)

        # for the schooldays in a range between 0 and the days_per_week.
        for schooldays in range(0, days_per_week):
            # append the the daily start time to the student
            self.start_time_list.append(random.randint(1, 86400))
            # sort the start times..for ease of reading
            self.start_time_list.sort()
    
    # signs seen function
    # appends the signs seen to the student, for tracking
    def signs_seen(self, sign):
        # appends the signs seen to the student
        self.student_signs_seen.append(sign)

# ANCHOR node
class node:
    '''
    Node
    Allows for creation of nodes.

    __init__(self, datan=None, nxt_node=None): creates a node, sets the next node equal to none.

    __repr__(self): returns the node representation in string format
    '''
    # default node constructor function
    # used to create a node
    # takes self, contents (aka data) and takes a next and sets it to none
    def __init__(self, datan=None, nxt_node=None):
        # set the data of the node to equal the data being passed in
        self.datan = datan
        # set the next node to equal the variable being passed in, otherwise set to none
        self.nxt_node = nxt_node

    # default node constructor function
    # learned from: https://www.journaldev.com/22460/python-str-repr-functions
    def __repr__(self):
        # returns the content ofn the object being passed as a string.
        return f"This node contains {self.datan}."

# ANCHOR Circular LinkedList Class
# Class to create a linkedlist
class c_linked_list:
    '''
    create_student

    __init__(self): default constructor to create a circular linked list

    append_right(self, data): adds a new node to right of the current head node

    contains(self, data): searches the circular linked list for similar data

    display_ll(self): prints the circular linked list
    '''

    # default constructor to create a linked list
    # takes self and data as input. if data isn't supplied, will proceed with an empty list.
    def __init__(self):
        # set the head equal to None
        self.head = node(None)

        # set the tail to None
        self.tail = node(None)

        # set the head's next node to be the tail
        self.head.nxt_node = self.tail   

        # set the tail's next node to be the head
        self.tail.nxt_node = self.head  

    # Append right function. Appends data to the right of the linked list.
    # takes self and data as input
    def append_right(self, data):
        # create a new node, passing the data that was passed from in
        new_node = node(data)

        # if the head is equal to none
        if self.head.datan is None:
            # set the head to equal the newly created node
            self.head = new_node
            # set the tail to equal the newly created node
            self.tail = new_node   
            # set the next node of the new node to the head 
            new_node.nxt_node = self.head
        # else...
        else:
            # set the tail's next node to be the new node
            self.tail.nxt_node = new_node
            # set the tail to be the new node
            self.tail = new_node
            # set the tail's next node to be the head
            self.tail.nxt_node = self.head

    # contains function. searches the linked list.
    # takes self and data as input
    def contains(self, data):
        # set the head as the current node
        current_node = self.head
        # if the head is none, the list isd empty
        if self.head == None:
            # let the user know the list is empty
            print("Linked List is empty.")
            # return
            return
        # while the current node is not equal to none
        while current_node.nxt_node != self.head:
            # if the data matches the data in the current node, we have a match
            if data == current_node.datan:
                # let the user know the list contains what they are looking for
                print(f"The Linked List contains: {data}")
                # break out of the while loop
                break
            # else...
            else:
                # advanced the curerent node to the next node in the linked list
                current_node = current_node.nxt_node
        # if the current not is not one (tail)
        if current_node == None:
            # let the user know the linked list doesn't have a match to what they are looking for
            print(f"The Linked List does not contain: {data}")
    
    # display_ll function. prints the linked list.
    # takes self as input
    def display_ll(self):
        # set the head of the linked list as the current node
        current_node = self.head

        # if the head is none, the list isd empty
        if self.head == None:
            # let the user know the list is empty
            print("Linked List is empty.")
            # return
            return
        else:
            # create an empty list
            elems_list = []
            # advance through the linked list
            while current_node.nxt_node != self.head:
                # appends the data in each node to the list
                elems_list.append(current_node.datan)
                # advances the current node to the next node
                current_node = current_node.nxt_node
            # appends the items to a python list, for easy printing
            elems_list.append(current_node.datan)
            # prints out the python list
            print(elems_list)

# ANCHOR Main
# determine if this script is being called by itself or imported. Only execute if it is not being imported.
# learned from: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    print("School for this week is now open!")

    # create an empty empty list
    signs_list = c_linked_list()

    # for the count in the range between 1 and num_signs...
    # create signs to be shown in a circ linked list
    for sign_count in range(1, num_signs + 1):
        # create sings to be shown in a circ linked list
        signs_list.append_right(f"Sign {sign_count}")

    # for the count in range between 1 and num_students...
    # create students as specified by num_students
    for studentcount in range(1, num_students + 1):
        # create students as specified by num_students
        students_roster.append(create_student(studentcount))

    # set the time to be nothing
    time_seconds = 0
    # set the current node (sign) to the head
    current_node = signs_list.head
    # while the time in seconds is less than a week
    while time_seconds < 604800:
        # if the time_seconds % sign_show_duration and equals 0, change the sign to the next one
        if time_seconds % sign_show_duration == 0:
            # change the sign to the next one
            current_node = current_node.nxt_node
        # for each student in the list of students
        for student in students_roster:
            # if time_seconds is in the students start time list
            if time_seconds in student.start_time_list:
                # create a temp_node and set it the current node
                temp_node = current_node
                # for signs_count in the range of read_duration // sign_show_duration
                for signs_count in range(student.read_duration // sign_show_duration + 1):
                    # add the current temp node (sign) to the students seen list
                    student.signs_seen(temp_node.datan)
                    # advance the sign (node) to the next one and run the loop again to see if the student has time to see it
                    temp_node = temp_node.nxt_node
                    # debug
                    #print("Seeing sign...")
        # increment the time by + 1
        time_seconds += 1

    # function that calculate how many signs the students have seen
    def calc_signs_seen():
        # create an empty list to dump all the signs into
        all_signs_seen = []
        # for each student in the students_roster
        for student in students_roster:
            # add their signs to the python list all_signs_seen
            all_signs_seen.extend(student.student_signs_seen)
        # once all the adding has been done, sort the list
        all_signs_seen.sort()
        # debug
        #print(all_signs_seen)

        # for each sign in the sorted set list
        for sign in sorted(set(all_signs_seen)):
            # print how many times the sign has been seen
            # i made this a bit more complicated than i needed to, buit i really was set on have it be 1 line... :)
            print(f"{sign} was seen {all_signs_seen.count(sign)} times - about {round(((all_signs_seen.count(sign) / len(all_signs_seen)) * 100), 2)}% of the time.")


    # call the function to calculate how many sings have been seen
    calc_signs_seen()

    print("School for this week is now done.")