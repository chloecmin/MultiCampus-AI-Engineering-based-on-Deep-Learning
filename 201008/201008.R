y<-rnorm(100) #평균:0, 표준편차:1, 정규분포 난수
hist(y)


x<-matrix(rnorm(100), nrow=5)#난수 100개 생성 -> 5행*20열
dist(x)
#20차원에 해당되는 데이터에서 1번째, 2번째 데이터간의 유클리디안 거리=5.966193 

#       1        2        3        4
# 2 5.966193                           
# 3 4.116722 5.714991                  
# 4 5.195768 5.016578 4.347651         
# 5 5.155299 4.703613 4.260210 4.513890

dist(x, method="manhattan")


data(iris) #data함수 : 데이터를 로드
head(iris)

iris[,-5]


#elbow
# 
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
# 5개 클러스터에 대한 중심점의 shape?  5행 30열 => 1행 값들의 의미? 1번째 클러스터의 중심점 좌표
# 2행 값들의 의미? 2번째 클러스터의 중심점 좌표 ...
# 




kmeans.iris<-kmeans(iris[,-5], 3)

kmeans.iris$centers

kmeans.iris$cluster

iris[,5]
kmeans.iris$cluster


table(iris[,5], kmeans.iris$cluster)


kmeans.iris<-kmeans(iris[,-5], 3)

#table(iris[,5], kmeans.iris$cluster)
kmeans.iris

kmeans10.iris<-kmeans(iris[,-5], 3, nstart=10)
round(sum(kmeans10.iris$withinss),2) #78.85


data(iris)




set.seed(123)

kmeans.iris<-kmeans(iris[,-5], 3)
round(sum(kmeans.iris$withinss),2) #78.85

kmeans10.iris<-kmeans(iris[,-5], 3, nstart=10)
round(sum(kmeans10.iris$withinss),2) #78.85


ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, colour=Species))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")


iris_plot <- ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, colour=Species))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")


iris_plot2<-iris_plot+
  annotate("text", x=1.5, y=0.7, label="Setosa", size=5)+
  annotate("text", x=3.5, y=1.5, label="Verisicolor", size=5)+
  annotate("text", x=6, y=2.7, label="Virginica", size=5)


iris_k_means<-kmeans(iris[ ,c("Petal.Length", "Petal.Width")], 3)

iris_k_means


iris_k_means$cluster

iris_k_means$totss

iris_k_means$withinss

iris_k_means$betweenss


prop.table(iris_k_means$size)


iris_k_means_centers<-iris_k_means$centers
iris_k_means_centers

iris_plot2+
  annotate("point", x=5.59, y=2.03, size=5, color="black")+
  annotate("point", x=1.46, y=0.24, size=5, color="black")+
  annotate("point", x=4.26, y=1.34, size=5, color="black")



#고려사항 :  kmeans
#표준화 작업
#범주별 데이터 개수가 비슷한 경우 -> 클러스터링 잘 됨
#범주별 데이터 개수가 차이가 심한 경우 -> 클러스터링 잘 되지 않음 => 데이터증식 or
#데이터 제거=> 범주별 데이터 개수를 비슷하게 해줌
#범주별 밀도가 다른 경우에 클러스터링이 잘 되지 않을 수 있음



z_iris<-scale(iris[,-5])



#iris 컬럼 2개, 3개, 4개 => 클러스터링 수행

























