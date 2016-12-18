'''
Created on 17 Dec 2016

@author: Max
'''
import os, time
hostname = "google.co.uk"
while True:
    response = str(os.system("ping " + hostname))
    if response == "0":
        ping = "Success"
    else:
        ping = "Fail"
    with open("log.txt", "a") as thisFile:
        thisFile.write("\n"+str(time.strftime("%c"))+" "+ping)
    time.sleep(30)