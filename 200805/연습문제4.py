from bs4 import BeautifulSoup
import urllib.request as req

# 5페이지까지 평론 출력 :
for i in range(1, 6):
    url = "https://movie.daum.net/moviedb/grade?movieId=127897&type=netizen&page="+str(i)
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")

    vlist = soup.select("p.desc_review")

    for v in vlist:
        v = v.text.split()
        if len(v)>0:
            print(" ".join(v),"\n")

