import numpy as np

def perceptron(data,labels,params,hook=None):

    T = params['T']
    d,n = data.shape
    th = np.zeros((d,1))
    th0 = np.zeros((1,1))

    for t in range(T) :
        for i in range (n):

            x =  data[:,i:i+1]
            y = labels[:,i:i+1]

            if y*(th.T@x+th0) <=0 :

                th = th+y*x
                th0 = th0 + y

    return th,th0