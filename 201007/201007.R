library(dplyr)

df<-data.frame(gender=c("m","f",NA,"m","f"),score=c(5,4,3,4,NA))
df
is.na(df)

table(is.na(df))
table(is.na(df$gender)) 

sum(df$score)

df %>% 
  filter(is.na(score)) #결측치를 제외한 연산

dfnew<-df %>% 
  filter(!is.na(score))

mean(dfnew$score)

df %>% filter(!is.na(score) & !is.na(gender))

na.omit(df)

sum(df$score, na.rm=T)

exam<-read.csv("Data/csv_exam.csv")
exam[c(3,8,15),"math"]<-NA #여러 행 추출시에는 c함수로 벡터화해서 추출

#exam[5,"math"]
exam

#결측값을 math의 평균값으로 대체
exam %>% 
  summarise(meanm=mean(math, na.rm=T))

exam %>% 
  summarise(meanm=mean(math, na.rm=T),
            summ=sum(math, na.rm=T),
            mem=median(math, na.rm=T)
            )



exam$math
#퀴즈1. 
#결측값을 math의 평균값으로 대체하라

#방법 1.
#코드 최적화(튜닝)
mean_math<-mean(exam$math, na.rm=T)
exam$math <- ifelse(is.na(exam$math), mean_math, exam$math)
exam

#방법2.
exam$math[is.na(exam$math)] <- mean(exam$math,na.rm=T)

table(is.na(exam$math))

#############################################################

#outlier 제거
#이상치(극단치)는 먼저 결측치로 처리(간주) -> 제외한 다음 분석

#성별변수 : 3가지 -> 1가지(결측처리)
#몸무게변수 : 변수값 200kg(정상범위설정 -> 결측처리)

ol<-data.frame(gen=c(1,2,1,2,3),
           score=c(5,4,1,3,4))
ol
table(ol$gen)

ol$gen<-ifelse(ol$gen==3, NA, ol$gen)
ol

#score가 4초과시 이상치 간주
ol$score<-ifelse(ol$score>4, NA, ol$score)
ol

ol %>% 
  filter(!is.na(gen) & !is.na(score)) %>%
  group_by(gen) %>% 
  summarise(ms=mean(score))


# 데이터전처리 -> 머신러닝/딥러닝
# 10000시간 법칙

#정상범위 : 논리적(통계적) 판단 근거 
#논리적? 성인 몸무게는 40kg~150kg
#통계적? 상하위 0.3% 극단치 or boxplot에서 iqr*1.5배 벗어나면 극단치

boxplot(mpg$hwy)


boxplot(mpg$hwy)$stats # 하위 극단치 경계(q1-1.5*iqr)/1사분위 경계(q1)/중위값/3사분위경계(q3)/상위 극단치 경계

#boxplot(mpg$hwy)$stats[1]
#boxplot(mpg$hwy)$stats[5]

#12보다 작으면,  37보다 크면 => 아웃라이어

mpg$hwy<-ifelse(mpg$hwy<12 | mpg$hwy>37, NA, mpg$hwy)
table(is.na(mpg$hwy))

mpg %>% 
  group_by(drv) %>% 
  summarise(mh=mean(hwy, na.rm=T))

###########################################################################
#한국인 삶의 질 분석#

#Koweps_hpc10_2015_beta1.sav
#sav파일은 SPSS 파일

install.packages("foreign")
library(foreign)
library(readxl)
library(ggplot2)

raw_welfare<-read.spss(file="Koweps_hpc10_2015_beta1.sav", to.data.frame = T)
#복사본
welfare<-raw_welfare
head(welfare)
tail(welfare)
View(welfare)

dim(welfare)
str(welfare)
summary(welfare)


welfare<-rename(welfare, 
       sex=h10_g3,
       birth=h10_g4,
       marriage=h10_g10,
       religion=h10_g11,
       income=p1002_8aq1,
       code_job=h10_eco9,
       code_region=h10_reg7
       )

#성별에 따른 월급 차이?

table(welfare$sex)

table(is.na(welfare$sex)) #결측치 없음

#ifelse사용 sex=1 => male, sex=2 => female 값 변경
welfare$sex<-ifelse(welfare$sex==1, "male", "female")
table(welfare$sex)
qplot(welfare$sex)

summary(welfare$income)
#na 대체값, na 제외

qplot(welfare$income)

qplot(welfare$income)+xlim(0,1000)


welfare$income<-ifelse(welfare$income %in% c(0, 5000), NA, welfare$income)
table(is.na(welfare$income))

###퀴즈2 : na가 아닌 데이터에 대해 성별에 따른 급여 평균 조사###
#방법1
welfare %>% group_by(sex) %>% filter(!is.na(income)) %>% summarise(mean = mean(income))
#방법2
welfare %>% 
  group_by(sex) %>% 
  summarise(meani = mean(income, na.rm = T))
#방법3
sex_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(sex) %>%
  summarise(mean_income=mean(income))
sex_income  
####################################################

ggplot(data=sex_income, aes(x=sex, y=mean_income))+geom_col() #geom_col(): y축의 값을 기준으로 그래프 그림
# 결과 : 성별에 따른 급여 차이가 있음



#몇살때 가장 많은 급여를 받을까?
# -> 나이에 따른 평균 월급
welfare$birth
summary(welfare$birth)
qplot(welfare$birth)

table(is.na(welfare$birth))

welfare$birth<-ifelse(welfare$birth==999, NA, welfare$birth)
table(is.na(welfare$birth))

#퀴즈3.
#age 열 추가
#age는 2015-birth+1 값으로 함
#summary, qplot출력

welfare$age<-2015-welfare$birth+1
summary(welfare$age)
qplot(welfare$age)

#나이에 따른 급여 평균
age_income<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(mean_income=mean(income))

ggplot(data=age_income, aes(x=age, y=mean_income))+geom_col()
ggplot(data=age_income, aes(x=age, y=mean_income))+geom_line() #선그래프

##연령대(young(<30) / middle(<60) / old(>=60))
welfare<-welfare %>% 
  mutate(ageg=ifelse(age<30,"young",
                     ifelse(age<=59,"middle","old")))
welfare

table(welfare$ageg)
qplot(welfare$ageg)

##연령대별 월급 평균 출력
ageg_income<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg) %>% 
  summarise(mean_income=mean(income))
ggplot(data=ageg_income, aes(x=ageg, y=mean_income))+geom_col()

#막대 정렬
ggplot(data=ageg_income, aes(x=ageg, y=mean_income))+geom_col()+
  scale_x_discrete(limits=c("young", "middle", "old"))

#성별에 따른 월급 차이가 연령대별로 다를까 비슷할까?
sex_income<-welfare %>% 
  filter(!is.na(income)) %>%
  group_by(ageg, sex) %>% 
  summarise(mean_income=mean(income))

ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex))+geom_col()+
  scale_x_discrete(limits=c("young", "middle", "old"))

ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex))+geom_col(position = "dodge")+
  scale_x_discrete(limits=c("young", "middle", "old"))

sex_age<-welfare %>% 
  filter(!is.na(income)) %>%
  group_by(age, sex) %>% 
  summarise(mean_income=mean(income))
sex_age

ggplot(data=sex_age, aes(x=age, y=mean_income, col=sex))+geom_line()
  



#직업군 <-> 급여 비교

welfare$code_job
table(welfare$code_job)

welfare$code_job


library(readxl)
list_job <-read_excel("Koweps_Codebook.xlsx", col_names = T, sheet=2)
list_job
dim(list_job) #(shape)직종코드 : 149개


welfare$code_job
welfare<-left_join(welfare, list_job, id="code_job")
#welfare에 list_job을 연결해라(code_job 공통 컬럼 값으로 )

str(welfare)


welfare %>% 
  filter(!is.na(code_job)) %>% 
  select(code_job, job) %>% 
  head(10)

#퀴즈3. 직업별 월급 평균 출력
job_income<-welfare %>%  
  filter(!is.na(job) & !is.na(income)) %>% 
  group_by(job) %>%  #142개 그룹
  summarise(mi=mean(income))
job_income



top20<-job_income %>% 
  arrange(desc(mi)) %>% 
  head(20)
top20

ggplot(data=top20, aes(x=job, y=mi)) + geom_col() +
  coord_flip() #그래프 모양을 가로로 


bottom10<-job_income %>% 
  arrange(mi) %>% 
  head(10)

bottom10
ggplot(data=bottom10, aes(x=job, y=mi)) + geom_col() +
  coord_flip()+ylim(0,500)


#퀴즈4 : 남성 직업 빈도 상위 10개 출력
job_male<-welfare %>% 
  filter(sex == "male" & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt = n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)
job_male

job_female<-welfare %>% 
  filter(sex == "female" & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt = n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)
job_female





#종교가 있는 사람이 이혼을 더/덜할까???
#종교 유/무에 따른 이혼율 조사
table(welfare$religion)

welfare$religion<-ifelse(welfare$religion==1, "yes", "no")
table(welfare$religion)
qplot(welfare$religion)

table(welfare$marriage)

#이혼 여부 변수 생성
welfare$group_marriage<-ifelse(welfare$marriage==1, "marriage", 
       ifelse(welfare$marriage==3, "divorce", NA))
table(welfare$group_marriage)

table(is.na(welfare$group_marriage))

qplot(welfare$group_marriage)


religion_marriage<-welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  group_by(religion, group_marriage) %>% 
  summarise(cnt=n()) %>% 
  mutate(tot_group=sum(cnt)) %>% 
  mutate(pct=round(cnt/tot_group*100,1))


divorce<-religion_marriage %>% 
  filter(group_marriage =="divorce") %>% 
  select(religion, pct)

divorce





