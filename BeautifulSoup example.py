# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


def main():
    html_doc = """  
    <html><head><title>The Dormouse's story</title></head>  
    <body>  
    <p class="title"><b>The Dormouse's story</b></p>  
      
    <p class="story">Once upon a time there were three little sisters; and their names were  
    <a href="http://example.com/elsie" class="sister" id="link">Elsie</a>,  
    <a href="http://example.com/lacie" class="sister" id="link">Lacie</a> and  
    <a href="http://example.com/tillie" class="sister" id="link">Tillie</a>;  
    and they lived at the bottom of a well.</p>  
      
    <p class="story">...</p>

    """
    soup = BeautifulSoup(html_doc, "html.parser")
    print(soup.prettify()) #格式化输出
    print("输出title: %s" % soup.title)
    print("输出第一个p标签的内容: %s" % soup.p)
    print("输出第一个a标签内容: %s" % soup.a)
    print("输出p标签的属性的内容（class = \"title \"）等： %s " % soup.p["class"])
    print("输出a标签的属性（<a href)等： %s" % soup.a["href"])
    print("_____________________________________________________________")
    one = soup.find_all("a", id="link")
    
    for i in one:
       print(" \na标签，id属性之后所包含的正文内容: %s" % i.string)
    print("_____________________________________________________________")
  
    two = soup.find_all("a", "sister")
    
    for i in two:
       print(" \na标签，含有sister内容的标签属性之后所包含的正文内容: %s" % i.string)
    print("_____________________________________________________________")

    three = soup.find_all("a")
    for i in three:
       print(" \na标签，href属性指定的链接 %s" % i["href"])
    print("_____________________________________________________________")    
if __name__ == "__main__":
    main()



  
