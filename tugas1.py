import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return (1-(0.6*x))/x

def midPoint(x1, x2):
   return (x1+x2)/2

print('#GUIDANCE: INPUT x1 and x2 THAT RESULTS IN DIFFERENT SIGN', end='\n')
x1 = float(input('insert x1: ' ))
x2 = float(input('insert x2: ' ))
iteration = int(input('insert iteration:' ))

if(x1>x2):
    x1,x2 = x2, x1

xPrint = np.arange(x1, x2, 0.1)
yPrint = function(xPrint)

print('========================= results =========================', end='\n')

for x in range(iteration):
    print('-------------- Iteration: ', x+1 , ' --------------', end='\n')
    markNeg=0
    fx1 = function(x1)
    fx2 = function(x2)

    print('x1: ', '{0:.8g}'.format(x1))
    print('x2: ', '{0:.8g}'.format(x2))
    print('f(x1): ', '{0:.8g}'.format(fx1))
    print('f(x2): ', '{0:.8g}'.format(fx2))

    x3 = midPoint(x2, x1)
    fx3 = function(x3)

    print('midPoint: ', '{0:.8g}'.format(x3))
    print('f(x3): ', '{0:.8g}'.format(fx3), end='\n\n')

    # Pergantian nilai x1 atau x2 berdasarkan tanda hasil f(x3)
    if(((fx2<0 or fx1>0) and fx3<0) or ((fx2>0 or fx1<0) and fx3>0)):
        x2 = x3
    else:
        x1 = x3

print('The answer is in between: ', '{0:.8g}'.format(x1), 'to', '{0:.8g}'.format(x2), end='\n\n')

plt.plot(xPrint, function(xPrint))
plt.show()