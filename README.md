# ToAnalytics
Sends nginx combined log hits to google analytics. Optimised for an eBay tracking pixel.

##Dependencies
requests  
time
random
datetime
GEOIP and GEOLITE 2
also Python... duh

##To make it work
You'll need to change the image name and the log file name. Place in log file directory, make sure your nginx log format isnt different from the standard one and add some kind of identifier to the end of your pixel embed. 

Also, get your own Google Analytics Account ID and obviously run this daily with cron. Clear the log file daily too... duh

Enjoy your google analytics with no javascript.
