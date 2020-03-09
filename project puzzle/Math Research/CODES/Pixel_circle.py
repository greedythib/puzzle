import matplotlib.pyplot as plt
import numpy as np

def pix_circle(r_pix):
    # Circle radius in pixel

    x=np.linspace(r_pix,0.0,300)
    y=np.sqrt(r_pix**2-x**2)
    yn=-np.sqrt(r_pix**2-x**2)


    pix_x=0
    pix_y=0

    X=[r_pix]
    Y=[0]

    for i in range(300):
        pix_x=int(x[i])
        pix_y=int(y[i])
        # print(x[i],y[i],pix_x,pix_y)
        if pix_x!=X[-1] or pix_y!=Y[-1]:
            X.append(pix_x)
            Y.append(pix_y)

    X_len=len(X)

    for j in range(X_len):
        X.append(X[X_len-j-1]*-1)
        Y.append(Y[X_len-j-1])

    for j in range(X_len):
        X.append(X[j]*-1)
        Y.append(Y[j]*-1)

    for j in range(X_len):
        X.append(X[X_len-j-1])
        Y.append(Y[X_len-j-1]*-1)

    return X,Y







#
# plt.scatter(x,y,c='b')
# plt.scatter(X,Y,c='r')
# plt.axis("equal")
# plt.show()

