#!/usr/bin/env python


import os
import pdb

current_directory = os.getcwd()
dir_to_clean = ['Forum-La1?re', 'LeJournalhoraire-La1?re', 'Lalibrairiefrancophone-La1?re']

for item in dir_to_clean:
    dir_curr = current_directory + os.sep + item
    files = os.listdir(dir_curr)
    files = sorted(files)
    print "In " + item + " deleted:"
    while files.__len__() > 20:
        print files[0]
        os.remove(dir_curr + os.sep + files[0])
        del files[0]
        

