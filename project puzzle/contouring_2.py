import imageio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import time

dir='//Users/martin//Desktop//project puzzle//Math Research//'
P_id=2
file_contour=open(dir+'Contour_Piece_'+str(P_id)+'.txt','w')
file_in_point=open(dir+'In_point_Piece_'+str(P_id)+'.txt','w')


im = imageio.imread(dir+'//Pieces//P'+str(P_id)+'.jpg')
# print(im.shape)

xw=im.shape[1]
yw=im.shape[0]


x=[]
y0=[]

X=[]
Y=[]

inc=20
av=175

t0=time.time()

in_point=False


for l in range(yw/inc):
    # print(l)
    for i in range(xw/inc):
        step0=float(im[l*inc,i*inc][0])
        step1=float(im[l*inc,(i+1)*inc][0])
        y0=step0
        y1=step1
        if y0>av and y1<av:
            plt.scatter(i,l,c='b')
            file_contour.write(str(i)+'\t'+str(l)+'\n')
            in_point=True
        if y0<av and y1>av:
            plt.scatter(i,l,c='b')
            in_point=False
            file_contour.write(str(i)+'\t'+str(l)+'\n')
        if in_point:
            plt.scatter(i,l,c='g')
            file_in_point.write(str(i)+'\t'+str(l)+'\n')
    in_point=False




for l in range(xw/inc):
    for i in range(yw/inc):
        step0=float(im[i*inc,l*inc][0])
        step1=float(im[(i+1)*inc,l*inc][0])
        y0=step0
        y1=step1
        if (y0<av and y1>av) or (y0>av and y1<av):
            plt.scatter(l,i,c='r')
            file_contour.write(str(l)+'\t'+str(i)+'\n')
t1=time.time()
print(t1-t0)

file_contour.close()
file_in_point.close()

plt.legend()
plt.axis('equal')
plt.show()



