#스크립트창 -> 파일 저장
#콘솔창 -> 실행결과 확인 / 간단한 코드 실행 결과 확인


# install.packages("readxl") #패키지 설치
library(readxl)

eng <- c(50,60,70)
mat <- c(70,80,90)

#데이터 프레임 생성
df <- data.frame(eng, mat)
df 

class <- c(1,1,2)
dfm <- data.frame(eng,mat,class)
dfm

mean(dfm$eng) #데이터프레임$칼럼명

#엑셀파일 읽어오기
read_excel("Data/excel_exam.xlsx")
read_excel("Data/excel_exam_novar.xlsx", col_names = F) #컬럼 이름을 지정하지 않을때
read_excel("Data/excel_exam_sheet.xlsx", sheet = 3) #몇번째 sheet의 데이터를 가져올지 옵션

#csv파일 읽어오기와 저장하기
data <- read.csv("Data/csv_exam.csv")
str(data) #데이터의 구조를 확인 #python에서 `info()`함수와 동일
write.csv(data, file="Data/savefile.csv")

#
exam <- read.csv("Data/csv_exam.csv")
head(exam) #상위 6개의 데이터 출력
tail(exam)
View(exam) #데이터 전체를 보여줌
dim(exam) #python의 `shape()`함수가 같은 함수
summary(exam) #기술통계 : python의 `describe()`

#######################################
install.packages("dplyr")
library(dplyr)

reexam <- rename(exam, eng=english) #칼럼이름 변경
reexam

reexam$plus_me <- reexam$math + reexam$eng #두 컬럼의 값을 더한 결과를 새로운 칼럼으로 추가가
reexam

#############################################

reexam$result <- ifelse(reexam$math>=70, "pass", 'fail') #np.where()
reexam

install.packages("ggplot2")
library("ggplot2")
qplot(reexam$result)

# ifelse를 중첩시켜서 조건문을 완성
# reexam$hakjum변수에 저장
# 조건 : math<50이면 'C', math<=80이면 'B', math<=100이면 'A'
reexam$hakjum <- ifelse(reexam$math<50, 'C', ifelse(reexam$math<=80, 'B', 'A'))
reexam
qplot(reexam$hakjum)

############################################################
table(reexam$hakjum) #value_counts

#####################################
exam <- read.csv("Data/csv_exam.csv")
exam %>% filter(class==1) #ctnl+shift+m : 필터(특정조건에 맞는 데이터 행만 추출)를 사용하기 위한 기호(%>%, 파이프라인)
exam %>% filter(math>=70 & english>=70)
exam %>% filter(class==1 | class==3)


exam %>% select(math) #특정 열 추출
exam %>% select(math, class)
exam %>% select(-math) #math칼럼을 뺀 나머지 추출

exam %>% filter(class==1) %>% select(english)
exam %>% 
  select(id, math) %>% 
  head

#정렬
exam %>% 
  arrange(math) #오름차순

exam %>% 
  arrange(desc(math)) #내림차순

exam %>% 
  arrange(class, math) #클래스가 같은 경우 오름차순 정렬렬

#파생변수 추가
exam %>% 
  mutate(total=math+english+science) %>% 
  head

exam %>% 
  mutate(res=ifelse(science>=60, 'pass', 'fail')) %>% 
  head

# groupby(집계함수)
exam %>% 
  summarise(mean_math=mean(math))

exam %>% 
  group_by(class) %>% 
  summarise(mean_math=mean(math),
            sum_math=sum(math),
            median_math=median(math), #중앙값
            n=n()) #빈도
#max, min, sd(표준편차), var(분산)

ggplot2::mpg
#패키지명::데이터셋

mpg <- as.data.frame(ggplot2::mpg)
str(mpg)


mpgb<-mpg %>% 
  filter(displ>5)
mpgb







a<-data.frame(id=c(1,2),
             test=c(50,90))
b<-data.frame(id=c(3,4),
            test=c(30,100))
bind_rows(a, b)



name<-data.frame(class=c(1,2,3,4,5),
                 tea=c('kim', 'park', 'lee', 'cho', 'jung'))
name

#exam과 name결합
left_join(exam, name, by='class')

#kmeans -> 3만 청소년의 심리상태 분석