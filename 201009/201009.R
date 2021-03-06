# eps(epsilon)? 특정한 1개 데이터로부터 떨어진 거리
# eps 범위 내에 데이터가 minPts개 이상 있으면 클러스터로 인식
# 
# ex) 점 p가 있을때, 점 p로부터  eps 이내에 다른 점들이(점 p도 포함됨) minPts개 이상 있다면,
# 이 영역을 하나의 클러스터로 간주


teens<-read.csv("snsdata.csv")
str(teens)

table(teens$gender) #table함수에서 NA값은 별도의 범주로 취급하지 않고 제외

table(teens$gender,useNA = "ifany") #NA값도 범주로 취급

table(teens$gradyear) #졸업연도

#1. 연습문제
#gender를 다른 값으로 대체, na 값을 갖는 학생과 가장 유사한(거리) 학생 10명 검색 -> 성별 판단 = 클러스터링

#table(teens$age)
summary(teens$age) #기술통계(describe)


#범주형 데이터에 대한 결측치는 별도의 범주로 취급하자
#gender 범주 : F OR M
str(teens)
teens$age<-ifelse(teens$age>=13 & teens$age<20, teens$age, NA) #stats or boxplot 사용
summary(teens$age)

teens$female<-ifelse(teens$gender=="F" & !is.na(teens$gender), 1, 0) #F이면서 NA가 아니면 1, 그렇지 않면 남성(0) => NA가 남성에 포함된다
table(teens$female, useNA="ifany")

teens$no_gender<-ifelse(is.na(teens$gender),1,0) #gender가 NA이면 1 아니면 0
table(teens$no_gender, useNA="ifany")


#age 칼럼

mean(teens$age)
mean(teens$age, na.rm=TRUE)

#퀴즈1.
#졸업연도 정보 -> 나이 유추
#졸업연도에 따른 나이의 평균
#졸업연도 조사, 각 졸업연도별 나이 평균
library(dplyr)

# aggregate(data, y(나이)~x(졸업연도), 집계함수(평균), na.rm=TRUE)
# y~x : x를 기준으로 y에 대해 집계함수를 수행
aggregate(data=teens,age~gradyear, mean, na.rm=TRUE)

# 나이(Age) NA(결측치) 처리
#1) 졸업연도를 확인 
#2) 졸업연도에 해당되는 age열 값을 가져와서 대체
################################################################################
#ave함수: 입력 벡터(x)의 길이와 동일한 길이의 벡터를 출력
x<-1:10
x #길이가 10인 벡터
mean(x) #5.5
ave(x) #5.5 ... 5.5  (5.5값이 벡터의 길이만큼 출력)

mygroup<-rep(1:2, c(3,7)) #1이 3번, 2가 7번 반복
mygroup #두 그룹

ave(x, mygroup, FUN = mean) #r같은 그룹의 데이터들에 대해 집계함수의 값을 반환 
#2  2  2  7  7  7  7  7  7  7
x       #1  2  3  4  5  6  7  8  9 10
mygroup #1  1  1  2  2  2  2  2  2  2


ave(x, mygroup, FUN = sum)
#6  6  6 49 49 49 49 49 49 49
x       #1  2  3  4  5  6  7  8  9 10
mygroup #1  1  1  2  2  2  2  2  2  2


ave(x,mygroup,FUN=function(a)sum(a^2))
################################################################################
ave_age<-ave(teens$age, teens$gradyear, FUN=function(x) mean(x, na.rm=TRUE))
teens$age<-ifelse(is.na(teens$age),ave_age,teens$age) 



summary(teens$age)
class(teens[5:40]) #자료구조 확인 함수

interests<-teens[5:40]
interests_z<-as.data.frame(lapply(interests, scale)) #scale : 표준화(mu=0,sigma=1)

set.seed(12345) #동일한 난수 발생
teen_clusters<-kmeans(interests_z, 5)
teen_clusters$size #4161 21580   578  2663  1018
teen_clusters$centers #각 클러스터에 대한 중심점의 좌표(36차원)
#ex) 1번째 클러스터의 중심점:(0.0121330, 0.09171404, ..., -0.05735705)
# 1번:운동(보통), 교회(종교), 음악, 쇼핑, 외모 관심 많음
# 2번:운동 싫어함, 별 관심이 없음, 내성적인 아이들...
# 3번:운동(보통), 외모 관심, 섹쉬함
# 4번:운동 매우 좋아함
# 5번:운동 조금 좋아함, 문제아(위험) 많음, 멋을 많이 부림, 외모, 노는것 좋아함

teens$cluster <- teen_clusters$cluster
teens[1:10,c("cluster", "gender", "age", "friends")]

aggregate(data=teens, age  ~ cluster, mean)
#클러스터 단위로 나이에 대한 평균을 구해라
aggregate(data=teens, female  ~ cluster, mean)
aggregate(data=teens, friends  ~ cluster, mean)


#분석은 끝냈고, 새로운 학생이 전학을 옴 -> 어떤 cluster에 속할까?
data<-as.data.frame(snsdata) #snsdata에는 36개 컬럼에 대한 값이 저장된 상태
data_z<-scale(data)


# 유사도 구하기
install.packages("proxy")
library(proxy)
#문서번호 : d1,d2,d3, c(단어등장횟수 벡터)
#(sky, cloud, rain)
d1<-c(1,0,5)
d2<-c(4,7,3)
d3<-c(40,70,30)

doc<-rbind(d1,d2,d3) #3x3행렬, row bind
colnames(doc)<-c("sky", "cloud", "rain")
doc

dist(doc, method="cosine") #코사인 거리 : 1-(두 점의 내적)
dist(doc, method="euclidean") #유클리디안 거리




################################ 연습문제 ######################################
#1. gender를 다른 값으로 대체, na 값을 갖는 학생과 가장 유사한(거리) 학생 10명 검색 -> 성별 판단 = 클러스터링
#2. 모델 퍼러미터 조정(n-start 등)
#3. 각 클러스터 해석(using aggregate())
#   => ???  ~ cluster  => 해석 결과를 문장으로 작성
#4. wine 데이터 클러스터링
