import requests #웹서비스를 요청하는 모듈
import xml.etree.ElementTree as xml

url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=Vsg3jI7E6V%2FAd3mSW%2BqlkbFw1xQtvJxOg%2BOePmttWGmaWPIRJcz%2FVXRycL3K7bCEDbqC9%2BvgDZr8Z%2BnKr53kgA%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200315"
res = requests.get(url)

root = xml.fromstring(res.text)  #sting형태일 때는 fromstring 사용
data = []

for items in root.iter("items"): # iter() 메소드를 이용하면 xml 문서 전체의 엘리먼트를 가지고 온다.
                                 # findall() 메소드를 이용하면 현재 태그의 자식중에서 지정한 태그를 반환한다.
    # print(items.tag)
    for item in items:
        # print(item.tag)
        dic = {}
        for i in item:
            # print(i.tag, i.text)
            dic[i.tag] = i.text
        data.append(dic)

print(len(data))
