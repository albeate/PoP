import matplotlib.pyplot as plt

plt.ion()
plt.figure()
x=[-5,5]
for i in range(100):
    plt.clf() #delets the figure
    x=[x[0]+i*0.001, x[1]+i*0.001]
    plt.plot(x[0], x[1], '.') #draw a point
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.draw()

raw_input("Tryk <retur>")
plt.ioff()


def drawfigure(i, ax, fig):
    """Function that's called for each time-step"""
    ax.cla() #a method to delete the figure
    x = [-5,5]
    x = [x[0]+i*0.1, x[1]+i*0.1]
    fram = ax.plot(x[0], x[1], '.')
    plt.xlim(-5,5)
    ply.ylim(-5,5)
    return frame

matplotlib.use('Agg')
fig=plt.figure()
ax=plt.subplot(111)
ani = animation.FuncAnimation(fig, drawfigure, frames=xrange(100), fargs=(ax, fig), interval=1)
plt.show() 
