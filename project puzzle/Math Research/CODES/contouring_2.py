import imageio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import time


file=open('//Users/martin//Desktop//piece2.txt','w')

im = imageio.imread('//Users/martin//Desktop//project puzzle//puzzle5.jpeg')
# print(im.shape)

xw=im.shape[1]
yw=im.shape[0]

margmin=int(0.1*xw)
margmax=int(0.9*xw)

x=[]
y0=[]

X=[]
Y=[]

inc=10
av=125

t0=time.time()

in_point=False


for l in range(yw/inc):
    print(l)
    for i in range(xw/inc):
        step0=float(im[l*inc,i*inc][0])
        step1=float(im[l*inc,(i+1)*inc][0])
        y0=step0
        y1=step1
        if y0>av and y1<av:
            plt.scatter(i,l,c='b')
            in_point=True
        if y0<av and y1>av:
            plt.scatter(i,l,c='b')
            in_point=False
        if in_point:
            plt.scatter(i,l,c='g')


for l in range(xw/inc):
    for i in range(yw/inc):
        step0=float(im[i*inc,l*inc][0])
        step1=float(im[(i+1)*inc,l*inc][0])
        y0=step0
        y1=step1
        if (y0<av and y1>av) or (y0>av and y1<av):
            plt.scatter(l,i,c='r')

t1=time.time()
print(t1-t0)


plt.legend()
plt.axis('equal')
plt.show()



