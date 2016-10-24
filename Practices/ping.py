import os
hostname = "google.com"
response = os.system("ping -c 5 " + hostname)

print (response)

#and then check the response...
if response == 0:
  print (hostname, 'is up!')
else:
  print (hostname, 'is down!')