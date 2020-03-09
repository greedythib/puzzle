import imageio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np
import time

fileX=open('//Users/martin//Desktop//project puzzle//piece1X.txt')
fileY=open('//Users/martin//Desktop//project puzzle//piece1Y.txt')


def interx(A,B,C):
    xa=A[0]
    xb=B[0]
    xc=C[0]
    t=((float(xc-xa)))/abs(float(xb-xa))
    print(t)
    if t>0 and t<1:
        return True
    else:
        return False


def intery(A,B,C):
    ya=A[1]
    yb=B[1]
    yc=C[1]
    t=((float(yc-ya)))/abs(float(yb-ya))
    if t>0 and t<1:
        return True
    else:
        return False


X=[]
Y=[]
# a=fileX.readline()
# while len(a)!=0:
#     b=a.split('\t')
#     X.append(int(b[0]))
#     Y.append(int(b[1]))
#     a=fileX.readline()
#
# a=fileY.readline()
# while len(a)!=0:
#     b=a.split('\t')
#     X.append(int(b[0]))
#     Y.append(int(b[1]))
#     a=fileY.readline()


X=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
Y=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]

# print(X,Y)

nbpt=len(X)

# pts1=np.array([X[4*nbpt/4-1],Y[4*nbpt/4-1]])
# pts2=np.array([X[1*nbpt/4],Y[1*nbpt/4]])
# pts3=np.array([X[2*nbpt/4],Y[2*nbpt/4]])
# pts4=np.array([X[3*nbpt/4],Y[3*nbpt/4]])

i1=0
i2=7
i3=18
i4=11

# 1,89,138,70

pts1=np.array([X[i1],Y[i1]])
pts2=np.array([X[i2],Y[i2]])
pts3=np.array([X[i3],Y[i3]])
pts4=np.array([X[i4],Y[i4]])


# print(pts1,pts2,pts3,pts4)

plt.plot(X,Y,'bo')

t0=time.time()

# ptin=0
# for i in range(len(X)):
#     C=np.array([X[i],Y[i]])
#     #print((inter(pts1,pts2,C)+inter(pts2,pts3,C)+inter(pts3,pts4,C)+inter(pts4,pts1,C))%2)
#     if (inter(pts1,pts2,C)+inter(pts2,pts3,C)+inter(pts3,pts4,C)+inter(pts4,pts1,C))%2==1:
#         print('i ',i)
#         print('cordon 1: ',inter(pts1,pts2,C))
#         print('cordon 2: ',inter(pts2,pts3,C))
#         print('cordon 3: ',inter(pts3,pts4,C))
#         print('cordon 4: ',inter(pts4,pts1,C))
#         ptin+=1
#         plt.plot(C[0],C[1],'go')
#


ptin=0
for i in range(len(X)):
    C=np.array([X[i],Y[i]])
    #print((inter(pts1,pts2,C)+inter(pts2,pts3,C)+inter(pts3,pts4,C)+inter(pts4,pts1,C))%2)
    ix=interx(pts1,pts2,C)+interx(pts2,pts3,C)+interx(pts3,pts4,C)+interx(pts4,pts1,C)
    iy=intery(pts1,pts2,C)+intery(pts2,pts3,C)+intery(pts3,pts4,C)+intery(pts4,pts1,C)
    if ix==1 and iy==1 :
        print('i ',i)
        # print('cordon 1: ',inter(pts1,pts2,C))
        # print('cordon 2: ',inter(pts2,pts3,C))
        # print('cordon 3: ',inter(pts3,pts4,C))
        # print('cordon 4: ',inter(pts4,pts1,C))
        ptin+=1
        plt.plot(C[0],C[1],'go')


print(len(X))
print(ptin)


t1=time.time()
print(t1-t0)
plt.plot(pts1[0],pts1[1],'co')
plt.plot(pts2[0],pts2[1],'yo')
plt.plot(pts3[0],pts3[1],'mo')
plt.plot(pts4[0],pts4[1],'ro')

plt.show()







