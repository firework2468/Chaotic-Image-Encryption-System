import cv2
import math
import numpy as np
from scipy.integrate import odeint
from functions import *
import requests
import os

def decrypt(savePath, image_url, key):
    os.mkdir(savePath)
    "---获得密钥---"
    Key = list(map(float, key))
    if (image_url.startswith("http")):
        file = requests.get(image_url)
        image = cv2.imdecode(np.frombuffer(file.content, np.uint8), 1)
    else:
        image = cv2.imread(image_url)
    I1 = image[:, :, 0]
    I2 = image[:, :, 1]
    I3 = image[:, :, 2]
    length = image.shape[0]
    width = image.shape[1]
    SUM = length * width
    size = int(Key[7])  # 加密时的分块大小

    "---logistic映射产生两个序列Kx和Ky---"
    u = 3.9999
    x1 = Key[1]
    x2 = Key[2]
    Kx = np.zeros([length + 1000])
    Ky = np.zeros([width + 1000])
    Kx[0] = x1
    Ky[0] = x2
    for i in range(length + 999):
        Kx[i + 1] = u * Kx[i] * (1 - Kx[i])
    for i in range(width + 999):
        Ky[i + 1] = u * Ky[i] * (1 - Ky[i])
    Kx = Kx[1000: len(Kx)]
    Ky = Ky[1000: len(Ky)]
    # 对Kx和Ky两个序列降序排序，并用索引序列Ux和Uy记录每个元素在排序之前的位置
    Ux = np.argsort(-Kx)
    Uy = np.argsort(-Ky)

    "---根据索引序列Ux和Uy对I1,I2,I3三个图像矩阵进行行列置换---"
    for i in range(width - 1, -1, -1):
        temp1 = np.copy(I1[:, i])
        I1[:, i] = I1[:, Uy[i]]
        I1[:, Uy[i]] = temp1
        temp2 = np.copy(I2[:, i])
        I2[:, i] = I2[:, Uy[i]]
        I2[:, Uy[i]] = temp2
        temp3 = np.copy(I3[:, i])
        I3[:, i] = I3[:, Uy[i]]
        I3[:, Uy[i]] = temp3

    for i in range(length - 1, -1, -1):
        temp1 = np.copy(I1[i, :])
        I1[i, :] = I1[Ux[i], :]
        I1[Ux[i], :] = temp1
        temp2 = np.copy(I2[i, :])
        I2[i, :] = I2[Ux[i], :]
        I2[Ux[i], :] = temp2
        temp3 = np.copy(I3[i, :])
        I3[i, :] = I3[Ux[i], :]
        I3[Ux[i], :] = temp3

    "---Logistic映射产生混沌序列并转化为二维矩阵H---"
    x0 = Key[0]
    p = np.zeros([SUM + 1000])
    p[0] = x0
    for i in range(SUM + 999):
        p[i + 1] = u * p[i] * (1 - p[i])
    p = p[1000: len(p)]
    p = np.fmod(np.round(p * pow(10, 4)), 256)
    H = p.reshape(length, width)

    "---超混沌系统产生产生四个序列X,Y,Z,W---"
    # 设置初值
    X0 = Key[3]
    Y0 = Key[4]
    Z0 = Key[5]
    W0 = Key[6]
    piece = int(SUM / (size * size))  # 块的个数

    # 根据初值，用Runge-Kutta法求解超混沌系统，得到四个混沌序列
    def func(L, time, a, b, c, d, r):
        x, y, z, w = L  # 位置矢量L
        return np.array([a * (y - x) + w, d * x - x * z + c * y, x * y - b * z, y * z + r * w])  # 超混沌系统公式

    time = np.arange(0, 500, 500 / (piece + 3000))  # 时间点
    A = odeint(func, (X0, Y0, Z0, W0), time, args=(35, 3, 12, 7, 0.6))  # 使用odeint求解
    # 四个长度为piece的序列X,Y,Z,W
    X = A[:, 0]
    X = X[3000: len(X)]  # 去除前3000项，获得更好的随机性
    X = np.abs(X)
    Y = A[:, 1]
    Y = Y[3000: len(Y)]
    Y = np.abs(Y)
    Z = A[:, 2]
    Z = Z[3000: len(Z)]
    Z = np.abs(Z)
    W = A[:, 3]
    W = W[3000: len(W)]
    W = np.abs(W)

    "---四个序列X,Y,Z,W中的元素转换---"
    i = 0
    for i in range(piece):
        X[i] = math.fmod(np.round(X[i] * pow(10, 4)), 8) + 1
        Y[i] = math.fmod(np.round(Y[i] * pow(10, 4)), 8) + 1
        Z[i] = math.fmod(np.round(Z[i] * pow(10, 4)), 4) + 1
        W[i] = math.fmod(np.round(W[i] * pow(10, 4)), 8) + 1
    Z[(Z == 1)] = 5  # 加减法互换
    Z[(Z == 2)] = 1
    Z[(Z == 5)] = 2

    "---矩阵I1,I2,I3和混沌矩阵H分别分块,并以子块为单位进行DNA编码和DNA运算,最终求得R,G,B三个图像矩阵---"
    B = np.zeros([length, width])
    G = np.zeros([length, width])
    R = np.zeros([length, width])
    lnum = length / size  # 行有lnum块
    wnum = width / size  # 列有wnum块
    for i in range(piece, 1, -1):
        # 加密时图像最后是有Wi决定的DNA解码方式，所以这里采用Wi决定DNA编码方式
        Q1_B = dna_code(divide(size, I1, i), W[i - 1])
        Q1_G = dna_code(divide(size, I2, i), W[i - 1])
        Q1_R = dna_code(divide(size, I3, i), W[i - 1])
        # 找到上一个子块
        tempB_Q = dna_code(divide(size, I1, i - 1), W[i - 2])
        tempG_Q = dna_code(divide(size, I2, i - 1), W[i - 2])
        tempR_Q = dna_code(divide(size, I3, i - 1), W[i - 2])
        # 与上一个子块逆运算
        B_Q = dna_operation(Q1_B, tempB_Q, Z[i - 1])
        G_Q = dna_operation(Q1_G, tempG_Q, Z[i - 1])
        R_Q = dna_operation(Q1_R, tempR_Q, Z[i - 1])
        # 对H的每一个分块按Y对应的序号进行DNA编码
        Q2 = dna_code(divide(size, H, i), Y[i - 1])
        # 与Q2进行逆运算
        finB_Q = dna_operation(B_Q, Q2, Z[i - 1])
        finG_Q = dna_operation(G_Q, Q2, Z[i - 1])
        finR_Q = dna_operation(R_Q, Q2, Z[i - 1])
        # 求第i个子块在完整矩阵中的x，y坐标
        x = int(math.floor(i / lnum) + 1)
        y = int(math.fmod(i, wnum))
        if y == 0:
            x = x - 1
            y = wnum
        # 将每一子块以Xi对应的解码方式解码，并合并成在R,G,B三个图像矩阵中
        B[int(size * (x - 1)): int(size * x), int(size * (y - 1)): int(size * y)] = dna_decode(finB_Q, X[i - 1])
        G[int(size * (x - 1)): int(size * x), int(size * (y - 1)): int(size * y)] = dna_decode(finG_Q, X[i - 1])
        R[int(size * (x - 1)): int(size * x), int(size * (y - 1)): int(size * y)] = dna_decode(finR_Q, X[i - 1])
    # 取矩阵I1,I2,I3第一子块并DNA编码
    Q1_B = dna_code(divide(size, I1, 1), W[0])
    Q1_G = dna_code(divide(size, I2, 1), W[0])
    Q1_R = dna_code(divide(size, I3, 1), W[0])
    # 取混沌矩阵H第一子块并DNA编码
    Q2 = dna_code(divide(size, H, 1), Y[0])
    # 矩阵Q1_B，Q1_G，Q1_R的第一子块与混沌矩阵Q2的第一子块分别进行DNA运算
    finB_Q = dna_operation(Q1_B, Q2, Z[0])
    finG_Q = dna_operation(Q1_G, Q2, Z[0])
    finR_Q = dna_operation(Q1_R, Q2, Z[0])
    # 对运算结果进行DNA解码，并合并在R,G,B三个图像矩阵中
    B[0: size, 0: size] = dna_decode(finB_Q, X[0])
    G[0: size, 0: size] = dna_decode(finG_Q, X[0])
    R[0: size, 0: size] = dna_decode(finR_Q, X[0])

    "---R,G,B三个图像矩阵合并得到解密图像---"
    image_decrypt = np.zeros([length, width, 3], dtype=np.float32)
    image_decrypt[:, :, 0] = B
    image_decrypt[:, :, 1] = G
    image_decrypt[:, :, 2] = R

    "---去除加密时补的零----"
    image_decrypt = image_decrypt[size: int(length - size), size: int(width - size), :]
    cv2.imwrite(savePath + '\\decrypt.png', image_decrypt)
    # cv2.imshow("解密图像", image_decrypt.astype(np.uint8))
    # cv2.waitKey(-1)