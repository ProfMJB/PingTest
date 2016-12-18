'''
Created on 18 Dec 2016

@author: davebarnett
'''
import subprocess

hostname = "google.co.uk"

# Mac Specific
proc = subprocess.Popen("ping -c 1 " + hostname, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

print "type:", type(out)

print "program output:", out