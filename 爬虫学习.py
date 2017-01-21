# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re
import os

def write(data):
    if os.path.isfile("web_data.txt"):
        print("Unable to write to file")
    else:
        f = open("web_data.txt", "w")
        f.write(data)
def main():
    #提取网页源码
    url = "http://tieba.baidu.com/p/4674140997?see_lz=1&pn=1"
    """headers = {
    "Host" : "blog.csdn.net",
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding" : "gzip, deflate",
    "DNT": "1",
    "Cookie" : "uuid=c9e0be9e-db19-4d3b-8163-ddd8aa26878d; avh=7398088%2c52075160%2c52044433; bdshare_firstime=1469952437559; dc_tos=ob6737; dc_session_id=1469953123607; uuid_tt_dd=-3581291459300866375_20160731; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1469952905; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1469952981; scvh=2016-07-27+09%3a56%3a55+003%2c2016-07-27+17%3a07%3a49+001; lzstat_uv=34973302962331314719|3609449; lzstat_ss=1724890398_0_1469981762_3609449",
    "Connection" : "keep-alive",
    "Cache-Control" : "max-age=0",
    }"""
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0",}
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req, timeout=10) #data=urllib.request.urlopen(url).read()  
    respHtml = (resp.read()).decode("utf-8")
    write(respHtml)

    soup = BeautifulSoup(respHtml, "html.parser")

    #<h1 class="core_title_txt.*?>(.*?)</h1>
    pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
    re_result = re.search(pattern, respHtml)
    if re_result:
        print("帖子标题：%s" % re_result.group(1))
    

if __name__ == "__main__":
    main()

    
