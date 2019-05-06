#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:love_cat
import cv2

# 接收两个参数，一个是文件名，一个值，如果值为1，接收的是彩色图片，如果值为零，接受的是灰度图片。会有一个返回值，表示返回的图片内容
img = cv2.imread('test.png',1)

(a, b, c ) = img[400, 400];
print(a, b ,c );

for i in range(1, 100):
    img[i, i] = (255, 0, 0);


# 接收两个参数，一个是窗体名称，另一个是要显示的内容
cv2.imshow('mashiro',img)

rgb565 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);

cv2.imshow("rgb565", rgb565 );

cv2.imwrite("test_1.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9]);


imginfo = img.shape;
height = imginfo[0];
width = imginfo[1];
mode = imginfo[2];

print( imginfo );

dstH = int(height * 0.5)
dstW = int(width * 0.5);

dst = cv2.resize(img, (dstW, dstH))
cv2.imshow("resize", dst)


# 将程序暂停，只有这样，才能看到图片,否则图片会一闪而过因为程序结束了，如果time.sleep()的话，会卡住
cv2.waitKey(0)


