import os,sys,time

os.system("reset")
print "Install Tools..."
time.sleep(2)
os.system("pkg install curl")
os.system("pip2 install requests")
os.system("pip2 install mechanize")
os.system("python2 dark.py")
