# 데이터 재구조화(pivot)



## 1. Series 재구조화

* `get()` : `loc()`함수와 같은 역할을 하여 시리즈의 일부를 참조한다.

  ```python
  seri = pd.Series(range(5), index=list('abcde'))
  
  seri.loc[['b', 'd']]
  seri.get(['b', 'd'])
  #두 함수의 결과는 같다
  ```



## 2. DataFrame의 재구조화

*`pivot_table`, `stack/unstack`, `melt`, `crosstab` 등 다양한 재구조화 방법이 있음.*

* `crosstab`   : 원하는 칼럼을 인덱스와 컬럼으로 지정해 재조합할 수 있다.

  - 요인별로 교차분석
  - 행, 열 요인 기준 별로 빈도수
  - 도수분포표/교차표 생성
  - 다중인덱스(다중레벨)로 구성 가능 

* `drop` : 칼럼 제거. 원본 데이터프레임에서는 제거되지 않는다.

* `del` : 칼럼 제거. 원본 데이터프레임에서 해당 컬럼을 제거한다.

  ```python
  #drop함수 사용법
  df.drop(['c4'], axis=1)
  
  #del함수 사용법
  del df['c4']
  ```

   

## 3. Numpy(배열) 재구조화

* ### `array` vs `asarray`
  * 공통점 : 배열을 생성한다
  * 차이점
  
  | array       | asarray      |
| :---------: | :----------: |
  | copy = __true__ |copy = __false__|
  | 복사본을 만들어서 저장 | 복사본없이 저장 |
  
  →  `asarray` 사용의 예외 : 다른 type(*ex. list*)의 데이터를 convert하기 위해 사용하는 경우는 반드시 새로운 구조를 만들어야 하므로 copy=false가 무시된다.
  → `asarray` 메모리 관리 : 같은 형태의 ndarray가 이미 메모리에 있다면 새로 생성하지 않고 기존 메모리에 있는 ndarray를 재사용한다.
  
  
  
* ### 행렬 
  - 요소 자동완성 함수 : `np.zeros()`, `np.ones()`, `np.empty()`  
  - 단위행렬 생성 함수 : `np.eye()`, `np.identity()`

  

* ### 비교연산
  ```python
  #x와 y값이 같냐?
  np.equal(x, y)
  #x와 y값이 크냐?
  np.greater(x, y)
  #x와 y값이 크거나 같냐?
  np.greater_equal(x, y)
  #x와 y값이 작냐?
  np.less(x, y)
  #x와 y값이 작거나 같냐?
  np.less_equal(x, y)
  #x와 y의 배열이 같냐?
  np.array_equal(x, y)
  ```




*  ### 논리연산
  
  ```python
  np.logical_and(a, b)
  np.logical_or(a, b)
  np.logical_xor(a, b)
  ```




* ### `astype` : 데이터 타입 재구조화를 위한 형 변환함수
  - 숫자형 : bool, 정수(int), 부동소수점(float), 복소수(complex)
  - 문자형 : string, object

  

* ### 소수점 버림, 내림, 올림
  ```python
  a = np.array([-4.62, -2.19, 1.57, 3.4, 0])
  
  np.trunc(a) #정수만 남김
  np.floor(a) #가장 가까운  작은 정수로 내림
  np.ceil(a) #가장 가까운 큰 정수로 올림
  ```

  

* ### 배열 간 연산

    * `keepdims` : 2차원 이상의 배열에서 사칙연산 후 차원유지를 위한 옵션
    * `nanprod`, `nansum` : null값을 포함한 연산. (곱셈에서는 nan=1, 덧셈에서는 nan=0으로 취급하여 연산)

  | **연산** | **함수** |
  | :--------: | ---------------------- |
  | 곱셈     | prod()<br>nanprod() |
  | 덧셈     | sum()<br>nansum() |
  | 누적합   | cumsum() |
  | 차분     | diff(*배열*, n) : 몇 차 차분을 할 것인지 옵션 |
| 절대값 | abs()<br>fabs() |
  | 나머지 | mod() |
  | 나머지와 몫 | modf() |
  | 부호 | sign() |
  
  
  
* ### 지수함수와 로그함수
    
    지수함수와 로그함수는 서로 역함수의 관계.

    * 지수함수 : `exp()`
    ![지수함수 그래프](https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F274F6F3358E24E7D0EEFE1)
    
    * 로그함수 : `np.log()`
    
      - 로그변환 : 오른쪽으로 크게 치우쳐진 멱함수 분호를 정규분포로 변환한다.
      - 멱함수(power law) : 한 수가 다른 수의 거듭제곱으로 표현되는 두 수의 함수적 관계
    
      ![로그함수 그래프](https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile30.uf.tistory.com%2Fimage%2F2652D93358E24E7E2E9000)




* ### 삼각함수

    - 주기적인 파동 함수(주파수)에서 sin함수. 벡터 내적에서 cos함수, 퓨리에 변환
    - degree?원을 360도로 표기
    - radian? 부채꼴의 호의 길이와 반지름 길이가 같을때의 각도를 1radian
    - 180도 = 파이 라디안
    - 1도 =파이 라디안 / 180
    - 1라디안 = 180도 / 파이 = 57.xx

    >__삼각함수의 역함수__
    >- 1/sin함수=csc함수
    >- 1/cos함수=sec함수
    >- 1/tan함수=cot함수

    

* ### 차원변형

    * `reshape` : 1차원 → 다차원
    * `ravel`, `flatten` : 다차원 → 1차원

    

*  ### 두 배열의 연결

    * 1차원 배열 

      ```python
      # 좌우로 연결
      np.r_[a,b]
      np.hstack([a,b])
      np.concatenate((a,b))
      
      # 상하로 연결
      np.r_[[a],[b]] #a,b 를 []사용 -> 1차원 배열 -> 연결
      np.vstack([a,b])
      ```

    *  2차원 배열

      ```python
      np.concatenate((a,b), axis=1)
      np.concatenate((a,b), axis=0)
      np.c_[a,b]
      np.column_stack([a,b])
      np.concatenate((a.T,b.T), axis=1)
      ```

    

* ### 정렬


    * `x.sort()` : 정렬 결과가 배열에 그대로 적용
    
    * `sorted(x)` : 정렬 결과의 복사본으로 원본은 그대로 유지.
    
        ※ *if `sorted(x)`의 결과를 원본에 적용하고 싶다면 `x = sorted(x)`로 변수에 직접 대입해야 함.*
    
    * `argsort()` : 정렬할 때 순서인덱스를 배열 요소의 순서대로 담은 배열 반환
    
        ```python
        x=np.array([4,2,6,3,9,5,10])
        
        print(np.argsort(x)) #결과값 : [1 3 0 5 2 4 6]
        print(x[np.argsort(x)]) #결과값 : 오름차순한 결과 -> [ 2  3  4  5  6  9 10]
        ```


​        

