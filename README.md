# OpenCV_Python

<br/>

- Img 파일 출력해보기 ([링크](https://github.com/Eilison98/OpenCV_Python/tree/main/Day_01#img-%ED%8C%8C%EC%9D%BC-%EC%B6%9C%EB%A0%A5%ED%95%B4%EB%B3%B4%EA%B8%B0))

<br/>

### IMREAD()함수의 2번째 인자 값 플래그 타입(ENUM) ###

| flags 타입 | 내용 |
|:---:|:---:|
|IMREAD_COLOR|별도로 지정하지 않은 경우 기본값, 3채널 BGR 컬러 이미지로 반환|
|IMREAD_GRAYSCALE|단일 채널 회색조 이미지로 반환(내부 코덱 변환)|
|IMREAD_UNCHANGED|이미지 원본 그대로 반환|
|IMREAD_ANYCOLOR|설정된 경우 가능한 모든 색상 형식으로 이미지를 읽음|
|IMREAD_REDUCED_COLOR_2|설정된 경우 이미지를 3채널 BGR컬러 이미지로 변환하고 이미지 크기를 1/2로 줄인다. 4를 넣을경우 1/4로 이미지 크기를 줄인다|
|IMREAD_REDUCED_GRAYSCALE_2|설정된 경우 항상 이미지를 단일 채널 회색조 이미지로 변환하고 이미지 크기를 1/2로 줄인다. 4를 넣을경우 1/4로 이미지 크기를 줄인다|
