import os
import time
from multiprocessing import Pool   
import subprocess

print("------------------------------------")
print(" 1.Luanch web")
print("------------------------------------")

web = input("Web url:")
open_count = input("open count:")

i = 1
while i <= int(open_count):
  print(i)
  cmd = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" ' +web + ' --profile-directory='+'QQ'+str(i)
  returned_value = subprocess.call(cmd, shell=False)
  time.sleep(0.5)
  i += 1