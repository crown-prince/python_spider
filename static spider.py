import urllib.request
from bs4 import BeautifulSoup

def main():
    #提取网页源码
    userMainUrl = "http://www.songtaste.com/user/351979/"
    req = urllib.request.Request(userMainUrl)
    resp = urllib.request.urlopen(req) #data=urllib.request.urlopen(url).read()  
    respHtml = resp.read()
    #  print(respHtml)

    #解析网页源码，提取指定内容
    soup = BeautifulSoup(respHtml, "html.parser",  from_encoding =  "GB2312")
    foundClassH1user = soup.find(attrs={"class":"h1user"}) #<h1 class="h1user">crifan</h1>
    print("foundClassH1user = %s " % foundClassH1user)
    if(foundClassH1user):
        h1userStr = foundClassH1user.string
        print("h1userStr = %s",  h1userStr)
  
if __name__ == "__main__":
    main()

    
