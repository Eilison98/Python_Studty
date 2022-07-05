import cv2

# 첫번째 이미지 불러오기
img1 = cv2.imread('D:\\Sources\\OpenCV_Python\\imgae\\plane.jpg')

# 첫번째 이미지 사진크기 조절
img1 = cv2.resize(img1, (620, 500))

# 두번째 이미지 불러오기
img2 = cv2.imread('D:\\Sources\\OpenCV_Python\\imgae\\save_plane.jpg')

# 두번째 이미지 사진크기 조절
img2 = cv2.resize(img2, (620, 500))

# 이미지를 수평 방향으로 붙여 리턴
img3 = cv2.hconcat([img1, img2])

# img3으로 두사진을 붙여 보여준다
cv2.imshow('image3', img3)

# 사용자의 입력을 기다린다
cv2.waitKey(0)

# 실행중인 프로그램 종료시 모든 창을 닫을때 사용
cv2.destroyAllWindows()