import requests
import time
import random
import datetime
from geoip import geolite2

#set timestamp
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%M')
writefile = 'ebay-' + timestamp + '.csv'

#create file to write
w = open(writefile, 'a+')

#open file
f = open('image-tracking.log')
i = 0

#make columns
w.write('SKU,IP,COUNTRY,TIME,')
w.write('\n')

for line in f:
     i = i+1
     if ‘thepixelofdoom.jpg?' in line and 'HTTP/1.1" 200' in line and 'googlebot' not in line:
         #split line into ip time and sku
         inputline=line
         splitlist = inputline.split(" - - ")
         IP = splitlist[0]
         #get country from IP
         match = geolite2.lookup(IP)
         COUNTRY = match.country
         splitlist = splitlist[1].split("]")
         TIME = splitlist[0]
         TIME = TIME.strip('[')
         splitlist = splitlist[1].split("?")
         banana = splitlist[1].split('"')
         SKU = banana[0]
         SKU = SKU.strip(' HTTP/1.1')
         payload = {'v': '1', 't': 'pageview', 'tid': 'UA-XXXXXXXX-X’, 'cid' : str(random.random()), 'dt' : SKU, 'dp' : SKU, 'uip' : IP, 'geoid' : COUNTRY}
         r = requests.post("http://www.google-analytics.com/collect", data=payload)
         print r.status_code
         #write to file
         w.write(SKU + ',' + IP + ',' + COUNTRY + ',' + TIME + ',')
         w.write('\n')
         

#close all files
f.close()
w.close()

print "DONE"
