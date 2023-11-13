import numpy
from matplotlib import pyplot

x = []
y = []
z = []
g = []
for i in range(0,404):
    import json
    with open("data_4/data_ear_rotation_{}.json".format(i),"r") as fp:
        data=json.load(fp)
    x.append(i)
    y.append(float(str(data["angle_x"])[:5]))
    z.append(float(str(data["angle_y"])[:5]))
    g.append(float(str(data["angle_z"])[:5]))
# x = numpy.arange(10)
# y = numpy.array([5,3,4,2,7,5,4,6,3,2])

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.set_ylim(min([min(y),min(z),min(g)]),max([max(y),max(z),max(g)]))
pyplot.plot(x,y)
pyplot.plot(x,z)
pyplot.plot(x,g)
# for i,j in zip(x,y):
#     ax.annotate(str(j),xy=(i,j))

# for i1,j1 in zip(x,z):
#     ax.annotate(str(j1),xy=(i1,j1))


# for i2,j2 in zip(x,g):
#     ax.annotate(str(j2),xy=(i2,j2))

pyplot.show()