# AI

### regression
##### : 2차 회귀함수 y = 0.5x^2 + 1 에 대하여 파라미터를 추정하는 코드 작성 및 학습

###### 결과
![PBL_regression](https://github.com/de110/AI/assets/67581448/e6a245b1-925a-4936-b82a-90d5bc869932)

---
### classification
##### 주어진 입력에 대해 class를 나누는 코드

– Input : 날개 / 창문 / 바퀴

– Output : 비행기 / 자동차 / 자전거 / 기타

	[0, 0, 0] -> [0, 0, 0, 1]
	[0, 0, 1] -> [0, 0, 1, 0]
	[0, 1, 0] -> [0, 0, 0, 1]
	[0, 1, 1] -> [0, 1, 0, 0]
	[1, 0, 0] -> [0, 0, 0, 1]
	[1, 0, 1] -> [0, 0, 0, 1]
	[1, 1, 0] -> [1, 0, 0, 0]
	[1, 1, 1] -> [1, 0, 0, 0]

###### 결과
![PBL_classification](https://github.com/de110/AI/assets/67581448/ca1fada3-3af8-4d95-a4e0-4ad2824aaa15)


---

### MNIST

##### 텐서보드를 이용하여 MNIST 학습 진행 결과 출력

###### 결과

- 학습 손실값 결과 그래프

  ![PBL_MNIST](https://github.com/de110/AI/assets/67581448/82fedcb6-cdaf-4586-af70-6239a399402f)


---

### MNIST, CNN

##### MNIST를 CNN으로 학습/ 평가

- 100회 학습한 결과 이미지

- Accuracy
  
  ![accuracy](https://github.com/de110/AI/assets/67581448/4c311662-df41-4e6c-a649-ad1f13fef416)
	
- main graph
  
  ![main_graph](https://github.com/de110/AI/assets/67581448/2051c186-ca73-430b-b0d3-fbcc8c0e2a27)
	
- optimizer
  
  ![optimizer](https://github.com/de110/AI/assets/67581448/1d6f5cb7-3dc8-4a87-9e16-3f7ae9bb5db6)
