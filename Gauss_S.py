from numpy import zeros
import time
import matplotlib.pyplot as plt

def GS(A):
    # function for determining the  solution using Gauss Siedel Iteration
    x_err=[]  # array to store the error in each iteration
    change=[]
    start=time.time()
    for i in range(n):
        for count in range(i+1,n):
            if abs(A[i][i]) < abs(A[count][i]):  #to make the matrix diagonally dominant
                t=A[i]
                A[i]=A[count]
                A[count]=t
    print(A)
    flag = 0
    while flag<n+1:
        for i in range(n):
            y=x[i]
            x[i]=A[i][n]
            for j in range(n):
                if j!=i:
                    x[i]=x[i]-A[i][j]*x[j]
            x[i]=x[i]/A[i][i]
            err=abs((x[i]-y)/x[i])
            x_err.append(err)
            if abs(err) <= 0.00001:
                flag=flag+1
    plt.figure(dpi=100)
    for q in range(n):
        change=x_err[q::n]
        plt.plot(range(len(change)),change)
    plt.title("error for each variable vs iteration")
    plt.xlabel("iteration number")
    plt.ylabel("error")
    plt.grid()
    plt.show()
    end=time.time()
    runtime=end - start
    print("Calculation time taken is : " + str(runtime))
    return x


tmp=input("Enter 1 for user input matrix, 2 for the Chapter 2 problem 1")
if tmp == '1':
    n = input("Enter the number of equations to solve ")
    n = int(n)
    x = zeros(n)
    A=[]
    for i in range(n):
        r=[]
        for j in range(n+1):
            prompt='Enter the coefficient ' + str(j+1) + ' of equation ' + str(i+1)
            r.append(float(input(prompt)))
        A.append(r)
    print(A)
else:
    n=6
    A=[[10.0, -1.0, 4.0, 0.0, 2.0, 9.0, 19.0], [0.0, 25.0, -2.0, 7.0, 8.0, 4.0, 2.0], [1.0, 0.0, 15.0, 7.0, 3.0, -2.0, 13.0], [6.0, -1.0, 2.0, 23.0, 0.0, 8.0, -7.0], [-4.0, 2.0, 0.0, 5.0, -25.0, 3.0, -9.0], [0.0, 7.0, -1.0, 5.0, 4.0, -22.0, 2.0]]
    x = zeros(n)
    x=GS(A)
    print(x)
