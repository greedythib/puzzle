import numpy as np
import matplotlib.pyplot as plt
import random as rd

### Function

def point(x,y):
    return np.array([[x],[y]])

def rd_point():
    i=rd.randint(0,nbp-1)
    return np.array([X[i],Y[i]])

def Intersect(A,B,C,D):
    vAB=np.array([B[0]-A[0],B[1]-A[1]])
    vAB=vAB/np.linalg.norm(vAB)
    vCD=np.array([D[0]-C[0],D[1]-C[1]])
    vCD=vCD/np.linalg.norm(vCD)
    t=float(((-A[0]+C[0])*vCD[1]-vCD[0]*(-A[1]+C[1]))/(vCD[0]*vAB[1]-vCD[1]*vAB[0]))
    I=np.array([-vAB[0]*t+A[0],-vAB[1]*t+A[1]])
    return I,t

def Intersect_Vert_Seg(A,B,P):
    vAB=np.array([B[0]-A[0],B[1]-A[1]])
    vAB=vAB/np.linalg.norm(vAB)
    vp=np.array([0,1])
    t=float((vAB[1]/vAB[0])*(P[0]-A[0])-(P[1]-A[1]))
    I=np.array([P[0],t+P[1]])
    return I,t

def point_in_segment(P,A,B):
    l1,l2=round((P[0]-B[0])/(A[0]-B[0]),9),round((P[1]-B[1])/(A[1]-B[1]),9)
    if l1==l2 and l1<=1 and l2<=1 and l1>=0 and l2>=0:
        return True
    else:
        return False

def plot_SEG(A,B):
    X=[A[0],B[0]]
    Y=[A[1],B[1]]
    plt.plot(X,Y,'r')

def SEG_3(I,seg_seq,i,seg_ind):
    A=seg_seq[i][0]
    B=seg_seq[i][1]
    if (point_in_segment(I,A,B)):
        plot_SEG(A,B)
        seg_ind.append(i)

def SEG_4(seg_seq,i,seg_ind):
    A=seg_seq[i][0]
    B=seg_seq[i][1]
    plot_SEG(A,B)
    seg_ind.append(i)





### exctract data from contour file
dir='//Users//martin//Desktop//project puzzle//'
filedir=dir+'piece1.txt'
file=open(filedir)
X=[]
Y=[]
rl=file.readline()
nbp=0
while rl!='':
    rl=file.readline()
    nbp+=1
file.close()
file=open(filedir)
for i in range(nbp):
    rl=file.readline().split('\t')
    X.append(int(rl[0]))
    Y.append(int(rl[1]))

plt.scatter(X,Y)

### four corner
A0=point(X[185],Y[185])
B0=point(X[84],Y[84])
C0=point(X[24],Y[24])
D0=point(X[21],Y[21])


### create four random point
# A1=rd_point()
# B1=rd_point()
# C1=rd_point()
# D1=rd_point()

### calculate the intesection point
# I1,t1=Intersect(A1,B1,C1,D1)
# I2,t2=Intersect(A1,C1,B1,D1)
# I3,t3=Intersect(A1,D1,B1,C1)


### seg_seq is the sequence of segment
# seg_seq=[[A1,B1],[B1,C1],[C1,D1],[D1,A1],[D1,B1],[C1,A1]]
# inter_pts=[I1,I2,I3]

###count of the Intersect point that are in segment
def function_Pts_In_Env(num):
    A1=rd_point()
    B1=rd_point()
    C1=rd_point()
    D1=rd_point()
    ### calculate the intesection point
    I1,t1=Intersect(A1,B1,C1,D1)
    I2,t2=Intersect(A1,C1,B1,D1)
    I3,t3=Intersect(A1,D1,B1,C1)


    ### seg_seq is the sequence of segment
    seg_seq=[[A1,B1],[B1,C1],[C1,D1],[D1,A1],[D1,B1],[C1,A1]]
    inter_pts=[I1,I2,I3]

    seg_seq=[[A1,B1],[B1,C1],[C1,D1],[D1,A1],[D1,B1],[C1,A1]]
    inter_pts=[I1,I2,I3]

    inter_pt_seg =0
    seg_ind=[]

    for i in range(6):
        for j in range(3):
            inter_pt_seg+=point_in_segment(inter_pts[j],seg_seq[i][1],seg_seq[i][0])

    if inter_pt_seg==2:
        for i in range(6):
            plt_seg=True
            for j in range(3):
                I=inter_pts[j]
                A=seg_seq[i][1]
                B=seg_seq[i][0]
                plt_seg&=not(point_in_segment(I,A,B))
            if plt_seg:
                SEG_4(seg_seq,i,seg_ind)
    else:
        for j in range(3):
            for i in range(6):
                SEG_3(inter_pts[j],seg_seq,i,seg_ind)

    k=0
    pts_in_env=0
    for i in range(nbp):
        P=point(X[i],Y[i])
        plt.scatter(P[0],P[1],c='b')
        for j in range(len(seg_ind)):
            A=seg_seq[seg_ind[j]][0]
            B=seg_seq[seg_ind[j]][1]
            I=Intersect_Vert_Seg(A,B,P)[0]
            t=Intersect_Vert_Seg(A,B,P)[1]
            if t>0 and point_in_segment(I,A,B):
                k+=1
        if k%2==1 and k<4:
            plt.scatter(P[0],P[1],c='r')
            pts_in_env+=1

        k=0



    if pts_in_env>0.25*nbp and pts_in_env<0.6*nbp:
        plt.savefig(dir+'rd_frame_Pts_count//'+str(pts_in_env)+'_'+str(num)+'.png')
        print(pts_in_env)
    plt.close()

num=0
for i in range(300):
    function_Pts_In_Env(num)
    num+=1













