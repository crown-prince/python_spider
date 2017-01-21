# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

def main():
    url = "http://www.wooyun.org/whitehats/"
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respHtml = resp.read()
    ok = respHtml.decode("utf-8")
    #print(ok) 
    
    soup = BeautifulSoup(ok, "html.parser")
    #print(soup.prettify) #格式化输出
    
    two = soup.find_all("a")
    
    for i in range(21, 41, 1):
       print(" \n白帽子名称: %s" % two[i].string)

    
if __name__ == "__main__":
    main()

"""
example:
<title>The Dormouse's story</title>
 
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
"""

"""
print soup.title
#<title>The Dormouse's story</title>
 
print soup.head
#<head><title>The Dormouse's story</title></head>
 
print soup.a
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
 
print soup.p
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

"""
