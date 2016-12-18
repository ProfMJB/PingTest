import subprocess, time

hostname = "google.co.uk"
while True:
    proc = subprocess.Popen("ping " + hostname, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if out[0:6] == "Ping r":
        with open("log.txt", "a") as thisfile:
            thisfile.write(str(time.strftime("%c"))+" Fail\n")
        print("Fail")
    else:
        parse = out.split("time=")
        pingtime = parse[1].split("ms")
        with open("log.txt", "a") as thisfile:
            thisfile.write(str(time.strftime("%c")) + " Success. Time : "+ pingtime[0]+"ms\n")
        print("Success")
    time.sleep(30)