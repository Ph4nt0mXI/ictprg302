#!/usr/bin/python3
"""
Title: Backup.py
Author: Nathan Davies
Version: 1.0
Copyright Nathan Davies
Description: this program is designed to be used to backup both files and directories of files.
"""
import os
import math
import sys
from backupcfg import jobs, backupDir, backupLog, smtp
from datetime import datetime 

import smtplib
import pathlib
import shutil

def errorHandler(errorMessage, dateTimeStamp):
# The errorHandler function helps to define which error is occuring, making it easier for the user to understand what type of error they are having.
    print (errorMessage)
    writeLogMessage(errorMessage, dateTimeStamp, False)
    sendEmail(errorMessage)
    pass

def writeLogMessage(logMessage, dateTimeStamp, isSuccess):
# The writeLogMessage function writes and print a message both to a log and in the terminal about whether the backup was successful or if it's a failure, what error has occured 
    
    try:
        file = open(backupLog, "a")
        if isSuccess:
            file.write(f"SUCCESS {dateTimeStamp} {logMessage}\n")
        else:
            file.write(f"FAILURE {dateTimeStamp} {logMessage}\n")
        
        file.close()
    except FileNotFoundError:
        print("ERROR: File does not exist.")
    except IOError:
        print("ERROR: File could not be accessed.")
        
def sendEmail(message):
#This defines who the email message is to, who is snending the message and what message is being sent 
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")
        
def main():
# this is the main function, this body of the program which is the steps which the program follows
   
    try:
      
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        argCount = len(sys.argv) 
       
        # Check at least one CLI argument
        if argCount < 2:
            errorHandler("ERROR. Job Not Specified", dateTimeStamp)
        else:
       
            for jobname in sys.argv[1:]:
            # check for valid job name in directory
                if not jobname in jobs:
                    errorHandler(f"ERROR. Job {jobname} not on the list", dateTimeStamp)
                else:
                    
                    jobsPath=jobs[jobname]
                    #Check source is a valid file/directory
        
                    if not os.path.exists(jobsPath):
                        errorHandler(f"ERROR: file {jobsPath} does not exist",dateTimeStamp)
                    else:
                        Destination = backupDir
                        # check Destination is valid
                        if not os.path.exists(Destination):
                            #os.makedirs(jobsPath)
                            errorHandler(f"ERROR: Dir {Destination} does not exist", dateTimeStamp)
                        else:
                            
                            srcPath = pathlib.PurePath(jobsPath)
                            dstLoc = Destination + "/" + srcPath.name + "-" + dateTimeStamp
                            # copys file/directory to a backup directory
                            if pathlib.Path(jobsPath).is_dir():
                                shutil.copytree(jobsPath, dstLoc)
                            else:
                                shutil.copy2(jobsPath, dstLoc)
                            
                            
                            writeLogMessage(f"Copied {jobsPath} to {dstLoc}", dateTimeStamp, True) 
                            print(f"{jobsPath} Has been backed up successfully")
    except:                        
        sendEmail("ERROR: The program has crashed")                   
 

if __name__ == '__main__':
    main()
