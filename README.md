# week3-variable
1. 사용자로부터 문자를 입력받아 입력받은 문자가 "Department of Computer Engineering, Hanbat National University 2023 Python programming"에 포함될 경우 True, 포함되지 않을 경우 False를 출력하는 프로그램을 작성하시오. (단, If, for 사용하지 않고 작성)  
  
- input : Hanbat
- output : True

2. 변수 num1을 15를 선언하고 사용자로부터 정수 num2를 입력받아 두 수의 합을 구하시오.

- input : 18
- output : 33


3. 사용자로부터 정수를 입력받고 해당 변수를 float 형태로 변환하여 출력하시오.

- input : 97
- output : 97.0

4. 사용자로부터 3개의 실수를 입력 받고, 평균 값을 계산하여 소숫점 3자리까지 출력하는 프로그램을 작성하시오.
(단, numpy.mean(), for를 사용하지 않고 작성)

- input : 5, 7, 32
- output 14.667


5. 사용자로부터 반지름을 입력받아 원의 넓이를 계산한 값을 정수 변수 circle에 저장한 후 circle의 자료형과 값을 출력하는 프로그램을 작성하시오.
(pi는 3.141592를 사용함)

- input : 7.4
- output : <class 'int'> 172


6. 사용자로부터 입력받은 금액을 동전(500, 100, 50, 10, 1)으로 반환할 때, 동전의 수를 출력하는 프로그램을 작성하시오.
(단, 금액이 높은 순서대로 반환함, if, for, list를 사용하지 않고 작성)

- input : 37420
- ouput :

  500 : 74개
  100 : 4개
  50 : 0개
  10 : 2개
  1 : 0개


7. 사용자로부터 3개의 실수를 입력받아 첫 번째로 입력받은 실수가 가장 큰 값일 경우 True를 출력하는 프로그램을 작성하시오.
(단, if, for, list를 사용하지 않고 작성)

- input : 30 20 10
- output : True

8. 사용자로부터 문자를 입력받아 앞의 5글자만 출력하는 프로그램을 작성하시오.
(단, 입력받는 값은 5자 이상임, if, for를 사용하지 않음)

- input : Hanbat National
- output : Hanba


9. 1부터 10까지의 랜덤값을 갖는 Tuple A를 선언하고 A와 첫 번째 요솟값이 같거나 더 클경우 True를 출력하는 프로그램을 작성하시오.
(단, if를 사용하지 않음)  
  

10. 사용자로부터 두 개의 값을 입력받아 두 개의 값이 세 번 반복되어 저장된 튜플을 구성하고 튜플의 길이와 값을 출력하는 프로그램을 작성하시오.
(hint : 튜플의 곱셈)

- input : 13 15
- output : 6 (13, 15, 13, 15, 13, 15)


11. 주어진 파일 fescape.txt의 내용을 읽고 이스케이프 코드를 활용해 다음 output을 출력하는 프로그램을 작성하시오. 
(단, print를 한 번만 사용하여 작성, 문자열(Hanbat National University) 앞에 tab 간격을 사용함)

- fescape.txt :   
  Hanbat National University 

- output :  
<br/>  “fescape.txt”  
<br/><t/>	  Hanbat National University
 
12. 문자열 포맷팅을 활용하여 "*"로 트리형태를 출력하는 프로그램을 작성하시오.
(단, for를 사용하지 않음, 트리는 최소 5줄 이상으로 구성)
(hint : 포맷팅을 활용하여 가운데 정렬, 문자열 곱셈)

- output : 
<br/>"　　　　　 *　　　 "
<br/>"　　　　　***　　　"
<br/>"　　　　 *****　　 "
<br/>"　　　　*******　　"
<br/>"　　　 *********　 "
