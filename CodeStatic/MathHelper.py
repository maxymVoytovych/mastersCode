import numpy as np
import math

def Derivative(f,x):
    eps = pow(10,20)
    return ((f(x + eps) - f(x)) / eps)

def IntegrateGauss(f,a,b):
    x = list(np.zeros(8))
    
    x[0] = -0.96028986
    x[7] = -x[0]
    x[1] = -0.79666648
    x[6] = -x[1]
    x[2] = -0.52553242
    x[5] = -x[2]
    x[3] = -0.18343464
    x[4] = -x[3]

    A = list(np.zeros(8))
    A[0] = A[7] = 0.10122854
    A[1] = A[6] = 0.22238103
    A[2] = A[5] = 0.31370664
    A[3] = A[4] = 0.36268378
    
    t = []
    for i in range(0,8):
        t.append((a + b) / 2 + ((b - a) / 2) * x[i])

    integral = 0
    
    for i in range(0,8):
        if callable(f):
            integral += (b - a) * (A[i] * f(t[i])) / 2
        else:
            integral += (b - a) * (A[i] * f / 2)
    
    return integral

def test_func1(x):
    return x*x

def Function(f,x):
    return f(x)

def Gauss(a,b):
    n = len(b)
    # Elimination phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i][k] != 0.0:
                #if not null define λ
                lam = a [i][k]/a[k][k]
                #we calculate the new row of the matrix
                a[i][k+1:n] = a[i][k+1:n] - lam*a[k][k+1:n]
                #we update vector b
                b[i] = b[i] - lam*b[k]
                # backward substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k][k+1:n],b[k+1:n]))/a[k][k]
    
    return b

def Integrate2D(f,a,b,c,d):
    x = [ -math.sqrt(3.0 / 5.0), 0, math.sqrt(3.0 / 5.0) ]
    weights = [ 5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0]
    jacobian = (b - a) * (d - c) / 4

    res = 0;
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            res += f(a + (1 + x[i]) *((b - a) / 2), c + (1 + x[j]) * ((d - c) / 2)) * weights[i] * weights[j] * jacobian

    return res
