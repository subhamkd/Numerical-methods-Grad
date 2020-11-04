from numpy import zeros
import time

def GE(A):
    # function for determining solution using Gaussian Elimination
    # Forward Elimination step
    start=time.time()
    for i in range(n):
        if A[i][i] == 0.0:
            t=A[i]
            A[i]=A[i+1]
            A[i+1]=t
        for j in range(i+1, n):
            c = A[j][i]/A[i][i]
            for k in range(n+1):
                A[j][k] = A[j][k] - c * A[i][k]

    # Backward Substitution step
    x[n-1] = A[n-1][n]/A[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = A[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j]*x[j]
        x[i] = x[i]/A[i][i]
    end=time.time()
    runtime=end - start
    print("Calculation time taken is : " + str(runtime))
    return x

n=6 # number of equations
A=[[10.0, -1.0, 4.0, 0.0, 2.0, 9.0, 19.0], [0.0, 25.0, -2.0, 7.0, 8.0, 4.0, 2.0], [1.0, 0.0, 15.0, 7.0, 3.0, -2.0, 13.0], [6.0, -1.0, 2.0, 23.0, 0.0, 8.0, -7.0], [-4.0, 2.0, 0.0, 5.0, -25.0, 3.0, -9.0], [0.0, 7.0, -1.0, 5.0, 4.0, -22.0, 2.0]] #the augmented matrix
x = zeros(n) # solution matrix
x=GE(A)
print(x)
