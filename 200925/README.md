# 1. 문자(텍스트)형 데이터 전처리



 1. `레이블 인코딩` : 순서가 의미있는 카테고리일 때

    *ex) 학점 :  A->1, B->2, C->3... (숫자가 커질수록 학점이 낮음)*

    ```python
    from sklearn.preprocessing import LabelEncoder
    ```



 2. `원핫 인코딩` : 순서가 의미없는 카테고리일 때

    *ex) 지역 :  서울=1000, 부산=0100, 제주=0010, 강릉=0001*

    ```python
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    
    #step1 : 원핫 인코딩을 하기 전에 모든 문자열을 숫자로 변환
    encorder = LabelEncoder()
    encorder.fit(items)
    labels = encorder.transform(items)
    
    #step2 : 숫자로 변환된 데이터(2차원)에 대한 원핫인코딩
    labels = labels.reshape(-1, 1)
    ohencorder = OneHotEncoder()
    labels = ohencorder.fit_transform(labels)
    print(labels.toarray())
    ```



 3. `get_dummies`함수 : 원핫 인코딩과 같은 원리이지만 한번에 숫자형으로 변형

    ```python
    df = pd.DataFrame(['tv', '냉장고', '에어컨', '에어컨', '전자레인지'],
                     columns=['item'])
    pd.get_dummies(df)
    ```

    

---



# 2. DecisionTree와 RandomForest의 특징



 1. 변수의 스케일링(표준화, 정규화)를 하지 않아도 된다.

 2. 연속형, 바이너리형 등 서로 다른 형태의 데이터들이 혼합되어 있어도 잘 동작한다.

 3. 가지치기가 필요하다. (일반화를 위해 -> 오버피팅(과적합)을 막기 위해)

    

---



# 3. Breast Cancer (랜덤포레스트)



 * ## Data Processing

 1. 하나의 데이터만 주어졌을 때 Train 데이터와 Test 데이터로 분리하기

    ```python
    from sklearn.model_selection import train_test_split
    
    xTrain,xTest,yTrain,yTest = train_test_split(xdata, ydata, test_size=0.25, random_state=0) #주로 70:30으로 Train/Test데이터를 분리한다.
    ```

 2. `StandardScaler` : 평균이 0, 표준편차가 1이 되도록 변환

    ```python
    from sklearn.preprocessing import StandardScaler
    
    sc = StandardScaler()
    xTrain = sc.fit_transform(xTrain)
    xTest = sc.fit_transform(xTest)
    ```

   

* ## RandomForest 모델링

  가지치기의 기준 : `GridSearch`를 이용하여 최적의 계수를 찾는것이 좋음

  ```python
  criterion='entropy' #엔트로피
  criterion='jini' #지니계수
  ```

  

* ## 모델평가(분류분석)

 1. Confusion Matrix : [모델평가도]()

    ```python
    from sklearn.metrics import confusion_matrix
    confusion_matrix(yTest, yPred)
    ```

 2. 정확도
    ```python
    from sklearn.metrics import accuracy_score
    accuracy_score(yTest, yPred)
    ```


---



# 4. House Price