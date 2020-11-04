# Defining the function to solve
import math
def f(x):
    return math.exp(2.5*x)-(x*x)+x-7

# Defining the derivative of the function
def g(x):
    return 2.5*(math.exp(2.5*x))-(2*x)+1

# Defining the double derivative of the function
def h(x):
    return 2.5**2*(math.exp(2.5*x))-2

# Function implementing the Newton Raphson method
def Newton(x0,err,N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('functional value at guess cannot be zero, enter different value')
            break
        
        x1 = x0 - f(x0)/g(x0)
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > err
    
    if flag==1:
        print('Required root using NR method is: ' + str(x1) + ' reached after '+ str(step-1) + ' iterations')
    else:
        print('\n The iterations do not converge in the given number of iterations.')

# Function implementing the Halley method
def Halley(x0,err,N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('functional value for guess cannot be zero, enter different value')
            break
        
        x1 = x0 - f(x0)/g(x0)*(1+(0.5*h(x0)*f(x0)/(g(x0)**2)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > err
    
    if flag==1:
        print('Required root using Halley method is: ' + str(x1) + ' reached after '+ str(step-1) + ' iterations')
    else:
        print('\n The iterations do not converge in the given number of iterations.')

x0 =1
err = 0.000001
N = 100 #max number of iterations

Newton(x0,err,N)
Halley(x0,err,N)