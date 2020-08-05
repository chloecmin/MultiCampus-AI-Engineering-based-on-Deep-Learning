from bs4 import BeautifulSoup
import urllib.request as req

url = "https://stackoverflow.com/questions/tagged/python"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

tlist = soup.select("#questions > div.question-summary > div.summary > h3 > a")
#
for t in tlist:
    print(t.string)
