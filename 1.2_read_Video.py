import  cv2 as cv

#读取视频
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    #print(isTrue)#帧读完之后报False
    if isTrue:
        cv.imshow('Video', frame)
        #cv.waitKey(20)
        if cv.waitKey(20) & 0xff == ord('d'):#输入d退出
            break
    else:
        break

capture.release()
cv.destroyAllWindows()