import time
import requests
import xml.etree.ElementTree as xml
url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=gZ1mis9Xa%2FvXgaEyc0FxYyZ7QvEq1u5WTu4U5thsna%2Bbp3lNV0RztdYSw%2FIuvOIZkJWjETFZRUMG%2FcpQuJgHwA%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200302&endCreateDt=20200723"
res = requests.get(url)
root = xml.fromstring(res.text)
data = []
for items in root.iter("items"):
	for item in items:		
		j = {}
		for i in item:
			#print(i.tag, i.text)
			j[i.tag] = i.text
		data.append(j)

print("Total Count : ", len(data))

def search_duration(startDt, endDt):
	result = []
	for row in data:
		r = {}
		#if row['stateDt'] >= '20200301' and row['stateDt'] <= '20200304':
		if row['stateDt'] >= startDt and row['stateDt'] <= endDt:
			r['stateDt'] = row['stateDt']
			r['decideCnt'] = row['decideCnt']
			r['clearCnt'] = row['clearCnt']
			r['examCnt'] = row['examCnt']
			r['deathCnt'] = row['deathCnt']
			r['clearCnt'] = row['clearCnt']		
			result.append(r)
	print(result)
	print("Count : ", len(result))
	return result

def search_death(count):
	result = []
	for row in data:
		r = {}
		#if row['stateDt'] >= '20200301' and row['stateDt'] <= '20200304':
		if int(row['deathCnt']) >= int(count):
			r['stateDt'] = row['stateDt']
			r['decideCnt'] = row['decideCnt']
			r['clearCnt'] = row['clearCnt']
			r['examCnt'] = row['examCnt']
			r['deathCnt'] = row['deathCnt']
			r['clearCnt'] = row['clearCnt']		
			result.append(r)
	print(result)
	print("Count : ", len(result))
	return result

#search_duration('20200301', '20200304')
#search_death(60)

while True:
	print("* 코로나바이러스감염증 감염현황 조회 서비스")
	print("########################################")
	print("# 1. 기간별 조회")
	print("# 2. 사망자 조회")
	print("# 3. 종료") 
	print("########################################")
	sel = input("# 메뉴를 선택해주세요.(1-3) :")

	if sel == "1":
		startDt = input("시작기간을 입력해주세요. :")
		endDt = input("시작기간을 입력해주세요. :")
		result = search_duration(startDt, endDt)
		print(result)
		time.sleep(2)
	elif sel == "2":
		count = input("기준 사망자수를 입력해주세요. :")
		result = search_death(count)
		print(result)
		time.sleep(2)
	elif sel == "3":
		print("감사합니다. 안녕히 가십시요.")
		time.sleep(2)
		break
	else:
		print("메뉴를 잘못선택하였습니다. 다시 선택해주세요.")
		time.sleep(2)		
		break