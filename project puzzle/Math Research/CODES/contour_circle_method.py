import Pixel_circle as pc
import numpy as np
import Len_file as lf
import imageio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import time


dir='//Users/martin//Desktop//project puzzle//Math Research//Circle_contour_method//'
P_id=1
file_contour=open(dir+'Contour_Piece_'+str(P_id)+'.txt','w')
file_in_point=open(dir+'In_point_Piece_'+str(P_id)+'.txt','w')
im = imageio.imread(dir+'//Pieces//P'+str(P_id)+'.jpg')
# print(im.shape)

xw=im.shape[1]
yw=im.shape[0]
# print(xw,yw)
ywh=yw/2-10
av=170




for i in range((xw-1)/10):
    y0=float(im[ywh,i*10][0])
    y1=float(im[ywh,(i+1)*10][0])
    if y0>av and y1<av:
        # plt.scatter(i,ywh,c='r')
        file_contour.write(str(i)+'\t'+str(ywh)+'\n')
        x_cont_init=i
        y_cont_init=ywh
        file_contour.write(str(x_cont_init)+'\t'+str(y_cont_init)+'\n')

print(x_cont_init,y_cont_init)



def next_point(x,y,r_circle):

    x1,y2=x,y
    X,Y=pc.pix_circle(r_circle,x,y)
    l=float(len(X))

    for i in range((len(X)-1)/10):
        y0=float(im[X[i*10],Y[i*10]][0])
        y1=float(im[X[(i+1)*10],Y[(i+1)*10]][0])

        if y0<av and y1>av:
            print('deg',i*10,l)
            deg=float((i*10*360)/l)
            print(deg)
            file_contour.write(str(X[i*10])+'\t'+str(Y[i*10])+'\t'+str(deg)+'\n')
            x=X[i*10]
            y=Y[i*10]
            # print(x,y)
            r_circle=20
    # print(x,y,r_circle,deg)
    if x1==x and y2==y:
        r_circle+=5



    return x,y,r_circle



r_circle=20
x,y,r_circle=next_point(x_cont_init,y_cont_init,r_circle)

for j in range(300):
    x,y,r_circle=next_point(x,y,r_circle)

file_contour.close()



