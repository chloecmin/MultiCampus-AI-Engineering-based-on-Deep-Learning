# CNN 알고리즘



## 1. LeNet

- 활성화 함수 : Tanh사용

- Average pooling적용

- pooling(풀링)  [참고](https://technical-support.tistory.com/65)

압축하여 연산을 줄이는 기법

image data를 작은 size의 image로 줄이는 과정

> Convolution을 거쳐서 나온 activation maps이 있을 때,
>
> 이를 이루는 convolution layer을 resizing하여 새로운 layer를 얻는 것

![Image for post](https://miro.medium.com/max/500/1*_aNCr6CtNk0Y45I9Ygs3Mg.png)

**Pooling의 효과**

1. parameter를 줄이기 때문에, 해당 network의 표현력이 줄어들어 **Overfitting을 억제**

2. Parameter를 줄이므로, 그만큼 비례하여 computation이 줄어들어 **hardware resource(energy)**를 절약하고 **speedup**



**Pooling의 특징**

1. training을 통해 train되어야 할 parameter가 없다.

2. Pooling의 결과는 channel 수에는 영향이 없으므로 channel 수는 유지된다. (independent)

3. input feature map에 변화(shift)가 있어도 pooling의 결과는 변화가 적다. (robustness)



## 2. AlexNet

[ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)

- Hinton : 딥러닝의 아버지

- 2개의 GPU를 이용하여 병렬연산 (ex) 첫번째 layer에는 1개의 GPU당 48개의 필터 사용) => 2개의 특성맵

- 8개의 layer(5: convortional layer /3: fully connected layer)

- Stride : 4

  > **Stride** 는 Filter 의 이동 간격을 조절하는 파라미터 입니다. 이 값이 커지게 되면 결과 데이터의 사이즈가 작아지게 됩니다

- 활성화 함수

  - convolutional layer에는 내부적으로 ReLu 적용(정확도와 속도 성능이 높음)
  - fully connected layer의 마지막 layer은 softmax 적용

- Dropout : overfiitting을 피하기 위한 방법 -> training할 때 일부 노드를 강제로 0으로 설정(신호 전달 안되도록)

- Max pooling (Overlapping pooling) 적용 : stride를 줄여 pooling 시에 겹치는 부분이 생기도록

- augmentation : 이미지 증식 => 데이터 양이 적을 때 오버피팅을 방지하기 위해 수행하여 데이터양을 늘린다.

  - 대칭이미지(mirror)
  - Crops : 이미지 자르기
  - Transation
  - shift
  - Zoom In/ Zoom Out
  - Greyscale.....



## 3. VGGNET

[Return of the Devil in the Details: Delving Deep into Convolutional Nets](https://arxiv.org/pdf/1405.3531.pdf)

![image-20201117103941625](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20201117103941625.png)

> The input image size is 224 × 224 x 3
>
> stride : 4
>
> padding : 나의 첫 머신러닝 p.236 참고
>
> conv1의 필터 개수 : 64 / conv1의 필터 크기 : 11x11x3(채널 수)
>
> conv2의 필터 개수 : 256 / conv2의 필터크기: 5x5x64(conv1의 필터개수)



* 입력이미지 크기 : WxH

  zero padding : P

  필터 크기 : Fh x Fw

  stride : S

  > `feature map`**의 넓이와 높이를 구하는 공식**
  >
  > - 높이 : (H+2P-Fh/S)+1
  > - 넓이 : (H+2P-Fw/S)+1
  >
  > *교재 p.176인가..? 참고*



## 4. VGG-16, VGG-19

[Very deep convolutional networks for large-scale image recognition](https://arxiv.org/pdf/1409.1556.pdf)
[논문 리뷰](https://medium.com/@msmapark2/vgg16-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-very-deep-convolutional-networks-for-large-scale-image-recognition-6f748235242a)
[Reference](https://keras.io/api/applications/vgg/)

- Layer가 16개
- input image : 224x224x3
- convolution filter : 3x3으로 고정

=> 필터의 크기를 줄이고 깊이를 깊게(?)

=> 분류 에러가 감소 : layer가 많아질 수록 성능이 좋아진다.



## 5. GoogLeNet

[Going Deeper with Convolutions](https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/43022.pdf)
[논문 리뷰](https://leedakyeong.tistory.com/entry/%EB%85%BC%EB%AC%B8-GoogleNet-Inception-%EB%A6%AC%EB%B7%B0-Going-deeper-with-convolutions-1)

- Inception이라고 부름.
- 22개 층의 Layer

> `Input` : 14x14사이즈의 240장의 특성맵
> `필터` : 48개 (사이즈 : 5x5 => 5x5*240)
> `zero padding` : 2
> `stride` : 1 일 때
> `Output` : 24장의 14x14의 특성맵 생성



## 6. ResNet

[Deep Residual Learning for Image Recognition](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)
[논문리뷰](https://jxnjxn.tistory.com/22)


## 7. SeNet
[Squeeze-and-Excitation Networks](https://arxiv.org/pdf/1709.01507.pdf)
[논문리뷰](https://jayhey.github.io/deep%20learning/2018/07/18/SENet/)

- 필터의 중요도를 반영



---



# 전이학습(transfer learning)

- 정의 : 미리 훈련된 모델(pretrained model)을 사용하는 것
- [전이학습을 활용한 빈곤지도](http://sustain.stanford.edu/predicting-poverty/)



---



# 강화학습

- 시행착오(Trial and Error)를 통해 학습하는 방법 
- 실수와 보상을 통해 학습을 하여 목표를 찾아가는 알고리즘
- 보상(Reward)이라는 개념을 사용하여 가중치와 편향을 학습하는 것
- 목적은 최적의 행동양식 또는 정책을 학습하는 것

