import math
import numpy as np

# 分块函数，分出array中以size为大小的第num块。
# size为分块大小，array为要分块的矩阵，num为第几子块
def divide(size, array, num):
    length = array.shape[0]
    width = array.shape[1]
    lnum = length / size                        # 行有lnum块
    wnum = width / size                         # 列有wnum块
    x = int(math.ceil(num / lnum))              # 第几大行
    y = int(np.mod(num, wnum))                  # 第几大列
    if y == 0:
        y = wnum
    f = np.zeros([4, 4])
    f = array[int(size*(x-1)): int(size*x), int(size*(y-1)): int(size*y)]
    return f                                    #返回第num块子块

# DNA编码
def dna_code(array, No):
    len = array.shape[0]
    wid = array.shape[1]
    b1 = (array.astype(np.int8) & 192) / 64
    b2 = (array.astype(np.int8) & 48) / 16
    b3 = (array.astype(np.int8) & 12) / 4
    b4 = (array.astype(np.int8) & 3)
    B = np.stack((b1, b2, b3, b4), axis=2)
    g = np.zeros([4, len, wid], dtype=np.str_)
    # 第1种DNA编码方式，'A'00,'T'11,'C'01,'G'10
    if No == 1:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'A'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'C'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'G'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'T'
    # 第2种DNA编码方式，'A'00,'T'11,'C'10,'G'01
    if No == 2:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'A'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'G'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'C'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'T'
    # 第3种DNA编码方式，'A'01,'T'10,'C'00,'G'11
    if No == 3:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'C'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'A'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'T'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'G'
    # 第4种DNA编码方式，'A'01,'T'10,'C'11,'G'00
    if No == 4:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'G'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'A'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'T'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'C'
    # 第5种DNA编码方式，'A'10,'T'01,'C'00,'G'11
    if No == 5:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'C'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'T'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'A'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'G'
    # 第6种DNA编码方式，'A'10,'T'01,'C'11,'G'00
    if No == 6:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'G'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'T'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'A'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'C'
    # 第7种DNA编码方式，'A'11,'T'00,'C'01,'G'10
    if No == 7:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'T'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'C'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'G'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'A'
    # 第8种DNA编码方式，'A'11,'T'00,'C'10,'G'01
    if No == 8:
        for i in range(4):
            for j in range(len):
                for k in range(wid):
                    if B[i][j][k] == 0:
                        g[i, j, k] = 'T'
                    elif B[i][j][k] == 1:
                        g[i, j, k] = 'G'
                    elif B[i][j][k] == 2:
                        g[i, j, k] = 'C'
                    elif B[i][j][k] == 3:
                        g[i, j, k] = 'A'
    return g

# DNA运算
# 采用基于第1种DNA编码的运算法则
def dna_operation(arr1, arr2, No):
    high = arr1.shape[0]
    len = arr1.shape[1]
    wid = arr1.shape[2]
    h = np.zeros([high, len, wid], dtype=np.str_)
    # 当No为1时，做加法运算
    if No == 1:  # 加法
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if arr1[i, j, k] == 'A':
                        h[i, j, k] = arr2[i, j, k]
                    elif arr1[i, j, k] == 'T':
                        if arr2[i, j, k] == 'A':
                            h[i, j, k] = 'T'
                        elif arr2[i, j, k] == 'T':
                            h[i, j, k] = 'G'
                        elif arr2[i, j, k] == 'C':
                            h[i, j, k] = 'A'
                        else:  # arr2[i, j, k] == 'G'
                            h[i, j, k] = 'C'
                    elif arr1[i, j, k] == 'C':
                        if arr2[i, j, k] == 'A':
                            h[i, j, k] = 'C'
                        elif arr2[i, j, k] == 'T':
                            h[i, j, k] = 'A'
                        elif arr2[i, j, k] == 'C':
                            h[i, j, k] = 'G'
                        else:   # arr2[i, j, k] == 'G'
                            h[i, j, k] = 'T'
                    else:  # arr1[i, j, k] == 'G'
                        if arr2[i, j, k] == 'A':
                            h[i, j, k] = 'G'
                        elif arr2[i, j, k] == 'T':
                            h[i, j, k] = 'C'
                        elif arr2[i, j, k] == 'C':
                            h[i, j, k] = 'T'
                        else:  # arr2[i, j, k] == 'G'
                            h[i, j, k] = 'A'
    # 当No为2时，做减法运算
    elif No == 2:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if arr2[i, j, k] == 'A':
                        h[i, j, k] = arr1[i, j, k]
                    elif arr2[i, j, k] == 'T':
                        if arr1[i, j, k] == 'A':
                            h[i, j, k] = 'C'
                        elif arr1[i, j, k] == 'T':
                            h[i, j, k] = 'A'
                        elif arr1[i, j, k] == 'C':
                            h[i, j, k] = 'G'
                        else:  # arr1[i, j, k] == 'G'
                            h[i, j, k] = 'T'
                    elif arr2[i, j, k] == 'C':
                        if arr1[i, j, k] == 'A':
                            h[i, j, k] = 'T'
                        elif arr1[i, j, k] == 'T':
                            h[i, j, k] = 'G'
                        elif arr1[i, j, k] == 'C':
                            h[i, j, k] = 'A'
                        else:  # arr1[i, j, k] == 'G'
                            h[i, j, k] = 'C'
                    else:  # arr2[i, j, k] == 'G'
                        if arr1[i, j, k] == 'A':
                            h[i, j, k] = 'G'
                        elif arr1[i, j, k] == 'T':
                            h[i, j, k] = 'C'
                        elif arr1[i, j, k] == 'C':
                            h[i, j, k] = 'T'
                        else:  # arr1[i, j, k] == 'G'
                            h[i, j, k] = 'A'
    # 当No为3时，做异或运算（同为0，异为1）
    elif No == 3:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if arr1[i, j, k] == arr2[i, j, k]:
                        h[i, j, k] = 'A'
                    elif (arr1[i, j, k] == 'A' and arr2[i, j, k] == 'T') or (
                            arr1[i, j, k] == 'T' and arr2[i, j, k] == 'A') or (
                            arr1[i, j, k] == 'C' and arr2[i, j, k] == 'G') or (
                            arr1[i, j, k] == 'G' and arr2[i, j, k] == 'C'):
                        h[i, j, k] = 'T'
                    elif (arr1[i, j, k] == 'A' and arr2[i, j, k] == 'C') or (
                            arr1[i, j, k] == 'C' and arr2[i, j, k] == 'A') or (
                            arr1[i, j, k] == 'T' and arr2[i, j, k] == 'G') or (
                            arr1[i, j, k] == 'G' and arr2[i, j, k] == 'T'):
                        h[i, j, k] = 'C'
                    else:
                        h[i, j, k] = 'G'
    # 当No为3时，做同或运算（同为1，异为0）
    else:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if arr1[i, j, k] == arr2[i, j, k]:
                        h[i, j, k] = 'T'
                    elif (arr1[i, j, k] == 'A' and arr2[i, j, k] == 'T') or (
                            arr1[i, j, k] == 'T' and arr2[i, j, k] == 'A') or (
                            arr1[i, j, k] == 'C' and arr2[i, j, k] == 'G') or (
                            arr1[i, j, k] == 'G' and arr2[i, j, k] == 'C'):
                        h[i, j, k] = 'A'
                    elif (arr1[i, j, k] == 'A' and arr2[i, j, k] == 'G') or (
                            arr1[i, j, k] == 'G' and arr2[i, j, k] == 'A') or (
                            arr1[i, j, k] == 'T' and arr2[i, j, k] == 'C') or (
                            arr1[i, j, k] == 'C' and arr2[i, j, k] == 'T'):
                        h[i, j, k] = 'C'
                    else:
                        h[i, j, k] = 'G'
    return h

# DNA解码
def dna_decode(array, No):
    high = array.shape[0]
    len = array.shape[1]
    wid = array.shape[2]
    C = np.zeros([high, len, wid])
    # 第1种DNA编码方式，'A'00,'T'11,'C'01,'G'10
    if No == 1:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 0
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 3
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 1
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 2
    # 第2种DNA编码方式，'A'00,'T'11,'C'10,'G'01
    if No == 2:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 0
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 3
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 2
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 1
    # 第3种DNA编码方式，'A'01,'T'10,'C'00,'G'11
    if No == 3:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 1
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 2
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 0
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 3
    # 第4种DNA编码方式，'A'01,'T'10,'C'11,'G'00
    if No == 4:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 1
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 2
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 3
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 0
    # 第5种DNA编码方式，'A'10,'T'01,'C'00,'G'11
    if No == 5:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 2
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 1
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 0
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 3
    # 第6种DNA编码方式，'A'10,'T'01,'C'11,'G'00
    if No == 6:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 2
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 1
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 3
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 0
    # 第7种DNA编码方式，'A'11,'T'00,'C'01,'G'10
    if No == 7:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 3
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 0
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 1
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 2
    # 第8种DNA编码方式，'A'11,'T'00,'C'10,'G'01
    if No == 8:
        for i in range(high):
            for j in range(len):
                for k in range(wid):
                    if array[i][j][k] == 'A':
                        C[i, j, k] = 3
                    elif array[i][j][k] == 'T':
                        C[i, j, k] = 0
                    elif array[i][j][k] == 'C':
                        C[i, j, k] = 2
                    elif array[i][j][k] == 'G':
                        C[i, j, k] = 1
    C1 = C[:, :, 0]
    C2 = C[:, :, 1]
    C3 = C[:, :, 2]
    C4 = C[:, :, 3]
    f = C1 * 64 + C2 * 16 + C3 * 4 + C4
    return f
