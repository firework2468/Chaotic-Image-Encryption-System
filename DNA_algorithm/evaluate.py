import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
import shutil
import os
import json
from decrypt import decrypt
from encrypt import encrypt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False


"---直方图分析---"
# image1为原始图像，image2为加密图像
def Histogram(savePath, image1, image2):
    os.mkdir(savePath+'\\histogram')
    B1 = image1[:, :, 0]
    G1 = image1[:, :, 1]
    R1 = image1[:, :, 2]
    B2 = image2[:, :, 0]
    G2 = image2[:, :, 1]
    R2 = image2[:, :, 2]
    # 绘制image1图像各通道的直方图
    plt.hist(B1.ravel(), 256)
    plt.title("原始图像B通道直方图")
    plt.xlabel("B通道像素灰度值")
    plt.ylabel("频数")
    plt.savefig(savePath+'\\histogram\\B1.png')
    plt.close()

    plt.hist(G1.ravel(), 256)
    plt.title("原始图像G通道直方图")
    plt.xlabel("G通道像素灰度值")
    plt.ylabel("频数")
    plt.savefig(savePath+'\\histogram\\G1.png')
    plt.close()

    plt.hist(R1.ravel(), 256)
    plt.title("原始图像R通道直方图")
    plt.xlabel("R通道像素灰度值")
    plt.ylabel("频数")
    plt.savefig(savePath+'\\histogram\\R1.png')
    plt.close()

    # 绘制image2图像各通道的直方图
    plt.hist(B2.ravel(), 256)
    plt.title("密文图像B通道直方图")
    plt.xlabel("B通道像素灰度值")
    plt.ylabel("频数")
    plt.savefig(savePath+'\\histogram\\B2.png')
    plt.close()

    plt.hist(G2.ravel(), 256)
    plt.title("密文图像G通道直方图")
    plt.xlabel("G通道像素灰度值")
    plt.ylabel("频数")
    plt.savefig(savePath+'\\histogram\\G2.png')
    plt.close()

    plt.hist(R2.ravel(), 256)
    plt.title("密文图像R通道直方图")
    plt.xlabel("R通道像素灰度值")
    plt.ylabel("频数")
    plt.savefig(savePath+'\\histogram\\R2.png')
    plt.close()

"---相邻像素相关性分析---"
def Correlation(savePath, p, title, image):
    savePath = savePath+'\\'+p
    os.mkdir(savePath)
    B = image[:, :, 0]
    G = image[:, :, 1]
    R = image[:, :, 2]
    # 先随机在0~H-1行和0~W-1列选中5000个像素点，
    # 计算水平相关性时，选择每个点的相邻的右边的点；
    # 计算垂直相关性时，选择每个点的相邻的下方的点；
    # 计算对角线相关性时，选择每个点的相邻的右下方的点。
    H, W = B.shape
    num = 5000  # 随机取5000个像素点
    x = np.random.randint(0, H - 1, 5000)  # 生成5000个0~M-1的随机整数作为行
    y = np.random.randint(0, W - 1, 5000)  # 生成5000个0~N-1的随机整数作为列
    # 预分配内存
    # 水平方向
    X_horizontal = np.zeros([num, 3])
    Y_horizontal = np.zeros([num, 3])
    # 垂直方向
    X_vertical = np.zeros([num, 3])
    Y_vertical = np.zeros([num, 3])
    # 对角线方向
    X_diagonal = np.zeros([num, 3])
    Y_diagonal = np.zeros([num, 3])

    for i in range(num):
        # 水平方向
        X_horizontal[i, 0] = B[x[i]][y[i]]
        Y_horizontal[i, 0] = B[x[i] + 1][y[i]]
        X_horizontal[i, 1] = G[x[i]][y[i]]
        Y_horizontal[i, 1] = G[x[i] + 1][y[i]]
        X_horizontal[i, 2] = R[x[i]][y[i]]
        Y_horizontal[i, 2] = R[x[i] + 1][y[i]]
        # 垂直方向
        X_vertical[i, 0] = B[x[i]][y[i]]
        Y_vertical[i, 0] = B[x[i]][y[i] + 1]
        X_vertical[i, 1] = G[x[i]][y[i]]
        Y_vertical[i, 1] = G[x[i]][y[i] + 1]
        X_vertical[i, 2] = R[x[i]][y[i]]
        Y_vertical[i, 2] = R[x[i]][y[i] + 1]
        # 对角线方向
        X_diagonal[i, 0] = B[x[i]][y[i]]
        Y_diagonal[i, 0] = B[x[i] + 1][y[i] + 1]
        X_diagonal[i, 1] = G[x[i]][y[i]]
        Y_diagonal[i, 1] = G[x[i] + 1][y[i] + 1]
        X_diagonal[i, 2] = R[x[i]][y[i]]
        Y_diagonal[i, 2] = R[x[i] + 1][y[i] + 1]

    "---水平相关性绘图---"
    # B通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "B通道水平相邻元素相关性点图")
    plt.xlabel("B通道随机点像素灰度值")
    plt.ylabel("与该点相邻水平方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_horizontal[:, 0], Y_horizontal[:, 0], c='b', marker='.')
    plt.savefig(savePath + '\\hor_B.png')
    plt.close()

    # G通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "G通道水平相邻元素相关性点图")
    plt.xlabel("G通道随机点像素灰度值")
    plt.ylabel("与该点相邻水平方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_horizontal[:, 1], Y_horizontal[:, 1], c='b', marker='.')
    plt.savefig(savePath + '\\hor_G.png')
    plt.close()

    # R通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "R通道水平相邻元素相关性点图")
    plt.xlabel("R通道随机点像素灰度值")
    plt.ylabel("与该点相邻水平方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_horizontal[:, 2], Y_horizontal[:, 2], c='b', marker='.')
    plt.savefig(savePath + '\\hor_R.png')
    plt.close()

    "---垂直相关性绘图---"
    # B通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "B通道垂直相邻元素相关性点图")
    plt.xlabel("B通道随机点像素灰度值")
    plt.ylabel("与该点相邻垂直方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_vertical[:, 0], Y_vertical[:, 0], c='b', marker='.')
    plt.savefig(savePath + '\\ver_B.png')
    plt.close()

    # G通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "G通道垂直相邻元素相关性点图")
    plt.xlabel("G通道随机点像素灰度值")
    plt.ylabel("与该点相邻垂直方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_vertical[:, 1], Y_vertical[:, 1], c='b', marker='.')
    plt.savefig(savePath + '\\ver_G.png')
    plt.close()

    # R通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "R通道垂直相邻元素相关性点图")
    plt.xlabel("R通道随机点像素灰度值")
    plt.ylabel("与该点相邻垂直方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_vertical[:, 2], Y_vertical[:, 2], c='b', marker='.')
    plt.savefig(savePath + '\\ver_R.png')
    plt.close()

    "---对角线相关性绘图---"
    # B通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "B通道对角线相邻元素相关性点图")
    plt.xlabel("B通道随机点像素灰度值")
    plt.ylabel("与该点相邻对角线方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_diagonal[:, 0], Y_diagonal[:, 0], c='b', marker='.')
    plt.savefig(savePath + '\\dia_B.png')
    plt.close()

    # G通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "G通道对角线相邻元素相关性点图")
    plt.xlabel("G通道随机点像素灰度值")
    plt.ylabel("与该点相邻对角线方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_diagonal[:, 1], Y_diagonal[:, 1], c='b', marker='.')
    plt.savefig(savePath + '\\dia_G.png')
    plt.close()

    # R通道
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + "R通道对角线相邻元素相关性点图")
    plt.xlabel("R通道随机点像素灰度值")
    plt.ylabel("与该点相邻对角线方向像素灰度值")
    # 设置横、纵坐标范围
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    # 设置横、纵坐标刻度值
    plt.xticks(range(0, 256, 15))
    plt.yticks(range(0, 256, 15))
    # 画散点图
    ax1.scatter(X_diagonal[:, 2], Y_diagonal[:, 2], c='b', marker='.')
    plt.savefig(savePath + '\\dia_R.png')
    plt.close()

    """相关性计算"""
    # 水平相关性
    EX_B_h = np.mean(X_horizontal[:, 0])
    DX_B_h = np.std(X_horizontal[:, 0])
    EY_B_h = np.mean(Y_horizontal[:, 0])
    DY_B_h = np.std(Y_horizontal[:, 0])
    COV_B_h = np.sum((X_horizontal[:, 0] - EX_B_h) * (Y_horizontal[:, 0] - EY_B_h)) / num
    r_B_h = COV_B_h / (DX_B_h * DY_B_h)
    r_B_h = np.round(r_B_h, 4)

    EX_G_h = np.mean(X_horizontal[:, 1])
    DX_G_h = np.std(X_horizontal[:, 1])
    EY_G_h = np.mean(Y_horizontal[:, 1])
    DY_G_h = np.std(Y_horizontal[:, 1])
    COV_G_h = np.sum((X_horizontal[:, 1] - EX_G_h) * (Y_horizontal[:, 1] - EY_G_h)) / num
    r_G_h = COV_G_h / (DX_G_h * DY_G_h)
    r_G_h = np.round(r_G_h, 4)

    EX_R_h = np.mean(X_horizontal[:, 2])
    DX_R_h = np.std(X_horizontal[:, 2])
    EY_R_h = np.mean(Y_horizontal[:, 2])
    DY_R_h = np.std(Y_horizontal[:, 2])
    COV_R_h = np.sum((X_horizontal[:, 2] - EX_R_h) * (Y_horizontal[:, 2] - EY_R_h)) / num
    r_R_h = COV_R_h / (DX_R_h * DY_R_h)
    r_R_h = np.round(r_R_h, 4)

    # 垂直相关性
    EX_B_v = np.mean(X_vertical[:, 0])
    DX_B_v = np.std(X_vertical[:, 0])
    EY_B_v = np.mean(Y_vertical[:, 0])
    DY_B_v = np.std(Y_vertical[:, 0])
    COV_B_v = np.sum((X_vertical[:, 0] - EX_B_v) * (Y_vertical[:, 0] - EY_B_v)) / num
    r_B_v = COV_B_v / (DX_B_v * DY_B_v)
    r_B_v = np.round(r_B_v, 4)

    EX_G_v = np.mean(X_vertical[:, 1])
    DX_G_v = np.std(X_vertical[:, 1])
    EY_G_v = np.mean(Y_vertical[:, 1])
    DY_G_v = np.std(Y_vertical[:, 1])
    COV_G_v = np.sum((X_vertical[:, 1] - EX_G_v) * (Y_vertical[:, 1] - EY_G_v)) / num
    r_G_v = COV_G_v / (DX_G_v * DY_G_v)
    r_G_v = np.round(r_G_v, 4)

    EX_R_v = np.mean(X_vertical[:, 2])
    DX_R_v = np.std(X_vertical[:, 2])
    EY_R_v = np.mean(Y_vertical[:, 2])
    DY_R_v = np.std(Y_vertical[:, 2])
    COV_R_v = np.sum((X_horizontal[:, 2] - EX_R_v) * (Y_horizontal[:, 2] - EY_R_v)) / num
    r_R_v = COV_R_v / (DX_R_v * DY_R_v)
    r_R_v = np.round(r_R_v, 4)

    # 对角线相关性
    EX_B_d = np.mean(X_diagonal[:, 0])
    DX_B_d = np.std(X_diagonal[:, 0])
    EY_B_d = np.mean(Y_diagonal[:, 0])
    DY_B_d = np.std(Y_diagonal[:, 0])
    COV_B_d = np.sum((X_diagonal[:, 0] - EX_B_d) * (Y_diagonal[:, 0] - EY_B_d)) / num
    r_B_d = COV_B_d / (DX_B_d * DY_B_d)
    r_B_d = np.round(r_B_d, 4)

    EX_G_d = np.mean(X_diagonal[:, 1])
    DX_G_d = np.std(X_diagonal[:, 1])
    EY_G_d = np.mean(Y_diagonal[:, 1])
    DY_G_d = np.std(Y_diagonal[:, 1])
    COV_G_d = np.sum((X_diagonal[:, 1] - EX_G_d) * (Y_diagonal[:, 1] - EY_G_d)) / num
    r_G_d = COV_G_d / (DX_G_d * DY_G_d)
    r_G_d = np.round(r_G_d, 4)

    EX_R_d = np.mean(X_diagonal[:, 2])
    DX_R_d = np.std(X_diagonal[:, 2])
    EY_R_d = np.mean(Y_diagonal[:, 2])
    DY_R_d = np.std(Y_diagonal[:, 2])
    COV_R_d = np.sum((X_diagonal[:, 2] - EX_R_d) * (Y_horizontal[:, 2] - EY_R_d)) / num
    r_R_d = COV_R_d / (DX_R_d * DY_R_d)
    r_R_d = np.round(r_R_d, 4)

    list = [{"name": "水平相关系数", "R": r_R_h, "G": r_G_h, "B": r_B_h},
            {"name": "垂直相关系数", "R": r_R_v, "G": r_G_v, "B": r_B_v},
            {"name": "对角线相关系数", "R": r_R_d, "G": r_G_d, "B": r_B_d}]
    json_str = json.dumps(list, indent=4)
    with open(savePath + '\\coefficient.json', 'w') as json_file:
        json_file.write(json_str)

"---信息熵分析---"
def Information_Entropy(savePath, image1, image2):
    savePath = savePath+'\\information_entropy'
    os.mkdir(savePath)
    B1 = image1[:, :, 0]
    G1 = image1[:, :, 1]
    R1 = image1[:, :, 2]
    B2 = image2[:, :, 0]
    G2 = image2[:, :, 1]
    R2 = image2[:, :, 2]

    H1, W1 = B1.shape
    SUM1 = H1 * W1
    #B通道
    T_B1 = np.histogram(B1.ravel(), 256, [0, 256])
    xxs_B1=0
    #G通道
    T_G1 = np.histogram(G1.ravel(), 256, [0, 256])
    xxs_G1=0
    #R通道
    T_R1 = np.histogram(R1.ravel(), 256, [0, 256])
    xxs_R1=0

    for i in range(256):
        pp_B1 = T_B1[0][i] / SUM1                #每个灰度值占比，即每个灰度值的概率
        pp_G1 = T_G1[0][i] / SUM1
        pp_R1 = T_R1[0][i] / SUM1
        if pp_B1 != 0:
            xxs_B1 = xxs_B1 - pp_B1 * math.log2(pp_B1)
        if pp_G1 != 0:
            xxs_G1 = xxs_G1 - pp_G1 * math.log2(pp_G1)
        if pp_R1 != 0:
            xxs_R1 = xxs_R1 - pp_R1 * math.log2(pp_R1)
    xxs_B1 = np.round(xxs_B1, 4)
    xxs_G1 = np.round(xxs_G1, 4)
    xxs_R1 = np.round(xxs_R1, 4)

    H2, W2 = B2.shape
    SUM2 = H2 * W2
    # B通道
    T_B2 = np.histogram(B2.ravel(), 256, [0, 256])
    xxs_B2 = 0
    # G通道
    T_G2 = np.histogram(G2.ravel(), 256, [0, 256])
    xxs_G2 = 0
    # R通道
    T_R2 = np.histogram(R2.ravel(), 256, [0, 256])
    xxs_R2 = 0

    for i in range(256):
        pp_B2 = T_B2[0][i] / SUM2  # 每个灰度值占比，即每个灰度值的概率
        pp_G2 = T_G2[0][i] / SUM2
        pp_R2 = T_R2[0][i] / SUM2
        if pp_B2 != 0:
            xxs_B2 = xxs_B2 - pp_B2 * math.log2(pp_B2)
        if pp_G2 != 0:
            xxs_G2 = xxs_G2 - pp_G2 * math.log2(pp_G2)
        if pp_R2 != 0:
            xxs_R2 = xxs_R2 - pp_R2 * math.log2(pp_R2)
    xxs_B2 = np.round(xxs_B2, 4)
    xxs_G2 = np.round(xxs_G2, 4)
    xxs_R2 = np.round(xxs_R2, 4)

    list = [{"name": "原始图像", "R": xxs_R1, "G": xxs_G1, "B": xxs_B1},
            {"name": "密文图像", "R": xxs_R2, "G": xxs_G2, "B": xxs_B2}]
    json_str = json.dumps(list, indent=4)
    with open(savePath + '\\data.json', 'w') as json_file:
        json_file.write(json_str)

"---密钥敏感性---"
# x0值在解密时微小变化导致的错误解密图像
def Key_Sensitive(savePath, key):
    image = savePath+'\\encrypt.png'
    savePath = savePath + '\\key_sensitive'
    key[0] = key[0] + 0.0000000000000001
    decrypt(savePath, image, key)

"---差分攻击分析---"
def NPCR(savePath, image1):
    image = cv2.imread(savePath + '\\origin.png')
    change = image
    change[0, 0, 2] = 0
    path = savePath + '\\change.png'
    cv2.imwrite(path, change)
    savePath = savePath + '\\differential_attack'
    encrypt(savePath, path)
    image2 = cv2.imread(savePath +'\\encrypt.png')
    h = image1.shape[0]
    w = image1.shape[1]
    # 图像通道拆分
    B1, G1, R1 = cv2.split(image1)
    B2, G2, R2 = cv2.split(image2)
    R_num = 0
    G_num = 0
    B_num = 0
    for i in range(h):
        for j in range(w):
            if R1[i, j] != R2[i, j]:
                R_num = R_num + 1
            if G1[i, j] != G2[i, j]:
                G_num = G_num + 1
            if B1[i, j] != B2[i, j]:
                B_num = B_num + 1
    R_npcr = R_num / (w * h)
    G_npcr = G_num / (w * h)
    B_npcr = B_num / (w * h)
    list = [{"name": "NPCR", "R": '{:.4%}'.format(R_npcr), "G": '{:.4%}'.format(G_npcr), "B": '{:.4%}'.format(B_npcr)}]
    json_str = json.dumps(list, indent=4)
    with open(savePath + '\\npcr.json', 'w') as json_file:
        json_file.write(json_str)

def UACI(savePath, image1):
    savePath = savePath + '\\differential_attack'
    image2 = cv2.imread(savePath + '\\encrypt.png')
    h = image1.shape[0]
    w = image1.shape[1]
    # 图像通道拆分
    B1, G1, R1 = cv2.split(image1)
    B2, G2, R2 = cv2.split(image2)
    # 元素为uint8类型取值范围：0到255
    # 强制转换元素类型，为了运算
    R1 = R1.astype(np.int16)
    R2 = R2.astype(np.int16)
    G1 = G1.astype(np.int16)
    G2 = G2.astype(np.int16)
    B1 = B1.astype(np.int16)
    B2 = B2.astype(np.int16)

    sumR = np.sum(abs(R1 - R2))
    sumG = np.sum(abs(G1 - G2))
    sumB = np.sum(abs(B1 - B2))
    R_uaci = sumR / 255 / (h * w)
    G_uaci = sumG / 255 / (h * w)
    B_uaci = sumB / 255 / (h * w)
    list = [{"name": "UACI", "R": '{:.4%}'.format(R_uaci), "G": '{:.4%}'.format(G_uaci), "B": '{:.4%}'.format(B_uaci)}]
    json_str = json.dumps(list, indent=4)
    with open(savePath + '\\uaci.json', 'w') as json_file:
        json_file.write(json_str)

