import imageio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

file=open('//Users/martin//Desktop//piece2.txt','w')

im = imageio.imread('//Users/martin//Desktop//project puzzle//puzzle2.jpeg')
print(im.shape)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# print(im[900,400])
# print(im[0,0])

# x=[]
# y=[]
# y2=[]
# y3=[]
# h=340
# # h=640
# inc=4
#
# xw=im.shape[1]
# yw=im.shape[0]
#
# margmin=int(0.1*xw)
# margmax=int(0.9*xw)
# for i in range(710):
#     x.append(i)
#     step0=int(im[h,i][0])
#     step1=int(im[h,i+inc][1])
#     step2=int(im[h,i+2*inc][1])
#     y.append((step1-step0)/inc)
#     # y2.append(((step2-step1)-(step1-step0))/inc**2)
#
#     # y1.append((im[h,i][0]))
#     # y2.append(im[h,i][1])
#     # y3.append(im[h,i][2])
#
#     # print(i,im[500,i][0])
# mini=y.index(min(y))
# print(mini)
# maxi=y.index(max(y))
# if mini > 0.2*xw and mini<0.8*xw and min(y)<-10:
#
#     mina=min(y[margmin:mini-10])
#     print(mina)
#     minb=min(y[mini+10:margmax])
#     print(minb)
#     mini2=min(mina,minb)
#     mini2ind=y.index(mini2)
#     print(mini2ind)
#     maxa=y[margmin:maxi-10].index(max(y[margmin:maxi-10]))
#     maxb=y[maxi+10:margmax].index(max(y[maxi+10:margmax]))
#     maxi2=max(maxa,maxb)
#
# plt.scatter(x,y)
# plt.scatter(x,y2)


# print(min(y1),y1.index(min(y1)))
# print(max(y1),y1.index(max(y1)))
# plt.plot(x,y2)
# plt.plot(x,y3)


###


xw=im.shape[1]
yw=im.shape[0]

margmin=int(0.1*xw)
margmax=int(0.9*xw)

x=[]
y=[]

X=[]
Y=[]
inc=5
for j in range(int(yw/10)):
    print(j)
    for i in range(xw-inc):
        step0=int(im[j*10,i][0])
        step1=int(im[j*10,i+inc][1])
        y.append((step1-step0)/inc)
    print(y.index(min(y)))
    mini=y.index(min(y))
    maxi=y.index(max(y))
    if mini > 0.2*xw and mini<0.8*xw and min(y)<-10:
        X.append(mini)
        file.write(str(mini)+'\t')
        Y.append(j*10)
        file.write(str(j*10)+'\n')
        X.append(maxi)
        file.write(str(maxi)+'\t')
        Y.append(j*10)
        file.write(str(j*10)+'\n')

        mina=min(y[margmin:mini-10])
        minb=min(y[mini+10:margmax])
        mini2=min(mina,minb)
        mini2ind=y.index(mini2)

        maxa=max(y[margmin:maxi-10])
        maxb=max(y[maxi+10:margmax])
        maxi2=max(maxa,maxb)
        maxi2ind=y.index(maxi2)
        if mini2 < 0.7*y[mini]:
            X.append(mini2ind)
            file.write(str(mini2ind)+'\t')
            Y.append(j*10)
            file.write(str(j*10)+'\n')
            X.append(maxi2ind)
            file.write(str(maxi2ind)+'\t')
            Y.append(j*10)
            file.write(str(j*10)+'\n')
    y=[]

plt.scatter(X,Y)

margmin=int(0.1*yw)
margmax=int(0.9*yw)
X1=[]
Y1=[]
inc=5
for j in range(int(xw/10)):
    print(j)
    for i in range(yw-inc):
        step0=int(im[i,j*10][0])
        step1=int(im[i+inc,j*10][1])
        y.append((step1-step0)/inc)
    print(y.index(min(y)),min(y))
    mini=y.index(min(y))
    maxi=y.index(max(y))
    if mini>0.2*yw and mini<0.8*yw and min(y)<-10:
        Y1.append(y.index(min(y)))
        X1.append(j*10)
        file.write(str(j*10)+'\t')
        file.write(str(mini)+'\n')
        Y1.append(y.index(max(y)))
        X1.append(j*10)
        file.write(str(j*10)+'\t')
        file.write(str(maxi)+'\n')

        mina=min(y[margmin:mini-10])
        minb=min(y[mini+10:margmax])
        mini2=min(mina,minb)
        mini2ind=y.index(mini2)

        maxa=max(y[margmin:maxi-10])
        maxb=max(y[maxi+10:margmax])
        maxi2=max(maxa,maxb)
        maxi2ind=y.index(maxi2)

        if mini2<0.7*y[mini]:
            Y1.append(mini2ind)
            X1.append(j*10)
            file.write(str(j*10)+'\t')
            file.write(str(mini2ind)+'\n')
            Y1.append(maxi2ind)
            X1.append(j*10)
            file.write(str(j*10)+'\t')
            file.write(str(maxi2ind)+'\n')
    y=[]

plt.scatter(X1,Y1,c='r')
plt.axis("Equal")





# X=[]
# Y=[]
# Z=[]
#
# xw=im.shape[1]
# yw=im.shape[0]
# print(xw,yw)
#
# for i in range(int(xw/10)):
#     for j in range(int(yw/10)):
#         X.append((i*10))
#         Y.append((j*10))
#         Z.append(im[(j*10),(i*10)][2])
#         # Z.append(0)
#
#
#
# ax.scatter3D(X,Y,Z,c=Z)
# plt.plot(X,Y,Z)
plt.show()
file.close()

