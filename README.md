<h1>Algorithm</h1>

Baekjoon Algorithm Solution in Python

-------------------------------------

Baekjoon Algorithm(acmicpc.net)
- DP
- Tree
- MST
- Topological Sorting
- union-find
- search
- string
-------------------------------------
<h1>String</h1>

KMP Algorithm
- 각 시점에서 접미사, 접두사가 같아지는 최대 길이를 구해서 테이블 구성
- 이를 이용해서 한 시점에서 문자열 비교가 틀린 경우, 비교를 다시 어디서부터 시작할 지 구할 수 있음.
- 핵심은 이전 단계까지 비교했던 것을 재사용한다는 점
- 실패 함수 구하는 알고리즘도 KMP 알고리즘 사용

<h2> 동작 과정 </h2> <br>
![image](https://user-images.githubusercontent.com/76891875/110346019-802d1f80-8072-11eb-9ee1-0dc14df9d155.png)

<h2> 실패 함수 구하는 예시 </h2> <br>
![image](https://user-images.githubusercontent.com/76891875/110342731-15c6b000-806f-11eb-9bec-ceb0e1ab5618.png)

출처 : https://bowbowbow.tistory.com/6
