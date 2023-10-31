#!/usr/bin/python3

jobs = {"job700" : "/home/ec2-user/environment/ictprg302/file1",
        "job1" : "/home/ec2-user/environment/ictprg302/dir1"}


backupDir = "/home/ec2-user/environment/ictprg302/backups"

backupLog = "/home/ec2-user/environment/ictprg302/backup.log"

smtp = {"sender": "dcleary@sunitafe.edu.au",
        "recipient": "",
        "server": "smtp.gmail.com",
        "port": 587,
        "user": "", # need to specify a gmail email address with an app password setup
        "password": ""}   # need a gmail app password