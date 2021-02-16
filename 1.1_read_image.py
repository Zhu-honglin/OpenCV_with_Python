import  cv2 as cv

#读取图像
cat_img = cv.imread('Resources/Photos/cat.jpg')
# cat_img = cv.imread('Resources/Photos/cat_large.jpg')#由于图像大导致超出屏幕
#在新窗口显示图像
cv.imshow('Cat', cat_img)
#打印下长宽和通道数(427, 640, 3)
print(cat_img.shape)
#延迟显示
cv.waitKey(0)


