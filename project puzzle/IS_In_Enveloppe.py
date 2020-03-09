import numpy as np
import matplotlib.pyplot as plt
import random as rd

def Inter_Hline_segment(A,B,P):
    vAB=np.array([B[0]-A[0],B[1]-A[1]])
    vAB=vAB/np.linalg.norm(vAB)
    vp=np.array([0,1])
    t=(vAB[1]/vAB[0])*(P[0]-A[0])-(P[1]-A[1])
    I=np.array([P[0],t+P[1]])
    return I,t

def point_in_segment(P,A,B):
    l1=round((P[0]-B[0])/(A[0]-B[0]),9)
    l2=round((P[1]-B[1])/(A[1]-B[1]),9)
    print(l1,l2)
    if l1==l2 and l1<=1 and l2<=1 and l1>=0 and l2>=0:
        return True
    else:
        return False



def Is_in_envelope(x,y,lines,linesind):
    return True




P=np.array([rd.random(),rd.random()])


A=np.array([0.3,0.51])
B=np.array([0.7,0.5])
I=Inter_Hline_segment(A,B,P)[0]
t=Inter_Hline_segment(A,B,P)[1]

print(t)
print(point_in_segment(I,A,B))

plt.scatter(A[0],A[1],c='r')
plt.scatter(B[0],B[1],c='r')
plt.scatter(P[0],P[1],c='g')
plt.scatter(I[0],I[1],c='c')

plt.show()



