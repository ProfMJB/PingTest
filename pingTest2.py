import subprocess

hostname = "google.co.uk"
proc = subprocess.Popen("ping " + hostname, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
if out[0:6] == "Ping r":
    print("Fail")
else:
    print("Success")
    parse = out.split("time=")
    time = parse[1].split("ms")
    print("time : "+time[0])
print(out)
print(out[0:6])