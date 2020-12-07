y<-rnorm(100) #평균:0, 표준편차:1, 정규분포 난수
hist(y)


x<-matrix(rnorm(100), nrow=5)#난수 100개 생성 -> 5행*20열
dist(x) #데이터 간 거리 구하기 : 기본옵션(유클리디안 거리)
#20차원에 해당되는 데이터에서 1번째, 2번째 데이터간의 유클리디안 거리=5.966193 
#       1        2        3        4
# 2 5.966193                           
# 3 4.116722 5.714991                  
# 4 5.195768 5.016578 4.347651         
# 5 5.155299 4.703613 4.260210 4.513890

dist(x, method="manhattan") #데이터 간 거리 구하기 : 맨하탄거리


data(iris) #data함수 : 데이터를 로드
head(iris)

iris[,-5] #5번재 열은 제외하기기


#클러스터의 개수(k)를 결정하는 기법
#1. elbow : 이질성 혹은 동질성의 특성이 완만해지는 부분분
#2. k = sqrt(n/2) -> 통계적 기법 (n: 데이터 개수)
# 
# iris는 4차원(features 개수가 4개) 데이터 => 3개 클러스터
# 
# =>3개 클러스터에 대한 중심점의 좌표 확인(centers)
# ex)
# #1 cluster의 cp : (5.7, 2.5, 1.3, 0.15)
# #2 cluster의 cp : (4.7, 1.5, 1.3, 0.15)
# #3 cluster의 cp : (3.7, 2.7, 1.3, 0.15)
# #3행 4열
# 
# ex)3만명 sns데이터, 5개 클러스터, features 30개
# 5개 클러스터에 대한 중심점의 shape?  5행 30열
#   1행 값들의 의미? 1번째 클러스터의 중심점 좌표
#   2행 값들의 의미? 2번째 클러스터의 중심점 좌표


# kmeans 클러스터링 1
kmeans.iris<-kmeans(iris[,-5], 3)

kmeans.iris$centers #각 클러스터의 중심점 출력
kmeans.iris$cluster #각 데이터가 어떤 클러스터에 할당되었는지를 확인하는 코드

iris[,5]
kmeans.iris$cluster


table(iris[,5], kmeans.iris$cluster) #실제결과와 클러스터 한 결과를 비교할 수 있음


# kmeans 클러스터링 2: nstart(클러스터링 횟수) 지정
kmeans.iris<-kmeans(iris[,-5], 3, nstart=50)
table(iris[,5], kmeans.iris$cluster)
kmeans.iris


kmeans10.iris<-kmeans(iris[,-5], 3, nstart=10)
round(sum(kmeans10.iris$withinss),2) #각 클러스터 내의 데이터와의 거리들의 합 : 78.85




###############################################################################
set.seed(123)

kmeans.iris<-kmeans(iris[,-5], 3)
round(sum(kmeans.iris$withinss),2) #78.85

kmeans10.iris<-kmeans(iris[,-5], 3, nstart=10)
round(sum(kmeans10.iris$withinss),2) #78.85

#####################################시각화#######################################

iris_plot <- ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, colour=Species))+
  geom_point(shape=19, size=4)+ #shape :점의 모양
  ggtitle("iris data")
iris_plot


iris_plot2<-iris_plot+
  annotate("text", x=1.5, y=0.7, label="Setosa", size=5)+ #시각화 된 그래프 위에 텍스트
  annotate("text", x=3.5, y=1.5, label="Verisicolor", size=5)+
  annotate("text", x=6, y=2.7, label="Virginica", size=5)


iris_k_means<-kmeans(iris[ ,c("Petal.Length", "Petal.Width")], 3)
iris_k_means


iris_k_means$cluster
iris_k_means$totss #모든 데이터의 제곱합의 총합
iris_k_means$withinss #응집력 : 클러스터 내 데이터의 거리(응집력)
iris_k_means$betweenss #클러스터 간의 데이터 거리(..력)
#`size` : 클러스안의 데이터 갯수
#`iter` : 클러스터링 반복 횟수

prop.table(iris_k_means$size) #`prop.table()` : 빈도수를 비율로 나타냄


#클러스터링 그래프에 중심점 표시를 추가
iris_k_means_centers<-iris_k_means$centers
iris_k_means_centers

iris_plot2+
  annotate("point", x=5.59, y=2.03, size=5, color="black")+
  annotate("point", x=1.46, y=0.24, size=5, color="black")+
  annotate("point", x=4.26, y=1.34, size=5, color="black")



#kmeans 고려사항
#표준화 작업
z_iris<-scale(iris[,-5]) #표준화 함수

#kmeans 장애요인(한계점) -> H-clustering, DBSCAN으로 극복
#1. 범주별 데이터 개수가 비슷한 경우 -> 클러스터링 잘 됨
#2. 범주별 데이터 개수가 차이가 심한 경우 -> 클러스터링 잘 되지 않음 
#     => 데이터증식 or 데이터 제거=> 범주별 데이터 개수를 비슷하게 해줌
#3. 범주별 밀도가 다른 경우에 클러스터링이 잘 되지 않을 수 있음


# <연습문제>
# 1. iris 컬럼 2개, 3개, 4개 => 클러스터링 수행
# 2. wine 데이터 클러스터링
