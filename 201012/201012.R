member<-data.frame(spent=c(10,1,1,17,4,6,1,15,22,3,0,3,7,0,2),
           time=c(15,2,10,7,5,7,1,10,18,3,1,3,7,10,2))
member
res<-kmeans(member, 3)#member를 3개의 클러스터로 구성
res

install.packages("fpc")
library(fpc)

plotcluster(member, res$cluster, color=T)
res$cluster #각 데이터가 소속된 클러스터
res$centers #각 클러스터의 중심좌표
res$totss #각 클러스터와 데이터간 거리 제곱의 합의 전체 합
res$withinss #응집력
res$tot.withinss #응집력의 총합(작을수록 좋다)
res$betweenss #클러스터 간 떨어져 있는 거리(클수록 좋다)
res$size #클러스터에 소속된 데이터의 개수
res$iter #클러스터링 반복 횟수

#인사이트 도출 => 클러스터에 대한 그룹별 연산
member$cluster<-res$cluster
member

aggregate(data=member, spent ~ cluster, max) #클러스터 별로 최대 spent값을 출력

################################################################################
install.packages("NbClust")
library(NbClust) #최적의 클러스터 갯수를 찾아주기 위한 라이브러리

nb<-NbClust(member[,1:2], min.nc=2, max.nc=5, method='kmeans')
nb$Best.partition

nb<-NbClust(iris[,1:4], min.nc=2, max.nc=5, method='kmeans')
nb$Best.partition

#엘보우 그래프 그리기
data(iris)
irisscale<-scale(iris[,-5]) #표준화
k.max=10
wss<-rep(NA, k.max)
nClust<-list()
for (i in 1:k.max){
  irisRes=kmeans(irisscale, i)
  wss[i]=irisRes$tot.withinss #클러스터 개수에 따른 응집력의 총합을 list에 저장
  nClust[[i]]=irisRes$size #클러스터 당 데이터의 개수 저장
}
wss
nClust

#엘보우 그래프 시각화 => 최적의 클러스터 개수 찾기
plot(1:k.max, wss, type='b') 

#최적의 클러스터 개수로 클러스터링
fitK<-kmeans(irisscale, 3)
str(fitK)

plot(iris, col=fitK$cluster) #클러스터링 결과 시각화

table(predicted=fitK$cluster, Actual=iris$Species) #클러스터링 결과와 실제 결과를 비교(정확도)

########################### < H클러스터링 > ####################################
a<-matrix(rnorm(100), nrow=5) #5행 20열, 표준정규분포 => 5건의 데이터, 20차원

#5개의 데이터를 h-clustering 알고리즘 -> 트리 구성
dist(a) #거리행렬

#거리를 구하는 방법(4가지) 
plot(h<-hclust(dist(a), method="single")) #min-distance
plot(h<-hclust(dist(a), method="complete")) #max-distance
plot(h<-hclust(dist(a), method="average")) #fully-connected
plot(h<-hclust(dist(a), method="centroid")) #centroid-point


####################### 유방암 진단(knn알고리즘) ###############################
wbcd<-read.csv("wisc_bc_data.csv", stringsAsFactors = FALSE)  
# stringsAsFactors : 범주(Factor)형으로 문자 데이터를 읽겠습니까?
# TRUE(DEFAULT) : 범주형 / FALSE : 문자형
str(wbcd)

#문자형을 Factor형으로 형변환
wbcd$diagnosis<-factor(wbcd$diagnosis, levels=c("B","M"), 
                       labels=c("Benign", "Malignant"))
str(wbcd)

#범주형 데이터 확인
wbcd$diagnosis
table(wbcd$diagnosis)
round(prop.table(table(wbcd$diagnosis))*100,1) #각 범주별 비율 확인(소수점 첫째자리까지)

# knn알고리즘을 적용할 수 있는 특징적인 컬럼 3가지 선정
summary(wbcd[c("radius_mean", "area_mean", "smoothness_mean")])

# 정규화함수 구현 : 실제 정규화 시 normalize()함수가 내장 되어 있어 함수를 따로 구현할 필요 없음
normalize<-function(x){ return ((x-min(x))/(max(x)-min(x)))}
normalize(c(1,2,3,4,5))

#id열 빼고 정규화
wbcd<-wbcd[-1]
wbcd_n<-as.data.frame(lapply(wbcd[2:31], normalize)) #수치 데이터 정규화하여 데이터 프레임으로 저장
wbcd_n

# 1) 트레이닝 입력데이터와 정답
# 2) 모델링(knn)
# 3) 모델에 테스트 입력 데이터 -> 예측/분류 결과

# 1) train/test 데이터 나누기
wbcd_train<-wbcd_n[1:469,] #train_x
wbcd_test<-wbcd_n[470:569,] #test_x
wbcd_train_labels<-wbcd[1:469, 1] #train_Y
wbcd_test_labels<-wbcd[470:569, 1] #test_Y

# 2) 모델링(KNN 알고리즘)
library(class)
wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test, cl=wbcd_train_labels, k=21)
wbcd_test_pred

# 성능평가를 위한 crosstable : 예측결과와 실제데이터 정확도
library(gmodels)
CrossTable(x=wbcd_test_labels, y=wbcd_test_pred)

# 성능 향상을 위한 개선 : 표준화
wbcd_z<-as.data.frame(scale(wbcd[-1]))

wbcd_train<-wbcd_z[1:469,]
wbcd_test<-wbcd_z[470:569,]
wbcd_train_labels<-wbcd[1:469, 1]
wbcd_test_labels<-wbcd[470:569, 1]

wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test, cl=wbcd_train_labels, k=21)
wbcd_test_pred

CrossTable(x=wbcd_test_labels, y=wbcd_test_pred)

# k=5,11,15,27 로 돌려가며 가장 적절한 k의 값 테스트