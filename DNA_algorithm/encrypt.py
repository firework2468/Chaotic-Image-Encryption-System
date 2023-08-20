import cv2
import math
import numpy as np
from scipy.integrate import odeint
from functions import *
import os
import requests
import json

def encrypt(savePath, image_url):
    "---原始图像分为三个矩阵I1，I2,I3---"
    os.mkdir(savePath)
    if(image_url.startswith("http")):
        file = requests.get(image_url)
        image = cv2.imdecode(np.frombuffer(file.content, np.uint8), 1)
    else:
        image = cv2.imread(image_url)
    cv2.imwrite(savePath + '\\origin.png', image)
    # 根据RGB通道分为三个矩阵I1,I2,I3
    I1 = image[:, :, 0]  # B
    I2 = image[:, :, 1]  # G
    I3 = image[:, :, 2]  # R
    size = 4  # 分块大小
    # 以size分块补零
    I1 = np.pad(I1, size)
    I2 = np.pad(I2, size)
    I3 = np.pad(I3, size)
    length = I1.shape[0]
    width = I1.shape[1]
    SUM = length * width

    "---Logistic映射产生混沌序列并转化为二维矩阵H---"
    # 设置参数μ和初值x0
    u = 3.9999
    x0 = (np.sum(I1) + np.sum(I2)) / (255 * SUM * 2)
    x0 = round(x0, 15)
    # 得到长度为SUM的p序列
    p = np.zeros([SUM + 1000])
    p[0] = x0
    i = 0
    for i in range(SUM + 999):  # 迭代循环
        p[i + 1] = u * p[i] * (1 - p[i])
    p = p[1000: len(p)]  # 去掉前1000个元素，获得更好的随机性
    p = np.fmod(np.round(p * pow(10, 4)), 256)  # 每个元素转化为0~255范围整数
    H = p.reshape(length, width)  # 将p序列转化为length*width的二维混沌矩阵H

    "---超混沌系统产生产生四个序列X,Y,Z,W---"
    # 设置初值
    X0 = sum(sum(I1 & 17)) / (17 * SUM)
    Y0 = sum(sum(I2 & 34)) / (34 * SUM)
    Z0 = sum(sum(I3 & 68)) / (68 * SUM)
    W0 = sum(sum(I1 & 136)) / (136 * SUM)
    X0 = round(X0, 15)  # 保留四位小数
    Y0 = round(Y0, 15)
    Z0 = round(Z0, 15)
    W0 = round(W0, 15)
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
    # 序列X和Y分别决定矩阵I1,I2,I3和矩阵H的编码方式，DNA编码方式有8种，故所有元素转换为1-8的整数
    # 序列Z决定矩阵I1,I2,I3与矩阵H对应字块间的DNA运算法则，DNA运算法则有4种，故所有元素转换为1-4的整数
    # 序列W决定DNA运算后的解码方式，故所有元素转换为1-8的整数
    i = 0
    for i in range(piece):
        X[i] = math.fmod(np.round(X[i] * pow(10, 4)), 8) + 1
        Y[i] = math.fmod(np.round(Y[i] * pow(10, 4)), 8) + 1
        Z[i] = math.fmod(np.round(Z[i] * pow(10, 4)), 4) + 1
        W[i] = math.fmod(np.round(W[i] * pow(10, 4)), 8) + 1

    "---矩阵I1,I2,I3和混沌矩阵H分别分块,并以子块为单位进行DNA编码和DNA运算,最终求得R,G,B三个图像矩阵---"
    B = np.zeros([length, width])
    G = np.zeros([length, width])
    R = np.zeros([length, width])
    lnum = length / size  # 行有lnum块
    wnum = width / size  # 列有wnum块
    # 为保证扩散效果：除第一子块外，其余每一个子块的加密结果与上一个子块再进行一次DNA运算
    # 取矩阵I1,I2,I3第一子块并DNA编码
    Q1_B = dna_code(divide(size, I1, 1), X[0])
    Q1_G = dna_code(divide(size, I2, 1), X[0])
    Q1_R = dna_code(divide(size, I3, 1), X[0])
    # 取混沌矩阵H第一子块并DNA编码
    Q2 = dna_code(divide(size, H, 1), Y[0])
    # 矩阵Q1_B，Q1_G，Q1_R的第一子块与混沌矩阵Q2的第一子块分别进行DNA运算
    tempB_Q = dna_operation(Q1_B, Q2, Z[0])
    tempG_Q = dna_operation(Q1_G, Q2, Z[0])
    tempR_Q = dna_operation(Q1_R, Q2, Z[0])
    # 对运算结果进行DNA解码，并合并在R,G,B三个图像矩阵中
    B[0:size, 0:size] = dna_decode(tempB_Q, W[0])
    G[0:size, 0:size] = dna_decode(tempG_Q, W[0])
    R[0:size, 0:size] = dna_decode(tempR_Q, W[0])

    for i in range(2, piece + 1):
        # 对矩阵I1,I2,I3先分块再DNA编码
        # 每个矩阵中第i个子块的DNA编码方式为X(i-1)
        Q1_B = dna_code(divide(size, I1, i), X[i - 1])
        Q1_G = dna_code(divide(size, I2, i), X[i - 1])
        Q1_R = dna_code(divide(size, I3, i), X[i - 1])
        # 对混沌矩阵H先分块再DNA编码
        # 混沌矩阵H中第i个子块的DNA编码方式为Y(i-1)
        Q2 = dna_code(divide(size, H, i), Y[i - 1])
        # 矩阵Q1_B，Q1_G，Q1_R与混沌矩阵Q2分别进行DNA运算
        # 采用Z（i-1）的运算法则
        B_Q = dna_operation(Q1_B, Q2, Z[i - 1])
        G_Q = dna_operation(Q1_G, Q2, Z[i - 1])
        R_Q = dna_operation(Q1_R, Q2, Z[i - 1])
        # 为保证扩散效果：每一个子块的加密结果与上一个子块再进行一次DNA运算
        finB_Q = dna_operation(B_Q, tempB_Q, Z[i - 1])
        finG_Q = dna_operation(G_Q, tempG_Q, Z[i - 1])
        finR_Q = dna_operation(R_Q, tempR_Q, Z[i - 1])
        tempB_Q = finB_Q
        tempG_Q = finG_Q
        tempR_Q = finR_Q

        # 求第i个子块在完整矩阵中的x，y坐标
        x = int(math.floor(i / lnum) + 1)
        y = int(math.fmod(i, wnum))
        if y == 0:
            x = x - 1
            y = wnum
        # 将每一子块解码并合并在R,G,B三个图像矩阵中
        B[int(size * (x - 1)): int(size * x), int(size * (y - 1)): int(size * y)] = dna_decode(finB_Q, W[i - 1])
        G[int(size * (x - 1)): int(size * x), int(size * (y - 1)): int(size * y)] = dna_decode(finG_Q, W[i - 1])
        R[int(size * (x - 1)): int(size * x), int(size * (y - 1)): int(size * y)] = dna_decode(finR_Q, W[i - 1])

    "---Logistic映射产生另外两个序列Kx和Ky，并进行降序排列---"
    # 设置参数μ和初值
    u = 3.9999
    x1 = (np.sum(I1) + np.sum(I3)) / (255 * SUM * 2)
    x2 = (np.sum(I2) + np.sum(I3)) / (255 * SUM * 2)
    x1 = round(x1, 15)
    x2 = round(x2, 15)
    # 得到长度为SUM的Kx和Ky序列
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

    "---根据索引序列Ux和Uy对R,G,B三个图像矩阵进行行列置换---"
    for i in range(length):
        # B矩阵行置换
        temp1 = np.copy(B[i, :])
        B[i, :] = B[Ux[i], :]
        B[Ux[i], :] = temp1
        # G矩阵行置换
        temp2 = np.copy(G[i, :])
        G[i, :] = G[Ux[i], :]
        G[Ux[i], :] = temp2
        # R矩阵行置换
        temp3 = np.copy(R[i, :])
        R[i, :] = R[Ux[i], :]
        R[Ux[i], :] = temp3
    for i in range(width):
        # B矩阵列置换
        temp1 = np.copy(B[:, i])
        B[:, i] = B[:, Uy[i]]
        B[:, Uy[i]] = temp1
        # G矩阵列置换
        temp2 = np.copy(G[:, i])
        G[:, i] = G[:, Uy[i]]
        G[:, Uy[i]] = temp2
        # R矩阵列置换
        temp3 = np.copy(R[:, i])
        R[:, i] = R[:, Uy[i]]
        R[:, Uy[i]] = temp3

    "---R,G,B三个图像矩阵合并得到密文图像---"
    image_encrypt = np.zeros([length, width, 3], dtype=np.float32)
    image_encrypt[:, :, 0] = B
    image_encrypt[:, :, 1] = G
    image_encrypt[:, :, 2] = R
    # 显示密文图像
    cv2.imwrite(savePath + '\\encrypt.png', image_encrypt)
    # cv2.imshow("密文图像", image_encrypt.astype(np.uint8))
    # cv2.waitKey(-1)
    # 密钥
    key = [x0, x1, x2, X0, Y0, Z0, W0, size]
    json_str = json.dumps(key, indent=4)
    with open(savePath + '\\key.json', 'w') as json_file:
        json_file.write(json_str)
    # np.save('./data/key', key)





