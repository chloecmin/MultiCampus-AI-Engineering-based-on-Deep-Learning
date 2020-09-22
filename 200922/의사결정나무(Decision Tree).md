# 의사결정나무(Decision Tree)



## 1. 불순도 함수

### 1-1. 지니지수

### 1-2. 엔트로피

- 엔트로피(복잡도)가 높을수록 무질서도가 높다. => **명확한 구분을 위해 의사결정나무는 엔트로피가 가장 적은 곳을 기준선으로 잡는다.**

- 공식 :  

  ![엔트로피공식](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FboyIKw%2FbtqBZr9v4dB%2FhJ1CbE1kIxlTWS1KDlARj1%2Fimg.png)

- 그래프 : 사건이 2개일 경우, 50:50일 확률의 경우 엔트로피가 가장 높음

![img1](https://miro.medium.com/max/500/0*tFIx9il3dkHW605S)

### 1-3. 디비언스

### 1-4. 분류오분류율





## 2. 정보획득량(Information Gain)

공식 : ( 분할 전 영역에 대한 엔트로피 ) - ( 분할 후 생성 영역에 대한 엔트로피 )



## 3. XGboost

여러 개의 `의사결정나무(Decision Tree)`를 조합한 앙상블 알고리즘. 최신기법



> `앙상블 기법` 이란?
>
> * 배깅(bagging) : 병렬학습
>
> * 부스팅(boosting) :  순차적 학습. 한번 학습 후 결과에 따라 오답에 가중치를 부여한 후 재학습 반복. 배깅에 비해 error가 적지만 오버 피팅 가능성이 높음.
>
>   
>
>   ![bagging-n-boosting](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbwr6JW%2FbtqygiHRbRk%2Fcy5hbDAPpTjCG7xa6UWxi0%2Fimg.png) 

