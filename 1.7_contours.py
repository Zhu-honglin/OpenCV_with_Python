import cv2 as cv
import numpy as np

'''
边缘检测主要是通过一些手段检测数字图像中明暗变化剧烈（即梯度变化比较大）像素点，偏向于图像中像素点的变化。如canny边缘检测，结果通常保存在和源图片一样尺寸和类型的边缘图中。
轮廓检测指检测图像中的对象边界，更偏向于关注上层语义对象。如OpenCV中的findContours()函数， 它会得到每一个轮廓并以点向量方式存储，除此也得到一个图像的拓扑信息，即一个轮廓的后一个轮廓、前一个轮廓、父轮廓和内嵌轮廓的索引编号。
'''

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# 直接用阈值函数获得二值化后的图像，扔进findContours后也可以做轮廓检测。
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# findContours函数可以参考文章（https://blog.csdn.net/dcrmg/article/details/51987348）
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)