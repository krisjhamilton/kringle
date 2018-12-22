#!/usr/bin/env python3

import requests as req
import json
import urllib2

status = False

f = open( "file.txt", "r" ).read()
lines = f.split("\n")
lineno = ""
rid = 'd802d8b3-be77-4ab8-94ea-933a41d6f98e'
while not status:
    for line in lines:
        lineno = line
        u = "https://doorpasscode.kringlecastle.com/checkpass.php?i="+line+"&resourceId="+rid
        url = urllib2.urlopen(u).read()
        obj = json.loads(url.decode('utf-8'))
        success = obj["success"]
        status = success
        print(obj, success, lineno, u)
f.close()

print(status, lineno, "done")