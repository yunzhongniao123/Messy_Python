# -*- coding:utf-8 -*-

import cv2
import numpy as np


# 计算图像矩阵FFT
def FFT2Image(src):
    r, c = src.shape[:2]
    # 得到FFT的最优扩充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 边缘扩充，扩充值为0
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = src
    # 快速傅里叶变换
    cv2.dft(fft2, fft2, cv2.DFT_COMPLEX_OUTPUT)
    return fft2


def FFTtest():
    src = cv2.imread('../Datas/colorG.bmp')
    image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    fft2 = FFT2Image(image)
    # 傅里叶逆变换
    ifft2 = np.zeros(fft2.shape[:2], np.float32)
    cv2.dft(fft2, ifft2, cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)
    # 裁剪
    img = np.copy(ifft2[:image.shape[0], :image.shape[1]])
    # 裁剪后image等于img，图像相减判断是否相同
    cv2.imwrite('result.bmp', img)
    print(np.max(image - img))


if __name__ == '__main__':
    FFTtest()
