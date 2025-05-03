import numpy as np

def positive(x,th,th0) :
    return np.sign(th.T@x + th0)

def averaged_perceptron(data,labels,params={}) :
    T = params.get('T',100)
    (d,n) = data.shape

    th = np.zeros((d,1))
    th0 = np.zeros(1,1)
    ths = th.copy()
    th0s = th0.copy()

    for t in range(T):
        for i in range(n):

            x = data[:,i:i+1]
            y=labels[:,i:i+1]

            if y* positive(x,th,th0) <= 0.0:
                th = th + y * x
                th0 = th0 +  y

            ths = ths + th
            th0s = th0s + th0

    th_avg = ths / (T*n)
    th0_avg = th0s / (T*n)

    return th_avg,th0_avg