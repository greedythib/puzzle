import numpy as np
import Len_file as lf
import matplotlib.pyplot as plt

dir_file_Contour='//Users//martin//Desktop//project puzzle//Math Research//Circle_contour_method//Contour_Piece_5.txt'
num_pts=lf.len_file(dir_file_Contour)
file_contour=open(dir_file_Contour)

print(num_pts)

X=[]
Y=[]

point=[]
deg=[]
rl=file_contour.readline().split('\t')

for i in range(num_pts):
    rl=file_contour.readline().split('\t')
    print(rl)
    x=int(rl[0])
    y=int(rl[1])
    d=float(rl[2])
    X.append(x)
    Y.append(y)
    deg.append(d)
    point.append(i)

plt.scatter(X,Y,c='b')
# plt.plot(point,deg)
plt.show()