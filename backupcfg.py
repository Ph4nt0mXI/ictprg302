#!/usr/bin/python3

jobs = {"job700" : "/home/ec2-user/environment/ictprg302/file1",
        "job1" : "/home/ec2-user/environment/ictprg302/dir1"}


backupDir = "/home/ec2-user/environment/ictprg302/backups"

backupLog = "/home/ec2-user/environment/ictprg302/backup.log"

smtp = {"sender": "nathdog11@hotmail.com",
            "recipient": "nathdog11@gmail.com",
            "server": "smtp.gmail.com",
            "port": 587,
            "user": "nathdog11@gmail.com", # need to specify a gmail email address with an app password setup
            "password": "gscawqssvxzruwje"}   # need a gmail app passwordmail app password