__author__ = 'CLefevre'
__edits__ = 'CDavidson'

import os
import os.path
import subprocess
import threading
import time
import multiprocessing
from multiprocessing import Pool
from multiprocessing import Process
#from logMessenger.logMessenger import LogMessenger
#from workerTemplate import workerClass

#import settings



class B4U_Convert(object):
    '''
        B4U Conversion, takes in a B4U file as input, outputs a B4X folder structure into the passed destination
    '''
    queue = "B4UConversion"

    ## Constructor
    # @param monitor An AMQP listener object that must implement a monitor method
    # @param publisher An AMQP publisher object that must implement a publish method
    # @param logger A logMessenger object to publish to the log message queue for a logging server to pick up.
    def __init__(self):
        currentPath = os.path.realpath(__file__)
        self.appDir = os.path.split(os.path.split(currentPath)[0])
        self.runDir = os.path.dirname(currentPath)
        self.appDir = self.appDir[0]
        self.processes = []

    ## parseCmdOut will parse the text output from the command line
    # @param cmdOutput The list of output lines to parse
    # @param transactionID The UUID of the process for tracking with the logging service.
    def parseCmdOut(self, cmdOutput):
        error_list = []
        for line in cmdOutput:
            print line
            #errorLog = open(os.path.join(appDir,'errorlog.txt'),'a+')   #open the error log
            #errorLog.write(line + "\n")                                #append the line that caused the error
            '''
            if "ERROR - " in line.upper():
                error_list.append(line)
            elif "Conversion Completed. Output file located at: " in line:
                if '\n' in line:
                    line = str(line)[46:-1]
                else:
                    line = str(line)[46:]
                #line = line[len(self.shareDirectory):].split(os.sep)
                #self.reply_message = {"Output Location":line, "UUID":transactionID}
        #return error_list
            '''
            
    ## processRequest runs the compiled command to convert the B4U into a B4X, and parses the output from the execution into an error_list
    # list, and a reply_message. It will then return the reply message to be sent to the requestee, while the error list will then be sent to the logging server.
    # @param cmd contains the compiled command to be executed calling the B4U_Util.jar with the input and destination directories.
    # @param transactionID contains the transaction ID (UUID) tracking the transaction throughout the process. Used only in the logging server calls.
    def processRequest(self, cmd):
        self.check()
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        self.processes.append(proc)
        self.check()
        #cmd_out = proc.stdout.readlines()
        #errors = self.parseCmdOut(cmd_out)
        
        #proc.wait()
        '''
        #these lines are commented out becuase the logger functions are not being called
        if errors:
            if not self.reply_message:
                self.reply_message = {"ERROR":errors}
            else:
                self.reply_message["ERROR"] = errors
        '''
    #Creating a check that will step trough the subprocesses and check to see if they are still active, if they are active take note and move on, if it is inactive then it is removed from the lsit.
    #Using poll() to check if the subprocess is active, 0 in inactive None is active
    #for performance tweaks you can change the threshold of len(self.processes) > x to whatever your system can handle
    #You can also increase speed by commenting out time.sleep(.1) if your system can handle a lot of recursive checks
    def check(self):                        #defining the function
        count = 0                           #setting position to 0 to start
        for x in self.processes:            #for every process in the list
            if x.poll() == None:            #if the process is active
                count = count + 1           #advance the position count by 1
            else:                           #if the process is not active
                self.processes.remove(x)    #remove this process from the list of processes
                break                       #break the loop as we have changed the list
               
        if len(self.processes) > 25:        #if the length of the list is greater than 30
            print "...Busy..."              #indicate the process is still running but busy
            time.sleep(.1)                  #Had to add a pause as recursion limit was being reached
            self.check()                    #run the check again
        else:
            print "Starting New Conversion" #letting the user know that a new conversion task is being started
                
    ## processMessage processes the message dictionary payload for converting a B4U to B4X using an executable JAR. Method will check the
    # message dictionary for proper values, finally compiling a command line execution for converting the B4U to B4X, returning the file location
    # for the converted files.
    # @param message_dictionary is the dictionary payload for the B4U Convert Worker. The keys "UUID", "B4U_Location", and "Destination" are
    # checked, then the command line execution is compiled. The output is then monitored, finally resulting in the output from the executable
    # Jar being returned to the calling function.
    def processMessage(self, input_dir, output_dir):
        self.reply_message = False
        #input_dir = message_dictionary.pop('B4U_Location') 
        #output_dir = message_dictionary.pop('Destination') 
        jar_file =  os.path.join(self.runDir, 'assets', 'B4U_Util.jar')
        #"C:\\b4ujar\\B4U_Util.jar"  #give static path self.jar_file = absolute path 
        #b4u_location = os.path.join(*input_dir)
        #destination = os.path.join(*output_dir)
        cmd = 'java -jar "%s" "%s" "%s"' % (jar_file, input_dir, output_dir)
        #print os.path.exists(str(input_dir))
        #print os.path.exists(jar_file)
        if os.path.exists(str(input_dir)) and os.path.exists(jar_file):
            print "process request"
            os.system(cmd)
