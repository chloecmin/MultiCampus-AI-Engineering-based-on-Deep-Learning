# 1. 기계학습의 역사

* AI는 1940년대 이후   ex)튜링머신 

* 신경망(단일 퍼센트론->멀티퍼셉트론)/DT -> 랜덤포레스트/SVM -> 딥러닝(깊은 신경망)



---



# 2. Titanic



* ## 목표

  정확도 **0.8** 이상



* ## 개선사항
  * 의사결정나무 알고리즘의  문제 : 오버피팅을 방지하기 위해 가지치기 => 부족한 알고리즘

  * [__대안__] [랜덤포레스트](https://github.com/chloecmin/MultiCampus-AI-Engineering-based-on-Deep-Learning/blob/master/200924/%EB%9E%9C%EB%8D%A4%ED%8F%AC%EB%A0%88%EC%8A%A4%ED%8A%B8.md) : 의사결정나무의 한계를 극복하기 위한 알고리즘

  * 나이 결측치 : 나이를 y변수로 두고 예측하여 결측치를 대체



* ## 최적 파라미터
	*  n_estimators=41, max_depth=5
	![kaggle_result](https://cafeptthumb-phinf.pstatic.net/MjAyMDA5MjRfMjc0/MDAxNjAwOTE0NjMwNzE5.deyMlNhVD82Cijz8xOigMNWWHILLayrpwawbfdkNJFsg.LBJfhOw4K9boH6X6OmzhQUiMsTA7R5iNOF66IekxJ4Yg.PNG/image.png?type=w1600)

    


---



# 3. Bike-Sharing-Demand



* ## feature engineering 

  * `windspeed`: 랜덤포레스트로 예측하여 0 값을 대체

  

* ## Score

  * [교차검증](https://github.com/chloecmin/MultiCampus-AI-Engineering-based-on-Deep-Learning/blob/master/200924/%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D.md)



---



# 4. Breast Cancer Wisconsin

미완성....



