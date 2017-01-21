import urllib.request, urllib.error, urllib.parse  
httpHandler = urllib.request.HTTPHandler(debuglevel=1)  
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)  
opener = urllib.request.build_opener(httpHandler, httpsHandler)  
urllib.request.install_opener(opener)  
request = urllib.request.Request('http://www.windpunish.net/')
feeddata = opener.open(request).read()

