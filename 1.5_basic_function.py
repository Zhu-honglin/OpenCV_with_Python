import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# 转换为灰度图
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 模糊
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 边缘检查
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# 扩大
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# 缩小
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# 设置大小
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 选择区域
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)