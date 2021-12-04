# Esty Friedman
# Malky Rotshild
# Adi Buchris
A = [[1, 2, 3, 4], [1, 4, 9, 16], [1, 8, 27, 64], [1, 16, 81, 256]]
B=[[2], [10], [44], [190]]
def det(M):
    a = M[0][0]*(M[1][1]*((M[2][2]*M[3][3])-(M[3][2]*M[2][3]))  -M[1][2]*((M[2][1]*M[3][3])-(M[3][1]*M[2][3])) +M[1][3]*((M[2][1]*M[3][2])-(M[3][1]*M[2][2])))

    b= -M[0][1]*(M[1][0]*((M[2][2]*M[3][3])-(M[3][2]*M[2][3]))  -M[1][2]*((M[2][0]*M[3][3])-(M[3][0]*M[2][3])) +M[1][3]*((M[2][0]*M[3][2])-(M[3][0]*M[2][2])))

    c=  M[0][2]*(M[1][0]*((M[2][1]*M[3][3])-(M[3][1]*M[2][3]))  -M[1][1]*((M[2][0]*M[3][3])-(M[3][0]*M[2][3])) +M[1][3]*((M[2][0]*M[3][1])-(M[3][0]*M[2][1])))

    d= -M[0][3]*(M[1][0]*((M[2][1]*M[3][2])-(M[3][1]*M[2][2]))  -M[1][1]*((M[2][0]*M[3][2])-(M[3][0]*M[2][2]))  +M[1][2]*((M[2][0]*M[3][1])-(M[3][0]*M[2][1])))

    det = a+b+c+d
    #print(det)
    if(det!=0):
        print("This matrix is regular")
    else:
        print("This matrix is not regular")
def elementryMatrix(n):
    c = [[0 for row in range(n)] for col in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                c[i][j]=1
            else:
                c[i][j]=0
    return c
def mulMatrix(A,B):
    n=len(A)
    c = [[0 for row in range(n)] for col in range(n)]
    for i in range(n):
        for k in range(n):
            temp=0;
            for j in range(n):
                temp+=A[i][j]*B[j][k]
            c[i][k]=temp
    return c
def elementary(A):
    x = len(A)
    U = elementryMatrix(4)#מטריצת יחידה
    for i in range(x):
        for k in range(i + 1, x):
            E = elementryMatrix(x)
            E[k][i] = -A[k][i]/A[i][i]
            A = mulMatrix(E, A)
            U = mulMatrix(E, U)
    for i in range(3, 0, -1):
        for k in range(i-1, -1, -1):
            E = elementryMatrix(x)
            E[k][i] = -A[k][i]/A[i][i]
            A = mulMatrix(E, A)
            U = mulMatrix(E, U)
    for i in range(x):

        E = elementryMatrix(x)
        E[i][i]=1/A[i][i]
        A[i][i] = A[i][i] / A[i][i]
        U = mulMatrix(E, U)
    print("The opposite matrix is:")
    for i in U:
        print(i)
def SwitchRows(matrix, i, j):
    temp=matrix[i]
    matrix[i]=matrix[j]
    matrix[j]=temp

def lm(matrix, b):
    n = len(matrix)
    y = [[0], [0], [0], [0]]
    for i in range(n):
        y[i][0] = b[i][0]
        for j in range(i):
            y[i][0] = y[i][0] - matrix[i][j] * y[j][0]
        y[i][0] = y[i][0] / matrix[i][i]
    return y

def um(matrix, y):
    x = [[0], [0], [0], [0]]
    for i in range(4):
        x[3 - i][0] = y[3 - i][0]
        for j in range(i):
            x[3 - i][0] = x[3 - i][0] - matrix[3 - i][3 - j] * x[3 - j][0]
        x[3 - i][0] = x[3 - i][0] / matrix[3 - i][3 - i]
    return x
def printf(matrix):
    for i in matrix:
        print(i)
def MatrixDiagonal(matrix):
    for i in range(4):
        MaxInd = i
        for j in range(i+1, 4):
            if abs(matrix[j][i]) > abs(matrix[MaxInd][i]):
                MaxInd = j
#            if abs(matrix[j][i])<1:
#               SwitchCols(matrix)
        if MaxInd != i:
            SwitchRows(matrix, i, MaxInd)
    for i in range (4):
        if matrix[i][i]==0:
            print("error!")
            return
    return matrix
def LU(A,B):
    x = len(A)
    E = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]# מטריצת יחידה
    L = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    for i in range(x):
        for k in range(i + 1, x):
            E = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
            E[k][i] = -A[k][i]/A[i][i]
            L[k][i] = A[k][i] / A[i][i]
            A = mulMatrix(E, A)
    return L,A

det(A)
elementary(A)
L, U = LU(A, B)
print("L:")
printf(L)
print("U:")
printf(U)
print("x:")
printf(um(U, lm(L,B)))