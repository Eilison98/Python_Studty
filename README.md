# OpenCV_Python

<br/>

- Img 파일 출력해보기 ([링크](https://github.com/Eilison98/OpenCV_Python/tree/main/Import_image#img-%ED%8C%8C%EC%9D%BC-%EC%B6%9C%EB%A0%A5%ED%95%B4%EB%B3%B4%EA%B8%B0))
- Img 파일 다른이름으로 저장 ([링크](https://github.com/Eilison98/OpenCV_Python/tree/main/Save_image_as#img-%ED%8C%8C%EC%9D%BC-%EB%8B%A4%EB%A5%B8-%EC%9D%B4%EB%A6%84%EC%9C%BC%EB%A1%9C-%EC%A0%80%EC%9E%A5))
- Img 파일 붙이기 ([링크](https://github.com/Eilison98/OpenCV_Python/tree/main/Paste_image#img-%ED%8C%8C%EC%9D%BC-%EB%B6%99%EC%9D%B4%EA%B8%B0))
- Img 파일 밝기조절 ([링크](https://github.com/Eilison98/OpenCV_Python/tree/main/Adjust_image_brightness#img-%ED%8C%8C%EC%9D%BC-%EB%B0%9D%EA%B8%B0-%EC%A1%B0%EC%A0%88))
- 동영상파일 얼굴인식, ([링크](https://github.com/Eilison98/OpenCV_Python/tree/main/Face_Recognition#%EC%98%81%EC%83%81-%ED%83%90%EC%A7%80%EA%B8%B0-%EC%82%AC%EC%A7%84-%ED%83%90%EC%A7%80%EA%B8%B0))

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
