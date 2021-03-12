# kor_grammer
## 한글 프로그래밍 언어를 위한 문법 처리기

## 1. 서론
우리 우수한 한글을 사용하여, 어린 [아희](http://puzzlet.org/doc/aheui/jsaheui_ko.html) 들도 사용할수 있는 교육적 목적의 프로그래밍 언어를 위한, 한글 문법 처리기입니다.

```python
print("Hello, world!")
```

```python
출력("안녕, 세상!")  
("안녕, 세상!")출력
```



`grammer.py`를 수정하여 본인만의 프로그래밍 언어를 설계할수도 있습니다.

## 2. 예시

```python
#소수 판별하기

n = input("수 : ")

is_prime = True

for k in range(2, n):
  if n % k == 0:
    is_prime = False

if is_prime:
  print("소수입니다")
else:
  print("소수가 아닙니다")
```

```python
#소수 판별하기

변수 정수 정의
정수는 입력받기("수 : ")

변수 소수인가 정의
소수인가는 참

(2, 정수)범위의 나눔에 대해 {
  만약 정수 % 나눔 == 0 이면 {
    소수인가는 거짓
  }
}
만약 소수인가 라면{
  ("소수입니다")출력하기
}
아니면{
  ("소수가 아닙니다")출력하기
}
```
