__author__ = 'CDavidson'

import os
import os.path
from batch_b4u_converter import B4U_Convert

#user entered path to the desired directory
folder = raw_input("Where are your b4u\'s?")
#extantiating the B4U_Convert class
convert = B4U_Convert()

#this will search through the given directory, folder, and find all .b4u file within and convert them to b4x
for directory, dirnames, filenames in os.walk(folder):              #using os.walk to step through all the folders
    for file in filenames:                                          #for all the files that exist in the given directory
        if file.endswith(('b4u')):                                  #if the file is a .b4u file
            input_dir = os.path.join(directory,file)                #then take the current directory and filename and combine them and save them as input_Dir
            output_dir = os.path.join(directory,"OUTPUT_B4Xs_1")    #then take the current directory and add "OUTPUT_B4Xs_1" to the path
            b4xPath = os.path.join(directory,"OUTPUT_B4Xs_1",file)  #take the current dir join it to "OUTPUT_B4Xs_1" and the file name
            finalPath =  b4xPath[:-4]                               #remove the file extension from the b4xpath
            if not os.path.exists(finalPath):                       #this logic skips b4u's that have already been converted
                convert.processMessage(input_dir,output_dir)        #call the B4U converter and pass both the input and output directories
            else:                                                   
                print "Skipping - File Already Exists"              #letting the user know that the file is being skipped