# [Gold IV] 사과나무 - 2987 

[문제 링크](https://www.acmicpc.net/problem/2987) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

기하학, 구현, 수학, 볼록 다각형 내부의 점 판정, 다각형의 넓이

### 제출 일자

2025년 6월 22일 11:12:19

### 문제 설명

<p>백준이는 사과나무가 N개 심어져있는 땅의 일부를 구매했다. 백준이가 구매한 땅은 삼각형이다. 따라서, 어떤 사과나무가 백준이의 것인지 알기가 힘들었다.</p>

<p>백준이 땅의 꼭짓점 좌표와 사과나무의 좌표가 주어졌을 때, 백준이 땅의 넓이와 백준이의 사과나무의 개수를 구하는 프로그램을 작성하시오.</p>

<p>만약, 어떤 사과나무가 땅의 경계선에 걸쳐있다면, 이것은 백준이 사과나무이다.</p>

<p>(x<sub>A</sub>,y<sub>A</sub>), (x<sub>B</sub>,y<sub>B</sub>), (x<sub>C</sub>,y<sub>C</sub>) 로 이루어진 삼각형의 넓이는 다음과 같이 구할 수 있다.</p>

<p>|x<sub>A</sub>(y<sub>B</sub>-y<sub>C</sub>)+x<sub>B</sub>(y<sub>C</sub>-y<sub>A</sub>)+x<sub>C</sub>(y<sub>A</sub>-y<sub>B</sub>)| / 2</p>

### 입력 

 <p>처음 세 개의 줄은 삼각형의 꼭짓점 좌표이다. 다음 줄에는 사과나무의 개수 N이 주어진다. (1 ≤ N ≤ 100). 다음 N개의 줄에는 사과나무의 좌표가 주어진다.</p>

<p>모든 좌표는 1,000보다 작거나 같은 양의 정수이고, 공백으로 구분되어져 있다.</p>

### 출력 

 <p>첫째 줄에는 백준이 땅의 넓이를 소수점 첫째자리까지 출력하고, 둘째 줄에는 백준이의 사과나무 개수를 출력한다.</p>

