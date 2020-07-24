import requests
import xml.etree.ElementTree as xml

class Corona:
    def searchDate(self, start, end):
        self.url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=Vsg3jI7E6V%2FAd3mSW%2BqlkbFw1xQtvJxOg%2BOePmttWGmaWPIRJcz%2FVXRycL3K7bCEDbqC9%2BvgDZr8Z%2BnKr53kgA%3D%3D&pageNo=1&numOfRows=10&startCreateDt={}&endCreateDt={}".format(start, end)
        self.res = requests.get(self.url)
        self.root = xml.fromstring(self.res.text)

        self.data = []
        self.seq = 1

        for self.items in self.root.iter("items"):
            for self.item in self.items:
                dic = {}
                print("[{}]".format(self.seq))
                for self.i in self.item:
                    dic[self.i.tag] = self.i.text
                    # print(self.i.tag,":",self.i.text)
                self.seq += 1
                print("기준일 : ",dic["stateDt"])
                print("확진자수 : ", dic["decideCnt"])
                print("격리해제수 : ", dic["clearCnt"])
                print("검사진행수 : ", dic["examCnt"])
                print("사망자수 : ", dic["deathCnt"])
                print("치료중 환자수 : ", dic["careCnt"])
                print("")
                self.data.append(dic)

        print("총 {}개의 데이터가 있습니다.".format(len(self.data)))
        print("")

        # for self.d in self.data:
        #     print(self.d)
        names = [self.tag for self.tag in self.data[0]]
        print(names)
    def searchDeath(self, num):
        self.url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=Vsg3jI7E6V%2FAd3mSW%2BqlkbFw1xQtvJxOg%2BOePmttWGmaWPIRJcz%2FVXRycL3K7bCEDbqC9%2BvgDZr8Z%2BnKr53kgA%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200302&endCreateDt=20200723"
        self.res = requests.get(self.url)
        self.root = xml.fromstring(self.res.text)

        self.data = []

        for self.items in self.root.iter("item"):
            self.dic = {}
            for self.item in self.items:
                self.dic[self.item.tag] = self.item.text

            if int(self.dic["deathCnt"]) > int(num):
                date = self.dic["createDt"]
                print(self.dic["stateDt"]," ->", self.dic["deathCnt"],'명 사망') #날짜는 date[0:10]으로 대체 가능
            else:
                pass

if __name__ == '__main__':
    while True:
        corona = Corona()

        print("* 코로나바이러스감염증 감염현황 조회 서비스")
        print("####################################")
        print("# 1. 기간별 조회")
        print("# 2. 사망자 조회")
        print("# 3. 종료")
        print("####################################")
        op = input("#메뉴를 선택해주세요(1-3) : ")

        if op == "1":
            # print("옵션1")
            corona.searchDate(input("시작기간을 입력해주세요. : "), input("종료기간을 입력해주세요 : "))
        elif op == "2":
            corona.searchDeath(input("사망자가 몇 명 이상 되는 경우 : "))
        elif op == "3":
            print("종료합니다.")
            break
        else:
            break