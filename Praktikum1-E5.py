import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return (1-(0.6*x))/x

def midPoint(x1, x2):
   return ((x1-x2)/2)+x2

x1 = float(input('insert x1:' ))
x2 = float(input('insert x1:' ))
iteration = int(input('insert iteration:' ))

xPrint = np.arange(x1, x2, 0.1)
yPrint = function(xPrint)

print('------ results ------', end='\n')

for x in range(iteration):
    print('Iteration: ', x+1 , end='\n')
    markNeg=0
    fx1 = function(x1)
    fx2 = function(x2)

    print('f(x1): ', '{0:.3g}'.format(fx1), '      ', 'f(x2): ',  '{0:.3g}'.format(fx2))

    if(fx2<0):
        x3 = midPoint(x1, x2)
        markNeg =1

    else:
        x3 = midPoint(x2, x1)
        markNeg =0

    fx3 = function(x3)
    print('midPoint: ', '{0:.4g}'.format(x3), '   ', 'f(x3): ', '{0:.3g}'.format(fx3), end='\n\n')

    if(fx3<0):
        if(markNeg==1):
            x2 = x3
        else:
            x1 = x3
        
    else:
        if(markNeg==0):
            x2 = x3
        else:
            x1 = x3;  
print('The answer is in between: ', '{0:.4g}'.format(x1), 'to', '{0:.4g}'.format(x2), end='\n\n')

plt.plot(xPrint, function(xPrint))
plt.show()
