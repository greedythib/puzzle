import numpy as np
import matplotlib.pyplot as plt
import random as rd


file=open('//Users/martin//Desktop//piece.txt')

# nbp=100
X=[]
Y=[]

rl=file.readline()

# print(rl)
nbp=0
while rl!='':
    rl=file.readline()
    nbp+=1
file.close()
file=open('//Users/martin//Desktop//piece.txt')

for i in range(nbp):
    rl=file.readline().split('\t')
    X.append(int(rl[0]))
    Y.append(int(rl[1]))
# print(len(X))
# print(X,Y)



# for i in range(nbp):
#     X.append(rd.random())
#     Y.append(rd.random())



plt.scatter(X,Y)


def point():
    i=rd.randint(0,nbp-1)
    return np.array([X[i],Y[i]])


def segment(A,B):
    X=[A[0],B[0]]
    Y=[A[1],B[1]]
    plt.plot(X,Y,'r')

def segment1(A,B):
    X=[A[0],B[0]]
    Y=[A[1],B[1]]
    plt.plot(X,Y,'r')

def Inter_Hline_segment(A,B,P):
    vAB=np.array([B[0]-A[0],B[1]-A[1]])
    vAB=vAB/np.linalg.norm(vAB)
    vp=np.array([0,1])
    t=float((vAB[1]/vAB[0])*(P[0]-A[0])-(P[1]-A[1]))
    I=np.array([P[0],t+P[1]])
    return I,t

def intersection(A,B,C,D):
    vAB=np.array([B[0]-A[0],B[1]-A[1]])
    vAB=vAB/np.linalg.norm(vAB)
    vCD=np.array([D[0]-C[0],D[1]-C[1]])
    vCD=vCD/np.linalg.norm(vCD)
    t=((-A[0]+C[0])*vCD[1]-vCD[0]*(-A[1]+C[1]))/(vCD[0]*vAB[1]-vCD[1]*vAB[0])
    I=np.array([-vAB[0]*t+A[0],-vAB[1]*t+A[1]])
    return I,t


def point_in_segment(P,A,B):
    l1=round((P[0]-B[0])/(A[0]-B[0]),9)
    l2=round((P[1]-B[1])/(A[1]-B[1]),9)
    #print(l1,l2)
    if l1==l2 and l1<=1 and l2<=1 and l1>=0 and l2>=0:
        return True
    else:
        return False

def SEG(I,A,B):
    if (point_in_segment(I,A,B)):
        print(A,B)
        segment(A,B)

def SEG1(I,lines,i,linesind):
    A=lines[i][0]
    B=lines[i][1]
    if (point_in_segment(I,A,B)):
        segment(A,B)
        linesind.append(i)

def SEG2(I,lines,i,linesind):
    A=lines[i][0]
    B=lines[i][1]
    if (point_in_segment(I,A,B)):
        segment1(A,B)
        linesind.append(i)

def SEG3(lines,i,linesind):
    A=lines[i][0]
    B=lines[i][1]
    segment(A,B)
    linesind.append(i)

def nSEG(I,A,B):
    if not(point_in_segment(I,A,B)):
        segment(A,B)

def nSEG1(I,lines,i,linesind):
    A=lines[i][0]
    B=lines[i][1]
    if not(point_in_segment(I,A,B)):
        segment(A,B)
        linesind.append(i)

def nSEG2(I,lines,i,linesind):
    A=lines[i][0]
    B=lines[i][1]
    if not(point_in_segment(I,A,B)):
        segment1(A,B)
        linesind.append(i)


def Is_in_envelope(x,y,lines,linesind):
    return True

pts_in_env=0
maxpts=0


linesind=[]

### create four random point
# A1=point()
# B1=point()
# C1=point()
# D1=point()
# print(A1,B1,C1,D1)

### four corner
A1=np.array([[X[185]],[Y[185]]])
B1=np.array([[X[84]],[Y[84]]])
C1=np.array([[X[24]],[Y[24]]])
D1=np.array([[X[21]],[Y[21]]])



### calculate the intesection point
I1,t1=intersection(A1,B1,C1,D1)
I2,t2=intersection(A1,C1,B1,D1)
I3,t3=intersection(A1,D1,B1,C1)

lines=[[A1,B1],[B1,C1],[C1,D1],[D1,A1],[D1,B1],[C1,A1]]
inter_point=[I1,I2,I3]


inter_pt_seg1=0
inter_pt_seg2=0
inter_pt_seg3=0

for i in range(6):
    # print(I1,point_in_segment(I1,lines[i][1],lines[i][0]))
    # print(I2,point_in_segment(I2,lines[i][1],lines[i][0]))
    # print(I3,point_in_segment(I3,lines[i][1],lines[i][0]))
    inter_pt_seg1+=point_in_segment(I1,lines[i][1],lines[i][0])
    inter_pt_seg2+=point_in_segment(I2,lines[i][1],lines[i][0])
    inter_pt_seg3+=point_in_segment(I3,lines[i][1],lines[i][0])

print('\n')

# for i in range(6):
#     for j in range(3):
#         print(inter_point[j],point_in_segment(inter_point[j],lines[i][1],lines[i][0]))



inter_pt_seg = inter_pt_seg1+inter_pt_seg2+inter_pt_seg3
print(inter_pt_seg)

# print(inter_pt_seg)

if inter_pt_seg==2:
    for i in range(6):
        k=1
        for j in range(3):
            test=not(point_in_segment(inter_point[j],lines[i][1],lines[i][0]))
            k=k*test
        # print(k,i)
        if k==1:
            SEG3(lines,i,linesind)
    # if inter_pt_seg1==2:
    #     for i in range(6):
    #         nSEG1(I1,lines,i,linesind)
    # elif inter_pt_seg2==2:
    #     for i in range(6):
    #         nSEG1(I2,lines,i,linesind)
    # else :
    #     for i in range(6):
    #         nSEG1(I3,lines,i,linesind)
else:
    for j in range(3):
        for i in range(6):
            SEG1(inter_point[j],lines,i,linesind)


# print(linesind)
k=0
pts_in_env=0
for i in range(nbp):
    P=np.array([X[i],Y[i]])
    for j in range(len(linesind)):

        A=lines[linesind[j]][0]
        B=lines[linesind[j]][1]
        I=Inter_Hline_segment(A,B,P)[0]
        t=Inter_Hline_segment(A,B,P)[1]
        if t>0 and point_in_segment(I,A,B):
            k+=1
    if k%2==1 and k<4:
        plt.scatter(P[0],P[1],c='r')
        pts_in_env+=1

    k=0


print(pts_in_env)



plt.scatter(A1[0],A1[1],c='g')
plt.scatter(B1[0],B1[1],c='g')
plt.scatter(C1[0],C1[1],c='g')
plt.scatter(D1[0],D1[1],c='g')

plt.show()

