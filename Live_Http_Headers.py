# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import sys
import hashlib
import http.client
def main():
 """  httpHandler = urllib.request.HTTPHandler(debuglevel = 1)
   httpsHandler = urllib.request.HTTPSHandler(debuglevel = 1)
   opener = urllib.request.build_opener(httpHandler, httpsHandler)
   urllib.request.install_opener(opener)
   response = urllib.request.urlopen("http://www.windpunish.net/")
   html = response.read()
   print(httpHandler, httpsHandler)

"""
httpResponse = urllib.request.urlopen("https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn")
resheader = httpResponse.getheaders()
print(resheader)
for header,value in httpResponse.headers.items() :
    print(header+':'+value )

if __name__ == "__main__":
    main()

