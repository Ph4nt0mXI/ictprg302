#!/usr/bin/python3

import math
import sys
from backupcfg import jobs

def main():

    
    try:
        argCount = len(sys.argv)
        
        if argCount !=2:
            print("ERROR. Job Not Specified")
        else:
            jobname = sys.argv[1]
            if not jobname in jobs:
                print ("ERROR. {jobname} not on the list")
            else:
                pass
    except:
           print ("ERROR: there was an issue") 

if __name__ == '__main__':
    main()