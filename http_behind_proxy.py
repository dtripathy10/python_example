import urllib2, urllib
import json

proxy = urllib2.ProxyHandler({'http': 'http://debabratatripathy:debu!linux@netmon.iitb.ac.in:80'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)

conn = urllib2.urlopen('http://python.org')
return_str = conn.read()

print return_str
