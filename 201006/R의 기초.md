# R의 기초

:star: [참고 소스코드]("R의 기초.R")

## 1. 설치

* [R 설치](https://cran.r-project.org/)
* [R Studio 설치](https://rstudio.com/)



---

## 2. R Studio

- `Script` : 코드입력 및 실제 파일이 저장되는 소스
- `Console` : 실행결과 확인 및 간단한 코드 즉시 입력/실행 가능
- `History` : 실행된 기록(History). 기록을 따로 저장하여 필요할 때 불러낼 수 있음 -> 자주 사용되는 함수나 형식은 `hisory`파일로 저장하여 유용하게 사용할 수 있다
- `Files` : 현재 작업중인 Directory 확인 가능
- `Plots` : `qplot()` 등으로 그래프를 그릴 때 시각화 확인이 가능
- `Help` : `F1`키를 누르면 글이 뜨는 창으로 다른 여타 프로그램보다 정말 유용한 정보들이 많이 뜸.
- `Viewer` : 우선 확인된 기능은 R markdown 작성 후  Knit한 결과를 띄울 수 있다. (추후 더 확인 예정)



---

## 3. 패키지를 활용한 기초문법

> R스크립트에서 라이브러리 설치 및 import하는 방법
>
> ```R
> install.packages(`라이브러리`)
> library(`라이브러리`)
> ```

- ### Basic

   - `ave` : 집계함수 사용

      > ave(데이터, 그룹, FUN = 집계함수)

- ### readxl

  외부 파일(xlsx, excel, csv, 등)의 데이터를 불러오는 패키지

  - `read_exel(*경로*)`
    - `col_names`
    - `sheet`
  - `read.csv(*경로*)`
  - `write.csv(*경로*)`
  - `str()`
  - `head()`
  - `tail()`
  - `view()`
  - `dim()`
  - `summary()`
  - `data.frame()`
  - `matrix()` : 2차원 배열 생성
  - `dist()` : `method`옵션으로 어떤 거리공식을 사용할지 설정. 기본적으로 유클리디안 거리를 이용한 거리
  - `data()` : 내장 데이터를 로드하는 함수

- ### dplyr

  데이터 전처리, 조작을 위한 패키지. R로 전처리시 가장 많이 사용되는 패키지

  ```R
  install.packages('dplyr') 
  library('dplyr')
  ```

  - `$`
  - ` %>%` :   `ctrl`+`shift`+`M`키의 조합으로 사용. 그 앞에 나온 데이터를 계속해서 사용하겠다는 것을 전달해주는 매개함수.
  - `ifelse`
  - `rename`
  - `table()`
  - `filter(*조건문*)`
  - `select(*특정칼럼*)`
  - `arrange(*정렬기준이 될 칼럼*)`
  - `mutate(*생성될 칼럼 이름 = 조건문*)`
  - `summarise(변수=*집계함수*)`
  - `group_by(칼럼)`

- ### ggplot2

   시각화를 위한 패키지, 데이터 셋이 들어있는 패키지

  - `qplot` : `ggplot2`패키지의 기본 함수. 데이터 프레임 형태의 데이터 시각화를 담당. 

```R
#패키지 안의 데이터를 불러오기

install.packages("ggplot2")
library("ggplot2")

mpg <- as.data.frame(ggplot2::mpg)
```

​	