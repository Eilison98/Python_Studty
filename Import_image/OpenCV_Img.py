import cv2

# 사진을 불러오는데 컬러로 불러오지만 이미지 크기를 1/4로 줄여서 출력
img1 = cv2.imread('plane.jpg', cv2.IMREAD_REDUCED_COLOR_4)

# 이미지파일 출력
print(type(img1))

# 이미지를 출력하기위한 윈도우 창을 호출하기위해 사용
cv2.imshow('image1', img1)

# 사용자의 입력을 기다려주는 함수
# 밑의 코드인 destroyAllWindows()함수를 실행하기 위해 기다린다고 생각하면 됨
cv2.waitKey(0)

# 실행중인 프로그램 종료시 모든 창을 닫을때 사용
cv2.destroyAllWindows()