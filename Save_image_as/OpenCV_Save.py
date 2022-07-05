import cv2

# 사진을 불러오는데 흑백으로 불러온다
img1 = cv2.imread('D:\\Sources\\OpenCV_Python\\imgae\\plane.jpg', cv2.IMREAD_GRAYSCALE)

# 다른 이름으로 저장하기 위해 cv2.imwrite()함수를 사용
cv2.imwrite('D:\\Sources\\OpenCV_Python\\imgae\\save_plane.jpg', img1)

# 파이썬에서 파일을 불러올때 
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape 에러
# 발생시 \ -> \\ 로 해결