# https://stackoverflow.com/questions/47465356/how-to-find-determinant-of-matrix-using-python
def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        sum = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            sum += mul * determinant(m, sign * matrix[0][i])
        return sum


N = int(input())
for i in range(N):
    x1, y1, x2, y2, x3, y3 = [int(w) for w in input().split()]
    det = abs(determinant([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]], 1))
    print(f'{det / 2:.3f}')
