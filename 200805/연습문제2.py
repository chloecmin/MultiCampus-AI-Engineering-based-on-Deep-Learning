from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

plist = soup.select("#mw-content-text > div > ul:nth-child(6) > li > ul > li > a")

for p in plist:
    print(p.string)