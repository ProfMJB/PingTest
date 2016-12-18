'''
Created on 17 Dec 2016

@author: Max
'''
import time, subprocess
hostname = "google.co.uk"
while True:
    response = subprocess.Popen("ping -c 1 " + hostname, stdout=subprocess.PIPE, shell=True)
    print(str(response))
    time.sleep(30)