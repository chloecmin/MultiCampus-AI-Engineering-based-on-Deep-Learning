
########################################
#예측 작업
data(iris)
mydata=iris
m=mydata[1:4]
train=head(m,100)
xNew=head(m,10)
train
xNew

rownames(train)<-1:nrow(train)

#표준화 된 유클리디안 거리를 구하는 함수 선언
norm_eucl=function(train)
  train/apply(train,1,function(x)sum(x^2)^.5) #제곱의 합의 제곱근(0.5승)
m_norm=norm_eucl(train)
m_norm

#임의의 데이터 입력 -> kmeans 클러스터 -> 클러스터를 할당 구현
result=kmeans(m_norm,3,30)
result

predict.kmeans <- function(x, newdata){
  apply(newdata, 1, function(r) which.min(colSums((t(x$centers) - r)^2)))
#https://issactoast.com/53

}


head(predict.kmeans(result, train / sqrt(rowSums(train^2))), 3)
# 1 2 3 
# 2 2 2
all.equal(predict.kmeans(result, train / sqrt(rowSums(train^2))), result$cluster)
# [1] TRUE

predict(result, xNew / sqrt(rowSums(xNew^2)))

result
train/sqrt(rowSums(train^2))