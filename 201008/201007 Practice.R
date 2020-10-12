library(dplyr)
library(foreign)
library(readxl)
library(ggplot2)


#Q1.
# myregion<-data.frame(code_region=c(1:7),
#            region=c("서울","수도권","경남","경북","대전","강원","광주"))
# left_join(welfare, myregion, id="code_region")


welfare<-rename(welfare, 
                sex=h10_g3,
                birth=h10_g4,
                marriage=h10_g10,
                religion=h10_g11,
                income=p1002_8aq1,
                code_job=h10_eco9,
                code_region=h10_reg7)

list_region<-data.frame(code_region=c(1:7),
           region=c("서울", "수도권(인천/경기)","부산/경남/울산",
                    "대구/경북","대전/충남","강원/충북","광주/전남/전북/제주도"))
list_region

table(welfare$code_region)

welfare<-left_join(welfare, list_region, id="code_region")

welfare %>% 
  select(code_region, region) %>% 
  head

str(welfare)

welfare$age<-2015-welfare$birth+1

welfare<-welfare %>% 
  mutate(ageg=ifelse(age<30,"young",
                     ifelse(age<=59,"middle","old")))

#지역별 연령대 비율 조사
welfare %>% 
  group_by(region, ageg) %>% 
  summarise(cnt=n()) %>% 
  mutate(tot_group=sum(cnt)) %>% 
  mutate(pct=round(cnt/tot_group*100,2))


#지역별 연령대 비율 조사(count함수 이용)
region_ageg<-welfare %>% 
  count(region, ageg) %>% 
  group_by(region) %>% 
  mutate(pct=round(n/sum(n)*100,2))

ggplot(data=region_ageg, aes(x=region, y=pct, fill=ageg))+
  geom_col()+
  coord_flip()

#노년층 비율 오름차순 정렬
list_order_old<-region_ageg %>% 
  filter(ageg=="old") %>% 
  arrange(pct)

list_order_old

order<-list_order_old$region
order

ggplot(data=region_ageg, aes(x=region, y=pct, fill=ageg))+
  geom_col()+
  coord_flip()+
  scale_x_discrete(limits=order)#limits=c(서울, 부산, 수도권,...)


mpg<-as.data.frame(ggplot2::mpg)
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA

table(mpg$drv)

table(is.na(mpg$drv))
table(is.na(mpg$hwy))

mpg %>% 
  filter(!is.na(hwy)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy=mean(hwy))


#오후 연습문제. 시각화연습
str(iris)
str(iris3)
iris3
#리스트:다양한 타입의 자료들이 저장될 수 있는 자료구조



mpg <- as.data.frame(ggplot2::mpg) # mpg 데이터 불러오기 
mpg[c(10, 14, 58, 93), "drv"] <- "k" # drv 이상치 할당 
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42) # cty 이상치 할당

table(mpg$drv)
mpg$drv<-ifelse(mpg$drv %in% c("4","f","r"),mpg$drv, NA)

table(mpg$drv)

boxplot(mpg$cty)

boxplot(mpg$cty)$stats

boxplot(mpg$cty)$stats[1] #아랫쪽 극단치 경계값

boxplot(mpg$cty)$stats[5] #윗쪽 극단치 경계값

#극단치를 NA로 대체
mpg$cty<-ifelse(mpg$cty<boxplot(mpg$cty)$stats[1] | mpg$cty>boxplot(mpg$cty)$stats[5], NA, mpg$cty)

boxplot(mpg$cty)

mpg %>% 
  filter(!is.na(drv) & !is.na(cty)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy=mean(cty))








