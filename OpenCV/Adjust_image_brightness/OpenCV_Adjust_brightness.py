import cv2

# 이미지 파일 불러오기
img1 = cv2.imread('D:\\Sources\\OpenCV_Python\\imgae\\plane.jpg')

# 불러온 이미지 파일 크지조절
img1 = cv2.resize(img1, (500, 400))

# 이미지 밝게
img2 = img1 + 50

# 이미지 어둡게
img3 = img1 - 50

# 3개의 이미지를 수평 방향으로 붙인다
img4 = cv2.hconcat([img1, img2, img3])

# 이미지를 보여준다
cv2.imshow('image3', img4)

# 사용자의 입력을 기다린다
cv2.waitKey(0)

# 실행중인 프로그램 종료시 모든 창을 닫을때 사용
cv2.destroyAllWindows()