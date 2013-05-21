"""
Author: Debabrata Tripathy
Email : dtripathy10@gmail.com

Access goole map API:
--------------------
For aceessing google map api we have 2 component
 1 - make url according to information nedded
 2 - it send data either in json/xml format. parse it according to your need


More information about google map api for url creation visit the below link
           https://developers.google.com/maps/documentation/geocoding/

"""

import urllib2, urllib
from urllib2 import urlopen
import json


proxy = urllib2.ProxyHandler({'http': 'http://debabratatripathy:debu!linux@netmon.iitb.ac.in:80'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#conn = urllib2.urlopen('http://python.org')
#return_str = conn.read()


url = 'http://maps.googleapis.com/maps/api/geocode/json?address=powai&sensor=false'
request = urllib2.urlopen(url)
return_str = request.read()
data_dump = json.loads(return_str)
for rs in data_dump:
    print rs

text_file = open("Output.json", "w")
text_file.write(return_str)
text_file.close()

print 'completed.................'
