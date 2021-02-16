import  cv2 as cv

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

#读取图像
cat_img = cv.imread('Resources/Photos/cat_large.jpg')#由于图像大导致超出屏幕
rescaleFrame_img = rescaleFrame(cat_img)
cv.imshow('cat_img', cat_img)
cv.imshow('rescaleFrame_img', rescaleFrame_img)
cv.waitKey(0)

#读取视频
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    #print(isTrue)#帧读完之后报False
    if isTrue:
        re_frame = rescaleFrame(frame,scale=0.9)
        cv.imshow('Video', re_frame)
        #cv.waitKey(20)
        if cv.waitKey(20) & 0xff == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()