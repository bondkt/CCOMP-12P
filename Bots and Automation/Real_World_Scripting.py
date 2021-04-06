# *===============================================
# * DESCRIPTION
# *===============================================
# File Name: Real_World_Scripting.py
# CCOMP-12P
# Spring 2021
# *===============================================

# *===============================================
# * LIBS
# *===============================================

# import Python Data Analysis Library as pd
import pandas as pd

# import numpy as np
import numpy as np

# import tkinter as tk
# from tkinter import the filedialog function
# learned from https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
# leanred more from: https://docs.python.org/3/library/dialog.html
import tkinter as tk
from tkinter import filedialog

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
appName = "Real_World_Scripting"
appVersion = "1.0.0"
appArch = "x86&x64"
appLang = "EN"
appScriptVersion = "1.0.0"
appScriptDate = "2021.03.28"
appScriptAuthor = "KTeuton"

# *===============================================
## Misc. Variables
# *===============================================

# hide the root GUI window of tkinter
root = tk.Tk()
root.withdraw()

# *===============================================

# use tkinter to open a dialog box to select a text file.
# set certain file types to be opened in the dialog.
# learned from: https://stackoverflow.com/questions/44403566/add-multiple-extensions-in-one-filetypes-mac-tkinter-filedialog-askopenfilenam
input_file = filedialog.askopenfilename(filetypes=[("CSV","*.CSV")])

# not used
# output file location
#output_file = filedialog.asksaveasfilename(filetypes=[("CSV","*.CSV")], defaultextension="*.csv")

# read the incoming CSV
df = pd.read_csv(input_file)

# find duplicate Curriculum Id's in the Curriculum Id 
dupe_id = df[df.duplicated(subset=['Curriculum Id*'], keep=False)]

# print out any duplicate Curriculum Id's
print(f"\nCurriculum Id Duplicates:\n {dupe_id}")

# merge columns C+D to create merged CD.
df["CD"] = df["Course Subject* (CB01)"] + df["Course Number* (CB01)"].astype(str)

# compare CD to B-Course Code (CB01) to ensure nothing is mismatched
results = np.where(df["CD"] == df["Course Code (CB01)"], True, False)

# offset count for the spreadsheet
# couldn't figure out how to get the index from numpy, using manual counter...
count = 2
print()
# for each bool in the numpy array...
for data in results:
    # if a bool is false, it doesn't match and should be checked
    if data == False:
        # print that it doesn't match and should be checked
        print(f"Line {count} - column B and C+D do not match and should be checked.")
    # increment the counter
    count += 1


# merge columns C+D, add 'C' and '-' once they are merged then compare them to column AB-Curriculum Id*
df["colCD"] = "C" + df["Course Subject* (CB01)"] + "-" + df["Course Number* (CB01)"].astype(str)

# compare colCD to Curriculum Id* to ensure nothing is mismatched
results = np.where(df["colCD"] == df["Curriculum Id*"], True, False)

# offset count for the spreadsheet
# couldn't figure out how to get the index from numpy, using manual counter...
count = 2
print()
# for each bool in the numpy array...
for data in results:
    # if a bool is false, it doesn't match and should be checked
    if data == False:
        # print that it doesn't match and should be checked
        print(f"Line {count} - columns C+D and AB do not match and should be checked.")
    # increment the counter
    count += 1


# merge columns V+W, add 'C' and '-' once they are merged then compare them to AB-Curriculum Id*
df["VW"] = df["Course Crosswalk Crs Dept Name (CB19)"] + "-" + df["Course Crosswalk Crs Number (CB20)"].astype(str)

# compare V+W to AB-Curriculum Id* to ensure nothing is mismatched
results = np.where(df["VW"] == df["Curriculum Id*"], True, False)

# offset count for the spreadsheet
# couldn't figure out how to get the index from numpy, using manual counter...
count = 2
print()
# for each bool in the numpy array...
for data in results:
    # if a bool is false, it doesn't match and should be checked
    if data == False:
        # print that it doesn't match and should be checked
        print(f"Line {count} - columns AB and V+W do not match and should be checked.")
    # increment the counter
    count += 1


# merge columns V+W, add '-' once they are merged then compare them to C+D
df["VW"] = df["Course Crosswalk Crs Dept Name (CB19)"] + "-" + df["Course Crosswalk Crs Number (CB20)"].astype(str)

# merge columns C+D, add 'C' and '-' once they are merged then compare them to V+W
df["CCD"] = 'C' + df["Course Subject* (CB01)"] + '-' + df["Course Number* (CB01)"].astype(str)

# compare V+W to AB-Curriculum Id* to ensure nothing is mismatched
results = np.where(df["VW"] == df["CCD"], True, False)

# offset count for the spreadsheet
# couldn't figure out how to get the index from numpy, using manual counter...
count = 2
print()
# for each bool in the numpy array...
for data in results:
    # if a bool is false, it doesn't match and should be checked
    if data == False:
        # print that it doesn't match and should be checked
        print(f"Line {count} - columns C+D and V+W do not match and should be checked.")
    # increment the counter
    count += 1


# merge columns V+W, add '-' once they are merged then compare them to C+D
df["SVW"] = df["Course Crosswalk Crs Dept Name (CB19)"] + df["Course Crosswalk Crs Number (CB20)"].astype(str)

# add c to column B for comparision
df["ColB"] = 'C' + df["Course Code (CB01)"]

# compare L-Course Units of Credit Maximum (CB06) to M-Course Units of Credit Minimum (CB07) to ensure nothing is mismatched
results = np.where(df["SVW"] == df["ColB"], True, False)

# offset count for the spreadsheet
# couldn't figure out how to get the index from numpy, using manual counter...
count = 2
print()
# for each bool in the numpy array...
for data in results:
    # if a bool is false, it doesn't match and should be checked
    if data == False:
        # print that it doesn't match and should be checked
        print(f"Line {count} - columns V+W and B do not match and should be checked.")
    # increment the counter
    count += 1

print("Done")


